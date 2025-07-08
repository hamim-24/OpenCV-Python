import numpy as np  # Importing numpy for array manipulation
import cv2 as cv

# mouse callback function
def draw_text(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        font = cv.FONT_HERSHEY_SIMPLEX
        print(f"Mouse Coordinates: ({x}, {y})")
        cv.putText(img, 'Hello', (x, y), font, 1, (255, 255, 255), 2)


def show_coordinates(event, x, y, flags, param):
    if event == cv.EVENT_MOUSEMOVE:
        print(f"Mouse Coordinates: ({x}, {y})")

# Initialize a black image
img = np.zeros((512, 512, 3), np.uint8)  # Create a black image of size 512x512 with 3 color channels (BGR)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_text)


while (1):
    cv.imshow('image', img)
    if cv.waitKey(1) & 0xFF == 27:
        break


cv.destroyAllWindows()
