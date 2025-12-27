import cv2
import numpy as np

#read an image
flag=False
ix= -1
iy= -1
def draw(event, x, y, flags, param):
    global ix,iy,flag
    if event == 1:
        flag=True
        ix=x
        iy=y

    elif event == 0:
        if flag == True:
            cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(0,255,0),thickness=-1)

    elif event == 4:
        flag=False
        cv2.rectangle(img,pt1=(x,y),pt2=(x,y),color=(0,255,0),thickness=2)

cv2.namedWindow(winname='img')
#cv2.setMouseCallback(windowname, function)
cv2.setMouseCallback('img', draw)
img= np.zeros((512,512,3))
while True:
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        #to exit from infinite loop press x on KB
        break
cv2.destroyAllWindows()
