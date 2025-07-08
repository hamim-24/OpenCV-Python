import numpy as np  # Importing numpy for numerical operations(drawing shapes)
import cv2 as cv  # Importing OpenCV for image processing

image = np.zeros((500, 500, 3), dtype=np.uint8)
# Create a black image of size 500x500 with 3 color channels (BGR)

"""
Draws a polygon on an image.

Parameters:
- image: The image on which to draw the polygon.
- vertices: A list of points defining the polygon.
- color: The color of the polygon in BGR format (default is green).
- thickness: The thickness of the polygon's outline (default is 2).

Returns:
- The image with the drawn polygon.
"""


def draw_polygon(image, vertices, color=(0, 255, 0), thickness=2):
    if len(vertices) < 3:
        raise ValueError("Polygon must have at least three vertices.")

    # Convert vertices to a numpy array
    points = np.array(vertices, np.int32)

    # Draw the polygon on the image
    cv.polylines(image, [points], isClosed=True,
                 color=color, thickness=thickness)

    return image


"""
Draws a specified shape on an image.

Parameters:
- image: The image on which to draw the shape.
- shape: A list of points defining the shape.
- color: The color of the shape in BGR format (default is green).
- thickness: The thickness of the shape's outline (default is 2).

Returns:
- The image with the drawn shape.
"""


def draw_shape(image, shape, color=(0, 255, 0), thickness=2):
    if len(shape) < 2:
        raise ValueError("Shape must have at least two points.")

    # Convert shape points to a numpy array
    points = np.array(shape, np.int32)

    # Draw the shape on the image
    cv.polylines(image, [points], isClosed=True,
                 color=color, thickness=thickness)

    return image


"""
Draws a circle on an image.
Parameters:
- image: The image on which to draw the circle.
- center: The center of the circle as (x, y).
- radius: The radius of the circle.
- color: The color of the circle in BGR format (default is green).
- thickness: The thickness of the circle's outline (default is 2).

Returns:
- The image with the drawn circle.
"""


def draw_circle(image, center, radius, color=(0, 255, 0), thickness=2):
    if radius <= 0:
        raise ValueError("Radius must be a positive integer.")

    # Draw the circle on the image
    cv.circle(image, center, radius, color, thickness)

    return image


"""
Draws a rectangle on an image.

Parameters:
- image: The image on which to draw the rectangle.
- top_left: The top-left corner of the rectangle as (x, y).
- bottom_right: The bottom-right corner of the rectangle as (x, y).
- color: The color of the rectangle in BGR format (default is green).
- thickness: The thickness of the rectangle's outline (default is 2).

Returns:
- The image with the drawn rectangle.
"""


def draw_rectangle(image, top_left, bottom_right, color=(0, 255, 0), thickness=2):
    if top_left[0] >= bottom_right[0] or top_left[1] >= bottom_right[1]:
        raise ValueError("Invalid rectangle coordinates.")

    # Draw the rectangle on the image
    cv.rectangle(image, top_left, bottom_right, color, thickness)

    return image


"""
Draws a line on an image.

Parameters:
- image: The image on which to draw the line.
- start_point: The starting point of the line as (x, y).
- end_point: The ending point of the line as (x, y).
- color: The color of the line in BGR format (default is green).
- thickness: The thickness of the line (default is 2).

Returns:
- The image with the drawn line.
"""


def draw_line(image, start_point, end_point, color=(0, 255, 0), thickness=2):
    # Draw the line on the image
    cv.line(image, start_point, end_point, color, thickness)

    return image


"""
Draws text on an image.

Parameters:
- image: The image on which to draw the text.
- text: The text to draw.
- position: The position of the text as (x, y).
- font: The font type (default is cv.FONT_HERSHEY_SIMPLEX).
- font_scale: The scale of the font (default is 1).
- color: The color of the text in BGR format (default is green).
- thickness: The thickness of the text (default is 2).

Returns:
- The image with the drawn text.
"""


def draw_text(image, text, position, font=cv.FONT_HERSHEY_SIMPLEX, font_scale=1, color=(0, 255, 0), thickness=2):
    # Draw the text on the image
    cv.putText(image, text, position, font, font_scale, color, thickness)

    return image


while True:
    cv.rectangle(image, (image.shape[0]//4, image.shape[1]//4),
                 (3 * image.shape[0]//4, 3 * image.shape[1]//4), (0, 255, 0), thickness=-1)    
    cv.circle(image, (image.shape[0]//2, image.shape[1]//2), 100, (0, 0, 255), thickness=-1)
    cv.putText(image, 'Bangladesh', (40, 3 * image.shape[1]//4 + 100), color=(255, 255, 255), fontScale=1, fontFace=cv.FONT_HERSHEY_SIMPLEX)
    cv.imshow('Circle', image)
    
    # # Draw a rectangle
    # draw_rectangle(image, (50, 50), (200, 200), color=(0, 255, 255), thickness=-1)

    # # Draw a line
    # draw_line(image, (50, 250), (200, 250), color=(255, 0, 255), thickness=4)

    # # Draw text
    # draw_text(image, "Hello OpenCV", (50, 300), color=(255, 255, 0), font_scale=1.5)

    # # Draw a polygon
    # draw_polygon(image, [(300, 100), (400, 150), (350, 200), (300, 200), (250, 150)], color=(0, 0, 255), thickness=3)

    # Show the image

    if cv.waitKey(0):
        break
