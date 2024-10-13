# Parking-Spot-Detection-and-Counter-2
This project is a computer vision-based parking spot detection and counter. The system allows you to manually select parking spots from an image and later detect and count the number of available or occupied spots in a video feed. The project uses OpenCV, CvZone, and Pickle modules for image processing and data handling. <br/>
<br/>

## Features
* Manual Spot Selection: Select parking spots manually by clicking on an image of the parking area.
* Parking Spot Detection: Detect cars occupying the selected parking spots in a video feed.
* Real-time Parking Counter: Displays the count of available parking spots in the video feed.
* Interactive Spot Selection: Add or remove parking spots by left-clicking and right-clicking on the image. <br/>
<br/>

## Project Structure
The project is divided into two main files: <br/>
1. ParkingSpacePicker.py: This script is used to manually select and label parking spots on an image of the parking area. <br/>
  * Left-click to add a rectangular frame to define a parking spot.
  * Right-click to remove a previously added parking spot.
  * After the selection, the parking spots' positions are saved in a CarParkPos.pkl file using the Pickle module. This file serves as the parking spot map.
2. main.py: This is the main script that detects and counts the occupied parking spots from a video feed of the parking area. <br/>
  * Loads the saved parking spot positions from CarParkPos.pkl.
  * Processes the video to detect whether the parking spots are occupied or vacant.
  * Displays the parking spot status and counts available spots in real-time on the video feed.
