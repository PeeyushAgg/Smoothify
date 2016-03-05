import cv2
import numpy as np
from time import sleep
flag=False	
change=2
r = 20
g = 20
bl = 20
cap=cv2.VideoCapture(0)

l,b,n=cap.read()[1].shape
temp1=np.zeros((l,b,n),dtype=np.int)

while(True):
	#pick BGR values
	ret,frame=cap.read()
	
	if(r==250 and g==250 and bl==250):
		flag=True
	
	if(r==10 and g==10 and bl==10):
		flag=False
	print temp1[2][2], flag	
	temp1[:]=[bl,g,r]
	sleep(0.001)
	if ( (r >= 10 & r<=250) & (g >= 10 & g<=250) & (bl >= 10 & bl<=250) ):
		
		if(not flag):
			if(r<250):
				r=r+change
			elif(bl<250):
				bl=bl+change
			elif (g<250):
				g=g+change
			
		elif (flag):
			if(r>10):
				r=r-change
			elif (g>10):
				g=g-change
			elif(bl>10):
				bl=bl-change
	else:
		if(r>250):
			r=250
		if(g>250):
			g=250
		if(bl>250):
			bl=250
		if(r<10):
			r=10
		if(g<10):
			g=10
		if(bl<10):
			bl=10
		flag=not(flag)
	f1=np.multiply(frame,temp1)
	cv2.imshow('Original',f1)
	if (cv2.waitKey(1) & 0xFF) == 27:
		break

cv2.destroyAllWindows()