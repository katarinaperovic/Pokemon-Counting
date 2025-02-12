import numpy as np
import cv2 
import matplotlib
import matplotlib.pyplot as plt 
import os
import csv
import sys
from sklearn.metrics import mean_absolute_error

image_directory = sys.argv[1]
csv_file = "squirtle_count.csv"
matplotlib.rcParams['figure.figsize'] = 16,12
results = {}
predicted_values = []
actual_values = [] 
with open(csv_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        filename, result = row
        results[filename] = result


for filename in os.listdir(image_directory):
    img = cv2.imread(os.path.join(image_directory, filename)) 

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
    brightness = cv2.mean(img)[0]
    _, std_dev = cv2.meanStdDev(img)
    contrast = std_dev[0][0]

    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
     
    if(62<brightness<70 and 60<contrast<62):
        ret, image_bin = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY_INV) 
    elif(50<brightness<54 and 56<contrast<59):
        ret, image_bin = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY_INV)
    elif(154<brightness<158 and 63<contrast<68):
        ret, image_bin = cv2.threshold(img_gray, 240, 255, cv2.THRESH_BINARY_INV)
    else: 
        ret, image_bin = cv2.threshold(img_gray, 220, 255, cv2.THRESH_BINARY_INV) 
    

    img_crop=image_bin[50:,0:450]

    kernel=np.ones((3, 3))
    img_crop=cv2.dilate(img_crop,kernel,iterations=1)
    img_crop=cv2.erode(img_crop,kernel,iterations=7)
    #plt.imshow(img_crop,'gray')

    contours_pokemon=[]
    
    if(62<brightness<70 and 60<contrast<62):
        contours,hierarchy=cv2.findContours(img_crop,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    else:
        contours,hierarchy=cv2.findContours(img_crop,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
    
        center, size, angle = cv2.minAreaRect(contour)
        height, width = size

        if width > 8 and width < 80 and height > 8 and height < 80 : 
            contours_pokemon.append(contour)
    cv2.drawContours(img[50:,0:450],contours_pokemon,-1,(255,0,0),1)

    predicted_values.append(len(contours_pokemon))
    actual_values.append(float(results[filename]))

    print('{}-{}-{}' .format(filename,results[filename],len(contours_pokemon)))
    
    #plt.imshow(img[50:,0:450])
    #plt.show()
    
mae = mean_absolute_error(actual_values,predicted_values)    
print(mae)
