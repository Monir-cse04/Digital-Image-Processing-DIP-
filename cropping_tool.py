import cv2
import numpy as np
flag= False
ix=-1
iy=-1
def crop(event, x, y, flags, param):
    global ix,iy,flag
    if event == 1:
        flag = True
        ix=x
        iy=y
        
    # elif event == 0:
    #     if flag == True:
    #         cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(0,0,0),thickness=1)

    elif event==4:
        fx=x
        fy=y
        flag = False
        cv2.rectangle(img, pt1=(ix,iy), pt2=(x, y), color=(0,0,0), thickness=1)
        cropped = img[ix:fx, iy:fy] #cropping portion
        cv2.imshow('crop_img', cropped) #crop pic will show  in new window name crop_img

        #if want to save this cropped picture then use  the followg function
        # cv2.imwrite('cropped_img.jpg', cropped) 
        
        cv2.waitKey(0) #delay
        
cv2.namedWindow(winname='img')
cv2.setMouseCallback("img",crop)
img=cv2.imread("jasmine.png")
while True:
    cv2.imshow("img",img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cv2.destroyAllWindows()

