import pickle

class Fruit(object):

    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def __str__(self):
        return "{}: {}".format(self.name, self.calories)


if __name__ == "__main__":
    fruit = Fruit("apple", 190)
    print(fruit)

    with open('data.pickle', 'wb') as file:
        pickle.dump(fruit, file)

    with open('data.pickle', 'rb') as file:
        data = pickle.load(file)
        print(data)