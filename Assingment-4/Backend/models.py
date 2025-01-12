# models file. i write all the stuff here that has the exercise class and collection manager.

class Exercise:
    def __init__(self, name, muscle_group, equipment):
        # this takes the name, muscle group, and the equipment and creates a new exercise
        self.name = name
        self.muscle_group = muscle_group
        self.equipment = equipment

    def to_dict(self):
        # so i use this to convert an exercise into a dictionary. useful for sending json stuff.
        return {
            "name": self.name,
            "muscle_group": self.muscle_group,
            "equipment": self.equipment
        }


class CollectionManager:
    def __init__(self):
        # i make this to manage all the exercises. it's a list that keeps them.
        self.exercises = []

    def add_exercise(self, exercise):
        # adds an exercise to the list.
        self.exercises.append(exercise)

    def remove_exercise(self, name):
        # removes the exercise that has the given name from the list
        self.exercises = [ex for ex in self.exercises if ex.name != name]

    def find_exercise(self, name):
        # finds an exercise by name and returns it. if it doesn’t exist, returns none.
        return next((ex for ex in self.exercises if ex.name == name), None)

    def update_exercise(self, name, muscle_group=None, equipment=None):
        # updates the muscle group or equipment of an exercise if it exists
        exercise = self.find_exercise(name)
        if exercise:
            if muscle_group:
                exercise.muscle_group = muscle_group
            if equipment:
                exercise.equipment = equipment
        return exercise

    def to_list(self):
        # converts all the exercises to a list of dictionaries for sending as json
        return [ex.to_dict() for ex in self.exercises]