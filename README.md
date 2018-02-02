# Masters-Thesis-iTrace-extension

This is part of my master thesis at the Technical university of Denmark, in computerscience and engineering.

The iTrace application extension is cloned from https://github.com/SERESLab/iTrace-Archive/ .


# Project description:
iTrace is an Eclipse plugin for linking eye tracking data to source code. The capabilities of iTrace are restricted to data collection, while visualization and analysis features are missing.
Goal of this thesis is to extend the tool with an analysis and visualisation aspect allowing the user to achieve a comprehensive understanding of the coding process. 
Possible application scenarios for the tool are software engineering experiments as well as teaching environments.  

# Summary:
The goal of the thesis is to create a tool for visualizing data gathered by the gaze to source code mapping Eclipse plugin, iTrace. The solution covers the steps necessary to analyze the data collected using iTrace. Starting with updating the iTrace interface connecting to the eye tracker to use the current state of the art Tobii eye tracker software development kit. Followed by extending the data storage of iTrace to support a database setup making several iTrace sessions readily available for the analysis tools. A python library, iTraceAnalyser is created to convert the iTrace gaze data into ﬁxations while retaining the source code information. Finally the thesis propose two visualization solutions. The ﬁrst being simple data visualizations using bar plots to quickly view data for single sessions. The second being a method of creating event logs making comparison of several sessions available through existing process mining tools

A short guide for setting up the system can be found in the thesis on PDF-page 89.
