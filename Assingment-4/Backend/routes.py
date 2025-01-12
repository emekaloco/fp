from flask import Blueprint, request, jsonify
from models import Exercise, CollectionManager

# routes file. i use this to create the api endpoints for the backend.

main_bp = Blueprint("main", __name__)

# collection manager. handles all the exercises and stores them.
collection = CollectionManager()

# gets all exercises from the collection
@main_bp.route("/exercises", methods=["GET"])
def get_exercises():
    # sends back all the exercises as a json response
    return jsonify(collection.to_list()), 200

# adds a new exercise to the collection
@main_bp.route("/exercises", methods=["POST"])
def add_exercise():
    # takes data from the request and creates a new exercise
    data = request.get_json()
    if not data or "name" not in data or "muscle_group" not in data or "equipment" not in data:
        # if the data is invalid, sends back an error
        return jsonify({"error": "Invalid data"}), 400

    # creates a new exercise object and adds it to the collection
    new_exercise = Exercise(
        name=data["name"],
        muscle_group=data["muscle_group"],
        equipment=data["equipment"]
    )
    collection.add_exercise(new_exercise)
    return jsonify({"message": "Exercise added successfully!"}), 201

# deletes an exercise by name
@main_bp.route("/exercises/<name>", methods=["DELETE"])
def delete_exercise(name):
    # looks for the exercise and removes it. if not found, returns an error.
    exercise = collection.find_exercise(name)
    if exercise:
        collection.remove_exercise(name)
        return jsonify({"message": f"Exercise '{name}' deleted successfully!"}), 200
    return jsonify({"error": "Exercise not found"}), 404

# updates an existing exercise by name
@main_bp.route("/exercises/<name>", methods=["PUT"])
def update_exercise(name):
    # gets the new data and updates the exercise if it exists
    data = request.get_json()
    exercise = collection.find_exercise(name)
    if not exercise:
        return jsonify({"error": "Exercise not found"}), 404

    # updates the muscle group and/or equipment
    if "muscle_group" in data:
        exercise.muscle_group = data["muscle_group"]
    if "equipment" in data:
        exercise.equipment = data["equipment"]

    return jsonify({"message": f"Exercise '{name}' updated successfully!"}), 200

# filters exercises by muscle group
@main_bp.route("/exercises/filter", methods=["GET"])
def filter_exercises():
    # checks if muscle_group is passed as a query parameter
    muscle_group = request.args.get("muscle_group")
    if not muscle_group:
        # sends an error if muscle_group is missing
        return jsonify({"error": "Please specify a muscle group"}), 400

    # filters the exercises by the given muscle group
    filtered = [ex for ex in collection.to_list() if ex["muscle_group"] == muscle_group]
    return jsonify(filtered), 200