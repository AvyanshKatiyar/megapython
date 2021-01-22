import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("news.jpg")
#using grayscale increases accuracy

gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#after each search 
#decreasign scale for search i.e image scaled down
#so bigger faces searched
#how many neighbours to search around the window
faces=face_cascade.detectMultiScale(gray_img,
scaleFactor=1.05,
minNeighbors=5)
print(faces)

#x,y gives top left corner of the face
#w and h are width and heights 
for x, y, w, h in faces:
    img=cv2.rectangle(img, (x,y),(x+w, y+h), (0, 255, 0), 3) 
    #(x,y) is the starting point

    
resized=cv2.resize(img, (int(img.shape[1]/3),int(img.shape[0]/3)))


cv2.imshow("Gray", resized)
cv2.waitKey(0)
cv2.destroyAllWindows

#https://stackoverflow.com/questions/20801015/recommended-values-for-opencv-detectmultiscale-parameters/20805153