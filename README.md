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

