# Masters-Thesis-iTrace-extension

This is part of my master thesis at the Technical university of Denmark, in computerscience and engineering.

The iTrace application extension is cloned from https://github.com/SERESLab/iTrace-Archive/ .


Project description is the following:
iTrace is an Eclipse plugin for linking eye tracking data to source code. The capabilities of iTrace are restricted to data collection, while visualization and analysis features are missing.
Goal of this thesis is to extend the tool with an analysis and visualisation aspect allowing the user to achieve a comprehensive understanding of the coding process. 
Possible application scenarios for the tool are software engineering experiments as well as teaching environments.  

Goals to achieve in the project are:

- Update the JNI to use the newest tobii SDK.
  - Added C support to SDK headers.
  
  TRACKING:
  - MainLoop (legacy name) starts the background thread and initialise the data used by the eytracker.
  - connectTobiiTracker, finds the eyetracker and applies the license. License is currently hard coded.
  - StartTracking, subscribes to eyetracker and uses callback function and HandleGazeData to pass gazes to java application.
  - StopTracking unsubscribes from eyetracker and deletes the current eyetracking data.
  CALIBRATION:
  - AddPoint, used to gather information about where someone is looking, compared to a specific point. Used whenever a focus point is recorded.
  - StartCalibration, puts the eyetracker in calibration mode.
  - StopCalibration, leaves calibration mode, and computes and applies the calibration to the eyetracker.
  - GetCalibration, return the results of the calibration, used to show how accurate the calibration was.
  
- Add database support for iTrace

- Visualise data gathered during an iTrace session.

Potential further work if time allow it.
- Examine possibilities for supporting writing in iTrace.
