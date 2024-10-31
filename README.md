**AUTOMATED VIDEO SEGMENTATION**
A Flask-based web application that allows users to upload a video and segments it into scenes based on structural similarity between frames. This tool is useful for video editing workflows, where automated scene detection can save significant time.

**Features**
**Video Upload**: Users can upload a video file through the web interface.
**Scene Detection:** The app uses OpenCV and structural similarity metrics to automatically segment the video into scenes.
**Scene Download:** After processing, each scene is made available for download as a separate video file.
**
Clone the repository:**
git clone https://github.com/yourusername/cinecopilot-video-segmentation.git
cd cinecopilot-video-segmentation

Set up a virtual environment (recommended):


python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the required dependencies:

pip install -r requirements.txt
Create necessary directories:

Ensure that uploads and output folders exist in the project root:

mkdir uploads output
Usage
Run the application:

bash
Copy code
python main.py
Access the web interface: by the link generated
**
Upload a video:**

On the main page, select a video file (must be in a compatible format such as .mp4).
Click on the "Upload" button to start processing.
Download segmented scenes:

Once the video is processed, download links for each segmented scene will appear.
Click on each link to download the scenes as separate video files.
Project Structure
bash
Copy code
cinecopilot-video-segmentation/
├── uploads/                     # Directory for uploaded videos
├── output/                      # Directory for processed video scenes
├── template/
│   └── index1.html              # HTML template for the web interface
├── main.py                      # Main application file
├── requirements.txt             # Python dependencies
└── README.md                    # Project README file
Configuration
Template Path: Ensure that the template folder contains the HTML template (index1.html). By default, Flask looks for templates in the template folder.
Folders:
uploads: Stores uploaded video files temporarily.
output: Stores the segmented scene files after processing.
Dependencies
This project uses the following Python libraries:

Flask: For building the web application and routing.
OpenCV (cv2): For video processing and frame manipulation.
scikit-image (compare_ssim): For calculating structural similarity between frames to detect scene changes.
NumPy: For numerical operations on video frames.

