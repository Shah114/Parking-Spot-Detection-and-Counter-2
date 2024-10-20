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
   * Displays the parking spot status and counts available spots in real-time on the video feed. <br/>
<br/>

## How It Works
1. Parking Spot Selection:
   * Run ParkingSpacePicker.py to manually select parking spots on an image.
   * The selected positions will be saved in a file called CarParkPos.pkl. <br/>
2. Parking Spot Detection:
   * Run main.py with a video file of the parking area.
   * The program will load the parking spot positions from the pickle file and check for cars in each spot.
   * The video output will display whether each spot is occupied and show the count of available spots. <br/>
<br/>

## Installation
1. Clone the repository:

   ```bash
   git clone https://github.com/Shah114/Parking-Spot-Detection-and-Counter-2.git
   ```

2. Install the required dependencies:

   ```bash
   pip install opencv-python cvzone pickle
   ```
<br/>

## Usage
**Parking Spot Selection (Labeling)** <br/>
1. Place an image of the parking area in the project folder.
2. Run the ParkingSpacePicker.py script to manually select parking spots.

   ```bash
   python ParkingSpacePicker.py
   ```
3. Left-click on the image to add rectangular frames for parking spots.
4. If you make a mistake, right-click to remove the frame you want.
5. Once you're done, close the window, and the parking spot positions will be saved in a file called CarParkPos.pkl. <br/>
<br/>

**Parking Spot Detection** <br/>
1. Place a video of the parking area in the project folder.
2. Run the main.py script to detect parked cars and count available spots.

   ```bash
   python main.py
   ```
3. The script will process the video and show real-time detection of occupied and available parking spots. <br/>
<br/>

## Sample
* Sample Image: The project includes a sample image for parking spot selection.
* Sample Video: A sample video is provided to demonstrate the real-time parking detection. <br/>
<br/>

## Dependencies
* Python 3.x
* OpenCV (opencv-python)
* CvZone (cvzone)
* Pickle (part of Python standard library) <br/>
<br/>

## Future Improvements
* Add support for automatic parking spot detection.
* Integrate a live camera feed for real-time detection.
* Improve detection accuracy by using a deep learning model.
<br/>

## Example
[Watch the demo video](Video/PSDC.mp4)
<br/>

![image alt](Example/example_image.png)

<br/>
