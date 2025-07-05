import cv2 as cv

video = cv.VideoCapture(0) # start video
if not video.isOpened(): # if not open
    print("Can not open camera")

while(True):
    ret, frame = video.read()
    # it returns a true/false if the frame is ready/not
    #returns value in frame

    if not ret:
        print("Can not receive frame, Exiting...")
        break

    ret = video.set(cv.CAP_PROP_FRAME_WIDTH, 600) # set the width of the frame
    ret = video.set(cv.CAP_PROP_FRAME_HEIGHT, 1000) # set the height of the frame
    frame = cv.flip(frame, 1) # flip the frame horizontally

    #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("frame", frame) # display the frame
    k = cv.waitKey(1) # wait for 1 millisecond for a key press
    # if the key pressed is 'q', then break the loop
    if k == ord('q'):
        break


video.release() # release the video capture object
cv.destroyAllWindows() # Uncomment the following lines to use the webcam for video capture
