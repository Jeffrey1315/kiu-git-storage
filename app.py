# Добавляем нужные библиотеки (scikit-image, numpy, sklearn, python-telegram-bot) для создания Telegram-бота, 
# который определяет что на фото (Cow/Landscape)

import os
from skimage.io import imread
from skimage.transform import resize
from skimage.feature import hog
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from joblib import dump, load
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


def load_images_from_folder(folder):
    images = []
    labels = []
    for filename in os.listdir(folder):
      # Проверка формат файла
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            img = imread(os.path.join(folder,filename))
            if img is not None:
              # Приведение всех изображений к одному размеру
                img_resized = resize(img, (128, 64))
                images.append(img_resized)
                labels.append(folder)
    return images, labels

# Загрузка изображений из каждой папки
class1_images, class1_labels = load_images_from_folder('Images/Cow')
class2_images, class2_labels = load_images_from_folder('Images/Landscape')

# Объединение данных
images = class1_images + class2_images
labels = class1_labels + class2_labels


# Извлечение признаков с помощью HOG.
# Функция принимает список изображений (images)
# и возвращает список "гистограмм направленных градиентов" (HOG) 
# для каждого изображения. 
# HOG - это метод извлечения признаков из изображений, 
# который используется в компьютерном зрении для распознавания объектов.


def extract_hog_features(images):
    hog_features = []
    for image in images:
        fd = hog(image, orientations=8, pixels_per_cell=(16, 16),
                 cells_per_block=(1, 1), visualize=False, channel_axis=-1)
        hog_features.append(fd)
    return hog_features

# Извлечение HOG признаков

features = extract_hog_features(images)


# Разделение данных,    обучение классификатора,    тестирование
# Разделение данных на обучающую и тестовую выборки
# Извлеченные признаки подготавливаются для обучения: данные разделяются на обучающую (X_train, y_train) и тестовую (X_test, y_test) выборки.
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Обучение классификатора
clf = SVC()
clf.fit(X_train, y_train)

# Тестирование модели
y_pred = clf.predict(X_test)

#Сохранение модели в файл с помощью библиотеки joblib
dump(clf, 'hog_classifier.joblib')

# Функция "predict_image_class" загружает сохраненную модель и предсказывает класс изображения (корова или пейзаж) на основе HOG-признаков.

def predict_image_class(image_path):
    # Загрузка обученной модели
    loaded_clf = load('hog_classifier.joblib')

    # Загрузка изображения
    img = imread(image_path)
    img_resized = resize(img, (128, 64))

    # Извлечение HOG признаков
    hog_features = extract_hog_features([img_resized])

    # Тестирование
    prediction = loaded_clf.predict(hog_features)

    return prediction[0]


loaded_clf = load('hog_classifier.joblib')

# Функция "start" выводит заданный текст при написании /start боту в Telegram
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Определитель коров и пейзажей')


def handle_image(update: Update, context: CallbackContext) -> None:
    photo_file = update.message.photo[-1].get_file()
    photo_path = f"images/{update.message.chat_id}_{photo_file.file_id}.jpg"
    photo_file.download(photo_path)

    # Загрузка фото
    img = imread(photo_path)
    img_resized = resize(img, (128, 64))

    # Извлечение HOG признаков
    hog_features = extract_hog_features([img_resized])

    # Определение коровы или поля
    prediction = loaded_clf.predict(hog_features)

    result_message = ""
    if prediction[0] == 'Images/Cow':
        result_message = "Это корова!"
    elif prediction[0] == 'Images/Landscape':
        result_message = "Это пейзаж!"
    else:
        result_message = "Неизвестно"

    update.message.reply_text(result_message)


def main() -> None:
    # Настройки Telegram-бота
    updater = Updater("6619874552:AAE_DjjVGeQOOdB-TBdqo5oqqGm-9wd9bFQ")
    dp = updater.dispatcher

    # Добавление команд Telegram-боту
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.photo, handle_image))

    # Запуск Telegram-бота
    updater.start_polling()

    # Запуск бота, до тех пор, пока не будет команды остановиться
    updater.idle()


if __name__ == '__main__':
    main()