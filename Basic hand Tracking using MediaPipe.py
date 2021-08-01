#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install mediapipe')


# In[2]:


import mediapipe as mp
import cv2
import time


# In[6]:


import mediapipe as mp
import cv2
import time
cap=cv2.VideoCapture(0)
mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpdraw=mp.solutions.drawing_utils
while True:
    _,frame=cap.read()
    imgRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for handLms in  results.multi_hand_landmarks:
            mpdraw.draw_landmarks(frame,handLms,mpHands.HAND_CONNECTIONS)
            for ide,lm in enumerate(handLms.landmark):
                h,w,c=frame.shape
                cx,cy =int(lm.x*w),int(lm.y*h)
                print(ide)
                if ide ==8:
                    
                    cv2.circle(frame,(cx,cy),5,(0,0,0),cv2.FILLED)
            
    cv2.imshow("window",frame)
    if cv2.waitKey(1)==27 :
        old_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cap.release()
        cv2.destroyAllWindows()
        break


# In[ ]:





# In[ ]:




