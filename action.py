import threading
import webbrowser
from time import sleep
from pynput.keyboard import Key, Controller
import cv2
import calculations


# Works out which action to do
def action(indexThumbDistance, pinkyThumbDistance):
    # Action becomes nothing if the indexThumbDistance hasn't changed much
    if indexThumbDistance < 0.1:
        drawText = "Jump"
        thread = threading.Thread(target=pressUp)
        thread.start()

    elif pinkyThumbDistance < 0.08:
        drawText = "Duck"
        thread = threading.Thread(target=pressDown)
        thread.start()

    else:
        drawText = ""
    return drawText


def DoAction(image, results, distanceList):
    # Get the height and width of the input image.
    height, width, _ = image.shape

    # Initialises drawText and newDistanceList
    drawText = ""
    newDistanceList = []

    # Create a copy of the input image to write the action on.
    outputImage = image.copy()

    # Iterate over the hands in the image
    for hand, handInfo in enumerate(results.multi_handedness):
        # Retrieve ALL of the landmarks of the found hand.
        handLandmarks = results.multi_hand_landmarks[hand]

        # Sets the coordinates of the thumb-pinky and thumb-index
        indexThumbDistance, pinkyThumbDistance = calculations.setCoordinates(handLandmarks)

        # Works out which action to do
        drawText = action(indexThumbDistance, pinkyThumbDistance)

        # Creates a new indexThumbDistance list with the last 4 distances
        newDistanceList = [distanceList[1], distanceList[2], distanceList[3], indexThumbDistance]

    # Write the action on the output image.
    # Parameters (image, text to be drawn, coordinates, font, font scale, colour, thickness, line type)
    cv2.putText(outputImage, drawText, (900, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 6)

    # Return the output image, the status of each finger and the count of the fingers up of both hands.
    return outputImage, newDistanceList


# Presses the up key when called
def pressUp():
    keyboard = Controller()
    keyboard.press(Key.up)
    keyboard.release(Key.up)


# Presses the down key when called
def pressDown():
    keyboard = Controller()
    with keyboard.pressed(Key.down):
        sleep(0.5)


def openGame():
    webbrowser.open('https://dino-chrome.com/en')


def checkEscape():
    # Wait for 1ms. If a key is pressed, retrieve the ASCII code of the key.
    k = cv2.waitKey(1) & 0xFF

    # Check if 'ESC' is pressed and break the loop.
    if k == 27:
        return True
