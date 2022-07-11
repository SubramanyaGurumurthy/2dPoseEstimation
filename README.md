# RealTimeHandTracking

Realtime pose detection of the human body is an important task in computer vision as the detected results can be further used for understanding and to analyze person's position, and the task that the person is performing. In this work I have used the [Mediapipe library](https://google.github.io/mediapipe/solutions/hands) by google for the detection and tracking of key points. The proposed application uses the raw pixel values of the captured image to detect different key points on the human body. I further use these key points for different sub-tasks such as Gesture Volume Control, Paint App using fingers.

## Dependencies
The listed details are the packages and versions which was used while developing this project and also recommended for using it.
* [python - 3.9.13 ](https://www.python.org/downloads/release/python-3913/)
* [mediapipe - 0.8.10.1](https://pypi.org/project/mediapipe/)
* [opencv - 4.5.5](https://opencv.org/opencv-4-5-5/)
* [matplotlib - 3.4.3](https://matplotlib.org/3.4.3/contents.html)
* [numpy -1.21.2](https://numpy.org/doc/stable/release/1.21.2-notes.html)
* [ctypes - 1.1](https://pypi.org/project/ctypes/)
* [pycaw](https://pypi.org/project/pycaw/)

## Folder Structure:
    .
    ├── ...
    ├── RealtimeHandgestureDetection
    │   |── Gesture_Volume_Control   
    |   |   ├── HandTrackingModule.py
    |   |   ├── VoulemeHandControl.py
    |   |── Human_Pose2d
    |   |   |── 1.mp4
    |   |   |── PoseEstimationMin.py
    |   |   |── Test,py
    │   |── Paint_Module
    |   |   |── HandTrackingModule.py
    |   |   |── VirtualPainter.py
    |   |── gif
    |   |   |── VoulmeControl.gif
    |   |   |── Painting.mp4
    |   └── Personal_trainer
    |       |──PoseModule.py
    |       └── TrainerProject.py
    └── ...

## Further details about the sub modules
### * Gesture Volume Control
In this module, user can control the device's volume using hand gesutre. The program detects hand using MediaPipe library, within which, the tip of the index finger and tip of the thumb is recognised and used further for controlling the volume. The volume increases as the user elongates the length between tip of index finger and thumb, and volume decreases as the user decreases it. 

#### Methodology

* The [HandTrackingModule.py](https://github.com/SubramanyaGurumurthy/RealTimeHandgestureDetection/blob/main/Gesture_Volume_Control/HandTrackingModule.py) uses the [mediapipe hand module](https://google.github.io/mediapipe/solutions/hands#python-solution-api) to detect the hand. The HandTrackingModule's [*findPosition()*](https://github.com/SubramanyaGurumurthy/RealTimeHandgestureDetection/blob/main/Gesture_Volume_Control/HandTrackingModule.py#:~:text=def-,findPosition,-(self%2C)) function detects 21 different points and returns the position of the detected points in the form of a list. 
* The [pycaw library](https://pypi.org/project/pycaw/#:~:text=from%20ctypes%20import%20cast,20.0%2C%20None) provides necessary control over the volume drivers of the computer. Initially the volume range is detected using the function [*GetVolumeRange()*](https://github.com/SubramanyaGurumurthy/RealTimeHandgestureDetection/blob/main/Gesture_Volume_Control/volumeHandControl.py#:~:text=%3D%20volume.-,GetVolumeRange,-()). The function [*GetMasterVolume()*](https://github.com/SubramanyaGurumurthy/RealTimeHandgestureDetection/blob/main/Gesture_Volume_Control/volumeHandControl.py#:~:text=(volume.-,GetMasterVolumeLevel,-())%2C%20%5BminVol%2C) returns the current volume level of the system and the function [*SetMasterVoume()*](https://github.com/SubramanyaGurumurthy/RealTimeHandgestureDetection/blob/main/Gesture_Volume_Control/volumeHandControl.py#:~:text=SetMasterVolumeLevel) sets the value to the user input level, provided the input values lies within the range of system volume level.
* From the 21 detected points detected in the hand, the tip of index finger and the thumb is taken into consideration. The index value for index finger is 8 and that of the thumb is 4. 
* Using the position of these two fingers, at every subsequent frames from the camera input, the distance is calculated. 
* The distance value shall be inputed into [*SetMasterVoume()*](https://github.com/SubramanyaGurumurthy/RealTimeHandgestureDetection/blob/main/Gesture_Volume_Control/volumeHandControl.py#:~:text=SetMasterVolumeLevel).
* Please refer to the gif below for live demo

![volume control](https://github.com/SubramanyaGurumurthy/RealTimeHandgestureDetection/blob/main/gif/Volume_control.gif)


### * Paint Module
In this module, user can paint on the camera screen using finger gestures. Similar to [Gesture_Volume_control](https://github.com/SubramanyaGurumurthy/RealTimeHandgestureDetection/tree/main/Gesture_Volume_Control) module, here the program initially detects the hand and within which the index finger and thumb tip positions are extracted. Using the extracted details, the user's gesture is painted on the screen. The painter module offer 3 different colors to chose from and an eraser options. By using both middle finger and index finger together and closing other fingers, user can switch between colors or eraser which can be found on the top of the screen. After selection, the user can paint or erase by just using just index finger. By default in the beginning, pink color will be selected. For the visual demonstration please refer to the gif provided below.

#### Methodology
* The [HandTrackingModule.py](https://github.com/SubramanyaGurumurthy/RealTimeHandgestureDetection/blob/main/Paint_Module/HandTrackingModule.py) helps to detect the hand and 21 different points on the hand. The function [*findPosition()*](https://github.com/SubramanyaGurumurthy/RealTimeHandgestureDetection/blob/main/Paint_Module/HandTrackingModule.py#:~:text=def-,findPosition,-(self%2C)) returns 21 different point locations as a list from the given input image frame. 
* Using the list, the index finger tip at 8th index position and middle finger tip at index 12 in the list is seperated.
* The function [*fingersUp()*](https://github.com/SubramanyaGurumurthy/RealTimeHandgestureDetection/blob/main/Paint_Module/virtualPainter.py#:~:text=fingers%20%3D%20detector.fingersUp()) checks if the middle finger is held up straight along with index finger or it is folded. 
* If the middle finger is folded, the drawing mode is activated, else if middle finger is held up, selection mode is activated.
* In selection mode, by moving middle and index finger into the corresponding icon at the top of the screen, user can select between colors and eraser.
* In drawing mode, user can move the index finger around to draw.
* All the drawings shall be performed on a image of numpy zeroes which has equal resolution as the camera image, and later both the images are processed and added using [*cv2.addWeighted()*](https://github.com/SubramanyaGurumurthy/RealTimeHandgestureDetection/blob/main/Paint_Module/virtualPainter.py#:~:text=img%20%3D%20cv2.addWeighted(img%2C%200.5%2C%20imgCanvas%2C%200.5%2C%200)) to achieve the live video painting.  

![Paint_Module](https://github.com/SubramanyaGurumurthy/RealTimeHandgestureDetection/blob/main/gif/ezgif.com-gif-maker.gif)
