# RealTimeHandGestureDetection

# Table of Contents
- [Helpful Infos for a Better Workflow](#helpful-information-for-a-better-workflow)
- [Carbon Fiber Discrepancy Detection](#carbon-fiber-discrepancy-detection)
    - [Structure](#cfdd-structure)
    - [README files](#cfdd-readme-files)
- [Video Inpainting](#video-inpainting)
    - [Structure](#structure)
    - [Seperate README files](#there-are-seperate-readme-files-for-all-three-approaches)

# Aim
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

## Gesture Volume Control
In this module, user can control the device's volume using hand gesutre. Basically in this module, the program detects hand using MediaPipe library, within which, the tip of the index finger and tip of the thumb is recognised and used further for controlling the volume. The volume increases as the user elongates the length between tip of index finger and thumb, and volume decreases as the user decreases it. For details, please refer to gif provided below.

![volume control](https://github.com/SubramanyaGurumurthy/RealTimeHandgestureDetection/blob/main/gif/Volume_control.gif)

### Tools used: 
Libraries: pycaw, mediapipe, Opencv, numpy, python
IDE: VS Code

## Paint Module
In this module, user can paint on the camera screen using finger gestures. Similar to volume control module, here the program first detects the hand and the tip of the index finger and middle finger is extracted from the detected points. The painter module offer 3 different colors to chose from and an eraser options. By using both middle finger and index finger together and closing other fingers, user can switch between colors or eraser which can be found on the top of the screen. After selection, the user can paint or erase by just using index finger. By default in the beginning, pink color will be selected. For the visual demonstration [click here](https://youtu.be/u2zQ_nwl4WA)

### Tools used: 
Libraries: matplotlib, mediapipe, Opencv, numpy, python
IDE: VS Code
