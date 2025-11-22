from ultralytics import YOLO
import streamlit as st
import time
import numpy as np
import tempfile


model = YOLO("yolov8n.pt")

video_path = 'videos'
os.makedirs(video_path, exist_ok=True)

cap = cv2.VideoCapture(0)


