from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Students(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(55), nullable = False)

    def __repr__(self):
        return '<Article %r>' % self.id

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/students')
def show_students():
    students = Students.query.all()
    return render_template('students.html', students=students)


@app.route('/students/<int:id>')
def students_info(id):
    students = Students.query.get(id)
    return render_template('students_detail.html', students=students)


@app.route('/create', methods=['POST', 'GET'])
def create_students():
    if request.method == 'POST':
        name = request.form['name']

        students = Students(name=name)

        try:
            db.session.add(students)
            db.session.commit()
            return redirect('students')
        
        except:
            return 'При добавлении студента произошла ошибка'
    else:
        return render_template('create.html')


@app.route('/students/<int:id>/delete')
def students_delete(id):
    students = Students.query.get_or_404(id)

    try:
        db.session.delete(students)
        db.session.commit()
        return redirect('/students')
    except:
        return 'При удалении студента произошла ошибка'

@app.route('/students/<int:id>/update', methods = ['POST', 'GET'])
def students_update(id):
    students = Students.query.get(id)
    if request.method == "POST":
        students.name = request.form["name"]

        try:
            db.session.commit()
            return redirect('/students')
        except:
            return "При редактировании человека произошла ошибка"
    else:
        return render_template("students_update.html", students=students)  



if __name__ == '__main__':
    app.run(debug=True)