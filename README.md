# RealTimeHandGestureDetection

## Gesture Volume Control
In this module, user can control the device's volume using hand gesutre. Basically in this module, the program detects hand using MediaPipe library, within which, the tip of the index finger and tip of the thumb is recognised and used further for controlling the volume. The volume increases as the user elongates the length between tip of index finger and thumb, and volume decreases as the user decreases it.

![volume control](https://github.com/SubramanyaGurumurthy/RealTimeHandgestureDetection/blob/main/gif/Volume_control.gif)

###Tools used: 
Libraries: pycaw, mediapipe, Opencv, numpy, python
IDE: VS Code

## Paint Module
In this module, user can paint on the camera screen using finger gestures. Similar to volume control module, here the program first detects the hand and the tip of the index finger and middle finger is extracted from the detected points. The painter module offer 3 different colors to chose from and an eraser options. By using both middle finger and index finger together and closing other fingers, user can switch between colors or eraser which can be found on the top of the screen. After selection, the user can paint or erase by just using index finger. By default in the beginning, pink color will be selected. For the visual demonstration [click here](https://youtu.be/u2zQ_nwl4WA)

###Tools used: 
Libraries: matplotlib, mediapipe, Opencv, numpy, python
IDE: VS Code
