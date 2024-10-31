**AUTOMATED VIDEO SEGMENTATION**

A Flask-based web application that allows users to upload a video and segments it into scenes based on structural similarity between frames with the help of Structural Similarity Index(SSI) . This tool is useful for video editing workflows, where automated scene detection can save significant time.



![image](https://github.com/user-attachments/assets/3a90c302-5114-4a86-9099-0d0002a215bc)


**Features**

**Video Upload**: Users can upload a video file through the web interface.

**Scene Detection:** The app uses OpenCV and structural similarity metrics to automatically segment the video into scenes.

**Scene Download:** After processing, each scene is made available for download as a separate video file.

**Upload a video:**

On the main page, select a video file (must be in a compatible format such as .mp4).
Click on the "Upload" button to start processing.
![image](https://github.com/user-attachments/assets/6759853a-afc1-48e1-9552-ec5e49732505)

**Download segmented scenes:**

Once the video is processed, download links for each segmented scene will appear.
Click on each link to download the scenes as separate video files.
![image](https://github.com/user-attachments/assets/90d334ea-aa01-41c1-810c-62b60ed7cceb)

**Configuration**
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

