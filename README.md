# Motion Detection Using python

This repository contains an open source motion detection project which uses the internal camera for video capturing
and it detects any moving object.

### Libraries : OpenCv, Bokeh, Pandas, datetime, time etc.

## Architecture:
1. Capture the first image and use it as a background:

2. Calculate the delta frame using the first background frame and current frame:

3. Calculate the threshold frame based on the color intensity of the delta frame:

4. Find the contours of the objects and highlight the object using rectangle box:

5. Record the duration for which the object was inside the frame and plot it using bokeh library:
