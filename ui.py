import streamlit as st
import cv2
import numpy as np
from emotion_detector import EmotionDetector
from advice_engine import AdviceEngine

st.title("Emotion Aware AI System")

detector = EmotionDetector()
advisor = AdviceEngine()

img = st.camera_input("Maak een foto")

if img:
    bytes_data = img.getvalue()
    nparr = np.frombuffer(bytes_data, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    image = cv2.flip(image, 1)

    emotion, annotated = detector.detect_emotion(image)
    annotated_rgb = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)

    st.image(annotated_rgb, caption="Detectie")

    st.subheader(f"Emotie: {emotion}")
    st.write(advisor.get_advice(emotion))
