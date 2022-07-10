# RealTimeHandGestureDetection

Realtime Detection of different points in the body is an important task in computer vision as the detected results can be further used for understanding and to analyze person's position, and the task that the person is performing. It can be also used for different purposes like contactless mouse usage, or much more, which eventually makes the system much more user-friendly and smart. In this work, I tried to come up with such a solution, a real-time body point detection using the camera. The proposed approach uses the raw pixel values of the captured image to detect different points on the human body. I further use these points for different sub-tasks such as Gesture Volume Control, Paint App using fingers, and angle detection between joints.

# Dependencies
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

# Further details about the sub modules
* [Gesture Volume Control](https://github.com/SubramanyaGurumurthy/RealTimeHandgestureDetection/blob/main/Gesture_Volume_Control/README.md)
* [Pain Module](https://github.com/SubramanyaGurumurthy/RealTimeHandgestureDetection/blob/main/Paint_Module/README.md)

# Results
## Gesture_Volume_Control
![volume control](https://github.com/SubramanyaGurumurthy/RealTimeHandgestureDetection/blob/main/gif/Volume_control.gif)

## Paint_Module
[Link for the live demonstration video](https://youtu.be/u2zQ_nwl4WA)
