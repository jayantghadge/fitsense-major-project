# FitSenseAI-Powered Gym Trainer

FitSense is an innovative AI-powered gym trainer that assists users in maintaining proper form and technique during their workout routines. It provides real-time feedback and guidance, counts repetitions, and assesses the accuracy of exercises to help users achieve their fitness goals safely and effectively.

## Features

- Real-time Pose Estimation: FitSense utilizes MediaPipe for real-time body pose estimation.
- Exercise Guidance: The application provides step-by-step guidance for various exercises, ensuring users perform them correctly.
- Repetition Count: FitSense counts repetitions and tracks the user's progress.
- Accuracy Assessment: The AI assesses the user's form and provides feedback on the accuracy of their movements.
- User-Friendly Interface: The web application offers an easy-to-use and intuitive interface.

## Screenshots

| Login Page | Home Page - Displaying list of all Exercises |
| ------- | ------- |
| ![output1](https://github.com/jayantghadge/fitsense-major-project/assets/88991259/a7d1aed8-877e-4257-bc63-d3e3d2b5a45c) | ![output2](https://github.com/jayantghadge/fitsense-major-project/assets/88991259/8fe4b071-b25d-4566-81b4-1144b5f83376) |


| Real-time pose estimation | Dashboard |
| ------- | ------- |
| ![output3](https://github.com/jayantghadge/fitsense-major-project/assets/88991259/9ee4f9a7-b3b7-43ce-82b0-08bcaa9be580)| ![output4](https://github.com/jayantghadge/fitsense-major-project/assets/88991259/af887272-ca88-4545-bd1a-05bd08e3c36c) |

## Technologies Used

- Mediapipe : For real-time pose estimation.
- HTML, CSS, and JavaScript: Used to create the user interface and interact with the AI model.
- OpenCV: Used for computer vision tasks, image processing, and real-time video analysis.
- Flask: A micro web framework for routing and serving the web application.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/fitsense.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:

   ```bash
   python app.py
   ```

4. Access the web application in your browser at `http://localhost:5000`.

## Usage

1. Launch the FitSense web application.
2. Select an exercise or workout routine.
3. The AI will provide real-time feedback on your performance.
4. Track your repetition count and accuracy to optimize your workout.

## Contributing

We welcome contributions from the open-source community. If you'd like to contribute to Searchify, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix:
   ```sh
   git checkout -b feature/your-feature-name
   ```

3. Commit your changes and push to your fork:
   ```sh
   git commit -m "Add your feature"
   git push origin feature/your-feature-name
   ```

4. Open a pull request on the original repository.

