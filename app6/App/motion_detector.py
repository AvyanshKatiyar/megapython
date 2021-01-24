import cv2, time, pandas
from datetime import datetime




#number is used to choose input method
video=cv2.VideoCapture(0)


#check is a boolean which checks whether cam on
#frame is an object 3-d color which stores the 
#
first_first_frame=None
first_frame=None 
#declaring a var


#as we are seeing -1 and -2
status_list=[None, None]
times=[]
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
        time.sleep(2)
        #means go back to top while
        continue
   
    if first_frame is None:
        first_frame=gray
        #means go back to top while
        continue
    
    #absolute difference
    delta_frame=cv2.absdiff(first_frame, gray)
    #print(delta_frame)
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
        status=1


        (x, y, w,h)=cv2.boundingRect(contour)
        #drawing on color frome
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0),3)

    #since we only need the last two status items
    status_list=status_list[-2:]
    
    status_list.append(status)
    #
    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    elif status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())





    
    #shows the frame
    cv2.imshow("Capturing", gray)
    cv2.imshow("Delta", delta_frame)
    cv2.imshow("Thresh", thresh_frame)
    cv2.imshow("Color Frame", frame)

  
    
    key=cv2.waitKey(1)

    if key==ord("q"):
        if status==1:
            times.append(datetime.now())
        break
    print(status)
    


print(status_list)
video.release()
cv2.destroyAllWindows()



#importing to pandas

df=pandas.DataFrame(columns=["Start", "End"])

for a in range(0,len(times), 2):
    df=df.append({"Start": times[a], "End": times[a+1]}, ignore_index=True)

df.to_csv("TImes.csv")