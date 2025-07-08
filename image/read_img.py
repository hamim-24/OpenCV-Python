
import cv2 as cv 
import sys 

img = cv.imread(cv.samples.findFile("image/abc.png")) # Read the image from the file system
# cv.samples.findFile is used to find the file in the sample data directory

if img is None: 
    sys.exit("Could not read the image.")
    
img = cv.resize(img, (512, 512))
img = cv.flip(img, 1)
cv.imshow("Display window", img)

k = cv.waitKey(0) 

if k == ord("s"):
    cv.imwrite("abc.jpg", img) 
    print("Image saved as abc.jpg") 

elif k == ord("q"):
    sys.exit("Exiting...")

else:
    print("Press 's' to save the image or 'q' to exit.")
    
cv.destroyAllWindows() 