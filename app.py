from flask import Flask, render_template, request, redirect, url_for
import subprocess
import os

app = Flask(__name__)

# Sample data for demonstration (replace with your data)
exercises = [
    {"name": "Push-up", "description": "Perform push-up exercise."},
    {"name": "Squats", "description": "Perform squats."},
    {"name": "Plank", "description": "Hold a plank position."},
    {"name": "Jumping Jacks", "description": "Perform jumping jacks."},
    {"name": "Lunges", "description": "Perform lunges."},
    {"name": "Bicep-Curls", "description": "Do bicep curls with dumbbells."},
    {"name": "Sit-ups", "description": "Perform sit-up exercises."},
    {"name": "Leg Raises", "description": "Perform leg raises."},
    {"name": "Yoga Pose 1", "description": "Description for Yoga Pose 1."},
    {"name": "Yoga Pose 2", "description": "Description for Yoga Pose 2."}]


# Function to estimate exercise accuracy by running the exercise-specific script


def estimate_exercise_accuracy(exercise_name):
    try:
        # Get the path to the exercise-specific script
        exercise_script = exercise_name.lower() + ".py"
        script_path = os.path.join("exercises", exercise_script)

        # Run the exercise-specific script and capture its output
        result = subprocess.check_output(['python', script_path], text=True)

        # Parse the count from the script's output (assuming the count is printed in the script)
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
