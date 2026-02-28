import cv2
from camera import Camera
from emotion_detector import EmotionDetector
from advice_engine import AdviceEngine

def main():
    cam = Camera()
    detector = EmotionDetector()
    advisor = AdviceEngine()

    while True:
        frame = cam.read()
        if frame is None:
            break

        emotion, annotated = detector.detect_emotion(frame)
        advice = advisor.get_advice(emotion)

        cv2.putText(
            annotated,
            advice,
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2,
        )

        cv2.imshow("Emotion AI System", annotated)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cam.release()

if __name__ == "__main__":
    main()
