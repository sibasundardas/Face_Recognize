# Face_Recognize

A simple face recognition system using real-time images from your mobile device. This project enables you to collect face data, train a recognition model, and perform real-time face recognition using a webcam stream.

## Features

- Collect face data using your mobile phone's camera
- Train a face recognition model
- Real-time face detection and recognition

## Prerequisites

- Python 3.x installed
- Required Python packages (see [Installation](#installation))
- An Android phone with the [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam) app installed

## Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/sibasundardas/Face_Recognize.git
    cd Face_Recognize
    ```

2. **Install Python dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### 1. Install IP Webcam App

- Download and install [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam) on your Android phone.
- Open the app and start the server.
- Take note of the IP address and port displayed (e.g., `http://192.168.1.5:8080`).

### 2. Collect Face Data

- **Create a folder named `images` in the project directory.**
    ```bash
    mkdir images
    ```
- Run the data collection script and **enter the IP address shown in the app** when prompted:
    ```bash
    python collect_data.py
    ```
- Follow the instructions in the terminal to collect face images using your phone's camera stream.

### 3. Consolidate Data

- **Create a folder named `data` in the project directory.**
    ```bash
    mkdir data
    ```
- Run the consolidation script:
    ```bash
    python consolidated_data.py
    ```
- This script processes and structures the collected images for training.

### 4. Train the Model / Face Detection

- Run the face detection and training script:
    ```bash
    python face_detection.py
    ```
- Wait until the model training completes.

### 5. Real-Time Face Recognition

- Run the recognition script to see live output:
    ```bash
    python recognize.py
    ```
- The system will display real-time video with recognized faces.

## File Overview

- `collect_data.py` — Collect images from your mobile webcam
- `consolidated_data.py` — Organize and preprocess images for training
- `face_detection.py` — Train the face recognition model
- `recognize.py` — Run real-time face recognition

## Notes

- Ensure your phone and PC are on the same Wi-Fi network for IP Webcam streaming.
- You may need to install additional packages (e.g., OpenCV, NumPy). Check `requirements.txt`.

## License

This project is licensed under the MIT License.

---

**Author:** [sibasundardas](https://github.com/sibasundardas)  
**LinkedIn:** [siba-sundar-das](https://www.linkedin.com/in/siba-sundar-das)
