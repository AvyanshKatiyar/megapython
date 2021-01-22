import cv2

#reading
#number pass one 
#1 means as it is
#0 means grayscale
#-1 image will have transparency
img= cv2.imread("galaxy.jpg", 0 )

# img is a numpy array
#img.shape gives dsimensions
#img.ndim gives number of dimensions



#resizing the image
resized_image = cv2.resize(img,(int(img.shape[1]/2 ),int(img.shape[0]/2)))



cv2.imshow("Galaxy", resized_image)

cv2.imwrite("Galaxy_resized.jpg", resized_image)

#decides what time before window closes
#0 means image will stay and press any key to close
#rest 2000 means 2 secinds
cv2.waitKey(30000)



cv2.destroyAllWindows()