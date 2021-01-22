#resizes all images in the directory

import cv2
import glob 


all_file_names = glob.glob("sample_images/*.jpg")
print(all_file_names)

for filename in all_file_names:
    img= cv2.imread(filename, 1 )
    resized_image = cv2.resize(img,(100, 100))
    cv2.imwrite(f"{filename[:-4]}_resized.jpg", resized_image)
