import cv2 as cv

video = cv.VideoCapture(0) # or it takes a video file path as an argument

if not video.isOpened():
    print("Can not open camera")

while(True):
    ret, frame = video.read()
    # it returns a true/false if the frame is ready/not
    #returns value in frame

    if not ret:
        print("Can not receive frame, Exiting...")
        break

    frame_resize = cv.resize(frame, (1000, 600))
    frame_resize = cv.flip(frame_resize, 1)

    cv.imshow("frame", frame_resize) 
    k = cv.waitKey(1)
    if k == ord('q'):
        break


video.release() 
cv.destroyAllWindows()
