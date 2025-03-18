# Face Recognition Using DeepFace and OpenCV

## Description
This project uses OpenCV and DeepFace to perform real-time face recognition with a webcam. The script captures video, processes frames, and compares detected faces with a reference image to determine if there is a match.

## Features
- Captures real-time video using OpenCV
- Uses DeepFace to compare the live video frames with a reference image
- Displays "MATCH!" or "NO MATCH!" on the video feed
- Uses threading for efficient face recognition
- Allows exiting the application by pressing 'q'

## Requirements
Ensure you have the following installed:

- Python 3.7+
- OpenCV
- DeepFace
- TensorFlow
- NumPy

### Install Dependencies
```bash
pip install opencv-python deepface tensorflow numpy
```

## Usage
1. Place the reference image in the same directory and name it `ref.jpg`.
2. Run the script:
```bash
python face_recognition.py
```
3. Press 'q' to exit the program.

## Troubleshooting
- If you get `ModuleNotFoundError: No module named 'cv2'`, install OpenCV:
  ```bash
  pip install opencv-python
  ```
- If you get `ModuleNotFoundError: No module named 'deepface'`, install DeepFace:
  ```bash
  pip install deepface
  ```
- If DeepFace verification fails frequently, ensure the reference image is clear and well-lit.

## License
This project is licensed under the MIT License.