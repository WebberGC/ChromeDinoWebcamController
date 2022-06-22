import math


# Calculates the distance
def calculateDistance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist


# Sets the coordinates of the thumb-pinky and thumb-index
def setCoordinates(handLandmarks):
    # Gather the X and Y coordinates of the thumb and the index finger
    thumby = handLandmarks.landmark[4].y
    thumbx = handLandmarks.landmark[4].x
    indexy = handLandmarks.landmark[8].y
    indexx = handLandmarks.landmark[8].x
    pinkyy = handLandmarks.landmark[20].y
    pinkyx = handLandmarks.landmark[20].y

    # Calculates the distance between the tip of the thumb and the tip of the index finger
    indexThumbDistance = calculateDistance(thumbx, thumby, indexx, indexy)
    pinkyThumbDistance = calculateDistance(thumbx, thumby, pinkyx, pinkyy)

    return indexThumbDistance, pinkyThumbDistance