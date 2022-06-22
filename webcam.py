import cv2


def initialiseWebcam():
    cameraVideo = cv2.VideoCapture(0)
    cameraVideo.set(3, 1280)
    cameraVideo.set(4, 960)
    return cameraVideo


# Create named window for resizing purposes.
def createWindow():
    cv2.namedWindow('T-Rex Chrome Dinosaur Controls', cv2.WINDOW_NORMAL)


# Reads the frame
def readFrame(cameraVideo):
    # Read a frame.
    success, frame = cameraVideo.read()
    return success, frame


# Flip the frame horizontally for natural (selfie-view) visualization.
def flipFrame(frame):
    # Flip the frame horizontally for natural (selfie-view) visualization.
    frame = cv2.flip(frame, 1)
    return frame


def displayFrame(frame):
    cv2.imshow('T-Rex Chrome Dinosaur Controls', frame)


def stopWebcam(cameraVideo):
    cameraVideo.release()
    cv2.destroyAllWindows()