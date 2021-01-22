import cv2, time, pandas

#number is used to choose input method
video=cv2.VideoCapture(0)


#check is a boolean which checks whether cam on
#frame is an object 3-d color which stores the 
#
first_first_frame=None
first_frame=None 
#declaring a var

while True:
    #reads on frame

    check, frame= video.read()
    status=0

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #smooths tupple contains blur 
    # last is standard deviation
    gray=cv2.GaussianBlur(gray,(21,21), 0)
    #init
    if first_first_frame is None:
        first_first_frame=gray
        time.sleep(5)
        #means go back to top while
        continue
   
    if first_frame is None:
        first_frame=gray
        #means go back to top while
        continue
    
    status=1
    #absolute difference
    delta_frame=cv2.absdiff(first_frame, gray)
    print(delta_frame)
    #if above 30 then convert to 255
    thresh_frame=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    
    #image smoothening
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=3)
    
    #finding contours and checking area
    #stored in cnts
    (cnts,_)=cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in cnts:
        if cv2.contourArea(contour)<10000:
            continue

        (x, y, w,h)=cv2.boundingRect(contour)
        #drawing on color frome
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0),3)

    


    
    #shows the frame
    cv2.imshow("Capturing", gray)
    cv2.imshow("Delta", delta_frame)
    cv2.imshow("Thresh", thresh_frame)
    cv2.imshow("Color Frame", frame)

  
    
    key=cv2.waitKey(1)

    if key==ord("q"):
        break
    #print(status)

video.release()
cv2.destroyAllWindows()

