def warn_the_sheep(queue):
    queue = queue[::-1]
    counter = 0
    for i, animal in enumerate(queue):
        if animal == "wolf":
            counter = i
    if counter == 0:
        return "Pls go away and stop eating my sheep"
    return f"Oi! Sheep number {counter}! You are about to be eaten by a wolf!"
