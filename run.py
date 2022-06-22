import action
import detectLandmarks
import webcam
import mediapipe as mp


def run():
    # Initialise the mediapipe hands class
    handsMP = mp.solutions.hands

    # Sets up the hands functions for images and videos
    hands = handsMP.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)

    # Initialise the mediapipe drawing class.
    drawingMP = mp.solutions.drawing_utils

    # Initialize the VideoCapture object to read from the webcam.
    cameraVideo = webcam.initialiseWebcam()

    # Initialise the distanceList
    distanceList = [0, 0, 0, 0]
    action.openGame()

    # Create named window for resizing purposes.
    webcam.createWindow()

    # Iterate until the webcam is accessed successfully.
    while cameraVideo.isOpened():

        # Reads the frame
        success, frame = webcam.readFrame(cameraVideo)

        # Check if frame is not read properly then continue to the next iteration to read the next frame.
        if not success:
            break

        # Flip the frame horizontally for natural (selfie-view) visualization.
        frame = webcam.flipFrame(frame)

        # Perform Hands landmarks detection on the frame.
        frame, results = detectLandmarks.detectHandsLandmarks(frame, hands, handsMP, drawingMP)

        # Check if the hands landmarks in the frame are detected.
        if results.multi_hand_landmarks:
            # Count the number of fingers up of each hand in the frame.
            frame, distanceList = action.DoAction(frame, results, distanceList)

        # Display the frame.
        webcam.displayFrame(frame)

        if action.checkEscape():
            break

    # Release the VideoCapture Object and close the windows.
    webcam.stopWebcam(cameraVideo)