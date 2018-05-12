# Motion Detection Using python

This repository contains an open source motion detection project which uses the internal camera for video capturing
and it detects any moving object.

### Libraries : OpenCv, Bokeh, Pandas, datetime, time etc.

## Architecture:
1. Capture the first image and use it as a background:
   <img width=700, alt="Background Frame" src="https://github.com/Anurag0212/motion_detection_using_python/blob/master/image/background.PNG">

2. Calculate the delta frame using the first background frame and current frame:
   <img width=700, alt="Delta Frame" src="https://github.com/Anurag0212/motion_detection_using_python/blob/master/image/delta_frame.PNG">

3. Calculate the threshold frame based on the color intensity of the delta frame:
  <img width=700, alt="Threshold Frame" src="https://github.com/Anurag0212/motion_detection_using_python/blob/master/image/threshold_frame.PNG">
  
4. Find the contours of the objects and highlight the object using rectangle box:
  <img width=700, alt="Highlighted Object" src="https://github.com/Anurag0212/motion_detection_using_python/blob/master/image/highlighted_object.PNG">
  
5. Record the duration for which the object was inside the frame and plot it using bokeh library:
  <img width=700, alt="Graph" src="https://github.com/Anurag0212/motion_detection_using_python/blob/master/image/motion_graph.PNG">
  
