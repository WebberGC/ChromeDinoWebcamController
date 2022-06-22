import cv2


def detectHandsLandmarks(image, hands, mp_hands, mp_drawing):
    # Create a copy of the input image to draw landmarks on.
    outputImage = image.copy()

    # Convert the image from BGR into RGB format.
    imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Perform the Hands Landmarks Detection.
    results = hands.process(imgRGB)

    # Check if landmarks are found and are specified to be drawn.
    if results.multi_hand_landmarks:

        # Iterate over the found hands.
        for handLandmarks in results.multi_hand_landmarks:

            # Draw the hand landmarks on the copy of the input image.
            mp_drawing.draw_landmarks(image=outputImage, landmark_list=handLandmarks,
                                      connections=mp_hands.HAND_CONNECTIONS,
                                      landmark_drawing_spec=mp_drawing.DrawingSpec(color=(255, 255, 255),
                                                                                   thickness=2, circle_radius=2),
                                      connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0),
                                                                                     thickness=2, circle_radius=2))

    # Return the output image and results of hands landmarks detection.
    return outputImage, results