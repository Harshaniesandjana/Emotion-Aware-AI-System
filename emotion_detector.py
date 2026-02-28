import cv2
import numpy as np

class EmotionDetector:
    def __init__(self):
        haar_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        self.face_cascade = cv2.CascadeClassifier(haar_path)

    def _classify_emotion(self, gray_face):
        mean = np.mean(gray_face)
        std = np.std(gray_face)

        if mean > 150 and std > 40:
            return "happy"
        elif mean < 80 and std < 30:
            return "sad"
        elif std > 60:
            return "surprise"
        elif mean < 90 and std > 40:
            return "angry"
        else:
            return "neutral"

    def detect_emotion(self, image_bgr):
        gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

        if len(faces) == 0:
            return None, image_bgr

        x, y, w, h = faces[0]
        face = gray[y:y+h, x:x+w]

        emotion = self._classify_emotion(face)

        cv2.rectangle(image_bgr, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(
            image_bgr,
            emotion,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 0),
            2,
        )

        return emotion, image_bgr
