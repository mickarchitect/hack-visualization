# hack-visualization repository

## Why - USA Facts Hackathon - Visualization Challenge

## Short version
- [The App](https://share.streamlit.io/mickarchitect/hack-visualization/main/epa_vis_app_v3.py)
- The App is a very rough draft but is essentially all I could complete by the end of the hackathon.

## Longer version
- [USA Facts.org]() offered a Data Challenge and a Visualization Challenge [link]().
- I was very interested:
  - I like the mission of USA Facts.
  - I needed to measure what I could do at this point in various learning curves that I am on.
  - Creating an Environmental Data Visualization sounded fun.
- I participated in the Data Challenge - see mickarchitect/hack-legislative-classifier.
  - But part of what I worked on were EPA Sources and I liked the TRI data.
- So for the visualization challenge, I tried to visualize the Toxics Release Inventory data.

## Contents of this folder
### Streamlit apps
- epa_vis_app_v3.py - this is the current active app, all others were partial or experimenting with a feature/etc.
- epa_vis_app.py, epa2.py, sankey_try1.py, sankey_try2.py, test_streamlit.py, tooltip_try1.py, tooltip_try2.py - can all be ignored.
### Notebooks
- NPDES_DataAcqAndEng - this is where I Discovered and Analyzed data.  It is also where I produce the final .CSV's for the app.
- VisualizationNotes - this is where I tried various visualization techniques.
### Data in main folder
- Outlier_Environmental_Hackathon_2021.xlsx - this is the output of the Data Challenge.
  - The EPA Strategic Goals tab has all of the research I did during the Data Challenge and the initial links for data for the Viz Challenge.
- requirements.txt - a python/pip list of libraries used.  Streamlit uses this file to build the environment for your app to run in.
### Data folder
- AnalyzeReleasesComplete.xlsx - a sample CSV brought into Excel with column widths and numeric formats set, etc.
- Final data was too large to upload
