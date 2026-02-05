# 🚦 Traffic Monitoring & Speed Estimation System (YOLOv8)

A real-time traffic analytics system that detects, tracks, and estimates vehicle speed from road videos using YOLOv8, DeepSORT, and perspective mapping.

## 🔧 Tech Stack
- Python
- YOLOv8 (Ultralytics)
- DeepSORT
- OpenCV
- NumPy
- Git LFS

## 📌 Features
- Multi-vehicle detection (Car, Bus, Truck, Bike)
- ID-based tracking
- Pixel to real-world mapping
- Speed estimation in km/h
- Overspeed detection
- Vehicle counting

## 🧠 Pipeline

Video → YOLOv8 → DeepSORT → Perspective Mapping → Speed Estimation → Analytics


## 📂 Project Structure

traffic_system/
├── detector.py
├── tracker_module.py
├── mapper.py
├── speed_behavior.py
├── analytics.py
├── main.py
├── highway.mp4
├── yolov8n.pt
├── requirements.txt
├── README.md
├── .gitignore
└── .gitattributes



## ▶️ How to Run
```bash
pip install -r requirements.txt
python main.py



# Traffic Monitoring & Speed Estimation System (YOLOv8)

A real-time traffic surveillance and analytics system that detects, tracks, and estimates the speed of vehicles from road videos using **YOLOv8**, **DeepSORT**, and **computer vision–based perspective mapping**.

This project demonstrates an end-to-end **Intelligent Transportation System (ITS)** pipeline suitable for smart city applications, traffic analysis, and research prototypes.

---

## Overview

The system processes a traffic video stream to:
- Detect multiple vehicle classes
- Assign consistent IDs across frames
- Convert pixel coordinates to real-world space
- Estimate vehicle speed in km/h
- Identify overspeeding vehicles
- Maintain unique vehicle counts

---

## Technology Stack

- **Python**
- **YOLOv8 (Ultralytics)** – Real-time object detection
- **DeepSORT** – Multi-object tracking with ID consistency
- **OpenCV** – Video processing and visualization
- **NumPy** – Numerical computation
- **Git LFS** – Large file management (video & model weights)

---

## Key Features

- Multi-vehicle detection (Car, Bus, Truck, Motorcycle)
- Robust ID-based tracking across frames
- Perspective (homography) mapping for real-world measurement
- Speed estimation in km/h
- Overspeed event detection
- Unique vehicle counting
- Modular and extensible code structure

---

## Processing Pipeline



