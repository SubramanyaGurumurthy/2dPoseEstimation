# Gesture_Volume_Control

In this module, user can control the device's volume using hand gesutre. The program detects hand using MediaPipe library, within which, the tip of the index finger and tip of the thumb is recognised and used further for controlling the volume. The volume increases as the user elongates the length between tip of index finger and thumb, and volume decreases as the user decreases it. 

## Methodology

* The [HandTrackingModule.py](https://github.com/SubramanyaGurumurthy/RealTimeHandgestureDetection/blob/main/Gesture_Volume_Control/HandTrackingModule.py) uses the [mediapipe hand module](https://google.github.io/mediapipe/solutions/hands#python-solution-api) to detect the hand. The HandTrackingModule's [*findPosition()*](https://github.com/SubramanyaGurumurthy/RealTimeHandgestureDetection/blob/main/Gesture_Volume_Control/HandTrackingModule.py#:~:text=def-,findPosition,-(self%2C)) function detects 21 different points and returns the position of the detected points in the form of a list. 
* The [pycaw library](https://pypi.org/project/pycaw/#:~:text=from%20ctypes%20import%20cast,20.0%2C%20None) provides necessary control over the volume drivers of the computer. Initially the volume range is detected using the function [*GetVolumeRange()*](https://github.com/SubramanyaGurumurthy/RealTimeHandgestureDetection/blob/main/Gesture_Volume_Control/volumeHandControl.py#:~:text=%3D%20volume.-,GetVolumeRange,-()). The function [*GetMasterVolume()*](https://github.com/SubramanyaGurumurthy/RealTimeHandgestureDetection/blob/main/Gesture_Volume_Control/volumeHandControl.py#:~:text=(volume.-,GetMasterVolumeLevel,-())%2C%20%5BminVol%2C) returns the current volume level of the system and the function [*SetMasterVoume()*](https://github.com/SubramanyaGurumurthy/RealTimeHandgestureDetection/blob/main/Gesture_Volume_Control/volumeHandControl.py#:~:text=SetMasterVolumeLevel) sets the value to the user input level, provided the input values lies within the range of system volume level.
* From the 21 detected points detected in the hand, the tip of index finger and the thumb is taken into consideration. The index value for index finger is 8 and that of the thumb is 4. 
* Using the position of these two fingers, at every subsequent frames from the camera input, the distance is calculated. 
* The distance value shall be inputed into [*SetMasterVoume()*](https://github.com/SubramanyaGurumurthy/RealTimeHandgestureDetection/blob/main/Gesture_Volume_Control/volumeHandControl.py#:~:text=SetMasterVolumeLevel).
* Please refer to the gif below for live demo

![volume control](https://github.com/SubramanyaGurumurthy/RealTimeHandgestureDetection/blob/main/gif/Volume_control.gif)
