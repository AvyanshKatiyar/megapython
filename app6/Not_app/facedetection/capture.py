import cv2, time

#number is used to choose input method
video=cv2.VideoCapture(0)


#check is a boolean which checks whether cam on
#frame is an object 3-d color which stores the 
#

a=1
while True:
    #reads on frame
    a=a+1
    check, frame= video.read()

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    # script will wait for 3s before video release
    #time.sleep(3)
    
    #shows the frame
    cv2.imshow("Capturing", gray)


    #first line for triggering code after key press
    
    #basically get the frame then gray it
    #then 
    key=cv2.waitKey(1000)

    #ord q is the unicode of q and waitKey 
    # basically stores value of key pressed
    if key==ord("q"):
        break

print(a)
video.release()
cv2.destroyAllWindows()