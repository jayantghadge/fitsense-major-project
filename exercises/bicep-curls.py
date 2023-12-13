import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture(0)


def calculate_angle(a, b, c):
    a = np.array(a)  # First point
    b = np.array(b)  # Mid point
    c = np.array(c)  # End point

    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - \
        np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)

    if angle > 180.0:
        angle = 360-angle

    return angle


# Curl counter variables
count = 0
stage = None

<<<<<<< HEAD
target_angle = 90.0
=======
target_angle = 90.0  
>>>>>>> 6b964447250138097481027b1c05fdb602c693c6

# Accuracy variable
accuracy = 0.0

# Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        results = pose.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Extract landmarks
        try:
            landmarks = results.pose_landmarks.landmark

            shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

            angle = calculate_angle(shoulder, elbow, wrist)

            cv2.putText(image, str(angle),
                        tuple(np.multiply(elbow, [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,
                                                        255, 255), 2, cv2.LINE_AA
                        )

            # Curl counter logic
            if angle > 160:
                stage = "down"  # down curl
            if angle < 30 and stage == 'down':
                stage = "up"
                count += 1

<<<<<<< HEAD
            # Calculate accuracy as the percentage
=======
            # Calculate accuracy as the percentage 
>>>>>>> 6b964447250138097481027b1c05fdb602c693c6
            accuracy = 100.0 - abs(target_angle - angle)
            accuracy = max(accuracy, 0.0)
            accuracy = min(accuracy, 100.0)

        except:
            pass

        cv2.rectangle(image, (0, 0), (225, 73), (245, 117, 16), -1)

        cv2.putText(image, 'REPS', (15, 12), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 0, 0), 1, cv2.LINE_AA)
        cv2.putText(image, str(count), (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

        cv2.putText(image, 'STAGE', (65, 12),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
        cv2.putText(image, stage, (60, 60), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (255, 255, 255), 2, cv2.LINE_AA)

        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(
                                      color=(245, 117, 66), thickness=2, circle_radius=2),
                                  mp_drawing.DrawingSpec(
                                      color=(245, 66, 230), thickness=2, circle_radius=2)
                                  )

        cv2.imshow('My WebCam', image)

        key = cv2.waitKey(10)
        if key == ord('q'):
            break

print(count)
print(int(accuracy))

cap.release()
cv2.destroyAllWindows()
