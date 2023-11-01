from flask import Flask, render_template
from flask import request, redirect, url_for, session
import subprocess
import os
app = Flask(__name__)
app.secret_key = 'dfhjdjd89d'

exercises = [
    {"name": "Push-up", "area": "Chest, Shoulders, Triceps",
        "difficulty": "Moderate", "calories_burnt": 100},
    {"name": "Squats", "area": "Legs, Glutes",
        "difficulty": "Easy", "calories_burnt": 70},
    {"name": "Plank", "area": "Core", "difficulty": "Easy", "calories_burnt": 50},
    {"name": "Jumping Jacks", "area": "Full Body",
        "difficulty": "Easy", "calories_burnt": 80},
    {"name": "Lunges", "area": "Legs, Glutes",
        "difficulty": "Moderate", "calories_burnt": 90},
    {"name": "Bicep-Curls", "area": "Biceps",
        "difficulty": "Moderate", "calories_burnt": 60},
    {"name": "Sit-ups", "area": "Core", "difficulty": "Easy", "calories_burnt": 40},
    {"name": "Leg Raises", "area": "Lower Abs",
        "difficulty": "Moderate", "calories_burnt": 70},
    {"name": "Yoga Pose 1", "area": "Various",
        "difficulty": "Varies", "calories_burnt": 80},
    {"name": "Yoga Pose 2", "area": "Various",
        "difficulty": "Varies", "calories_burnt": 90}
]

opencv_window_status = {}
username = "jayant"
password = "ghadge"


def run_exercise_analysis(exercise_name):
    script_path = os.path.join("exercises", exercise_name.lower() + ".py")
    subprocess.run(['python', script_path])


def estimate_exercise_accuracy(exercise_name):
    try:
        exercise_script = exercise_name.lower() + ".py"
        script_path = os.path.join("exercises", exercise_script)
        result = subprocess.check_output(['python', script_path], text=True)

        count_str, accuracy_str = result.strip().split('\n')
        count = int(count_str)
        accuracy = int(accuracy_str)

        return count, accuracy
    except subprocess.CalledProcessError:
        return 0, 0


@app.route('/')
def exercise_list():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('exercise_analysis.html', exercises=exercises)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        entered_username = request.form.get(
            'username')
        entered_password = request.form.get(
            'password')

        if entered_username == username and entered_password == password:
            session['logged_in'] = True
            return redirect('/')
    return render_template('login.html')


@app.route('/exercise_pose/<exercise_name>')
def exercise_pose(exercise_name):
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    exercise = next(
        (e for e in exercises if e["name"].lower() == exercise_name), None)
    if exercise:
        return render_template('exercise_pose.html', exercise_name=exercise_name, exercise_area=exercise["area"])
    else:
        return "Exercise not found"


@app.route('/exercise_result/<exercise_name>')
def exercise_result(exercise_name):
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    if exercise_name in opencv_window_status and opencv_window_status[exercise_name]:
        return "Waiting for the OpenCV window to close..."
    else:
        exercise = next(
            (e for e in exercises if e["name"].lower() == exercise_name), None)
        if exercise:
            count, accuracy = estimate_exercise_accuracy(exercise_name)
            show_camera = True
            return render_template('exercise_result.html', exercise_name=exercise_name, count=count, accuracy=accuracy, show_camera=show_camera, calories_burnt=exercise["calories_burnt"])
        else:
            return "Exercise not found"


if __name__ == "__main__":
    app.run(debug=True)
