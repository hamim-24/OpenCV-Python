
import cv2 as cv # OpenCV library for image processing
import sys # System library for system-specific parameters and functions

img = cv.imread(cv.samples.findFile("abc.png")) # Read the image from the file system
# cv.samples.findFile is used to find the file in the sample data directory

if img is None: # Check if the image was read successfully
    sys.exit("Could not read the image.") # Exit if the image is not found
img = cv.resize(img, (500, 500)) # Resize the image to 500x500 pixels
img = cv.flip(img, 1) # Flip the image horizontally
cv.imshow("Display window", img) # Display the image in a window

# The window will automatically adjust to the size of the image
k = cv.waitKey(0) # Wait for a key press indefinitely

if k == ord("s"):
    cv.imwrite("abc.jpg", img) # Save the image if 's' is pressed
    print("Image saved as abc.jpg") # Print confirmation message

elif k == ord("q"):
    sys.exit("Exiting...")
# Exit if 'q' is pressed
else:
    print("Press 's' to save the image or 'q' to exit.")
    
cv.destroyAllWindows() # Close all OpenCV windows