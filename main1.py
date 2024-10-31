from flask import Flask, request, render_template, send_from_directory, jsonify
import cv2
import os
import numpy as np
from skimage.metrics import structural_similarity as compare_ssim
from werkzeug.utils import secure_filename
import shutil

#intializing app
app = Flask(__name__, template_folder=r"C:\Users\91735\Downloads\New folder\New folder\template")

#direcorry to access files
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

#splitting frames 
def cut_video_on_transitions(input_video_path, output_folder, transition_threshold=0.4, min_scene_length=24):
    video = cv2.VideoCapture(input_video_path)
    fps = video.get(cv2.CAP_PROP_FPS)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    ret, prev_frame = video.read()
    if not ret:
        print("Failed to read the video file.")
        return []

    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    scene_number = 1
    frames_since_last_cut = 0
    output_paths = []

    scene_clip_path = os.path.join(output_folder, f"scene_{scene_number}.mp4")
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(scene_clip_path, fourcc, fps, (width, height))

    #iterating thorugh all frames and comparing it one by one
    def ssim_difference(frame1, frame2):
        (score, diff) = compare_ssim(frame1, frame2, full=True)
        return score

    for frame_number in range(1, frame_count):
        ret, curr_frame = video.read()
        if not ret:
            break

        curr_gray = cv2.cvtColor(curr_frame, cv2.COLOR_BGR2GRAY)
        ssim_score = ssim_difference(prev_gray, curr_gray)

        if ssim_score < transition_threshold and frames_since_last_cut > min_scene_length:
            out.release()
            output_paths.append(scene_clip_path)
            scene_number += 1
            scene_clip_path = os.path.join(output_folder, f"scene_{scene_number}.mp4")
            out = cv2.VideoWriter(scene_clip_path, fourcc, fps, (width, height))
            frames_since_last_cut = 0

        out.write(curr_frame)
        prev_gray = curr_gray
        frames_since_last_cut += 1

    out.release()
    video.release()
    output_paths.append(scene_clip_path)

    return output_paths

#render index.1hyml template get method
@app.route('/')
def index():
    return render_template('index1.html')

#post request
@app.route('/upload', methods=['POST'])
def upload_video():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    
    filename = secure_filename(file.filename)
    input_video_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(input_video_path)
    
    # Process the video
    output_paths = cut_video_on_transitions(input_video_path, OUTPUT_FOLDER)
    
    # Clean up the uploaded file
    os.remove(input_video_path)
    
    # Prepare download links for each scene
    download_links = [f'/download/{os.path.basename(path)}' for path in output_paths]
    
    return jsonify(download_links)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(OUTPUT_FOLDER, filename, as_attachment=True)

#run file wihtout reloading
if __name__ == '__main__':
    app.run(debug=True)
