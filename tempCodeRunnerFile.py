from flask import Flask, render_template, request, redirect, url_for
import subprocess
import os

app = Flask(__name__)

exercises = [
    {"name": "Push-up", "area": "Chest, Shoulders, Triceps", "difficulty": "Moderate"},
    {"name": "Squats", "area": "Legs, Glutes", "difficulty": "Easy"},
    {"name": "Plank", "area": "Core", "difficulty": "Easy"},
    {"name": "Jumping Jacks", "area": "Full Body", "difficulty": "Easy"},
    {"name": "Lunges", "area": "Legs, Glutes", "difficulty": "Moderate"},
    {"name": "Bicep-Curls", "area": "Biceps", "difficulty": "Moderate"},
    {"name": "Sit-ups", "area": "Core", "difficulty": "Easy"},
    {"name": "Leg Raises", "area": "Lower Abs", "difficulty": "Moderate"},
    {"name": "Yoga Pose 1", "area": "Various", "difficulty": "Varies"},
    {"name": "Yoga Pose 2", "area": "Various", "difficulty": "Varies"}
]


def estimate_exercise_accuracy(exercise_name):
    try:

        exercise_script = exercise_name.lower() + ".py"
        script_path = os.path.join("exercises", exercise_script)

        result = subprocess.check_output(['python', script_path], text=True)

        count = int(result.strip())
        return count
    except subprocess.CalledProcessError:
        return "Error running exercise estimation"


@app.route('/')
def exercise_list():
    return render_template('exercise_analysis.html', exercises=exercises)


@app.route('/estimate/<exercise_name>')
def estimate(exercise_name):
    for exercise in exercises:
        if exercise_name.lower() == exercise['name'].lower():
            count = estimate_exercise_accuracy(exercise_name)
            return render_template('exercise_result.html', exercise_name=exercise['name'], count=count)

    return "Exercise not found"


if __name__ == "__main__":
    app.run(debug=True)
