import cv2
import numpy as np

camera=cv2.VideoCapture(0)

if (camera.isOpened())==False;:
    easygui.msgbox('please turn on your camera')

es = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,4))
kernel = np.ones((5,5),np.uint8)
background = None
flag = 0

while Ture:

    text = 'Undetected'#标注检测状态，检测到或未检测到
    grabbed, frame_lwpCV = camera.read()#从camera中拿当前帧的图像

    gray_lwpCV=cv2.cvtColor(frame_lwpCV,cv2.COLOR_BGR2GRAY)


