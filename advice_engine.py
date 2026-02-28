class AdviceEngine:
    def __init__(self):
        self.advices = {
            "happy": "You seem happy. Use this positive energy to tackle something meaningful or challenging right now.",
            "sad": "You seem a bit down. Take a short break, stretch, and focus on one small achievable task to regain momentum.",
            "angry": "You seem frustrated. Pause for 60 seconds, breathe slowly, and respond instead of reacting.",
            "fear": "You seem anxious. Break the problem into smaller steps and focus only on the next controllable action.",
            "surprise": "You seem surprised. Take a moment to process what happened and decide your next thoughtful move.",
            "neutral": "You seem calm and steady. This is a great state for focused, deep work." 
        }

    def get_advice(self, emotion):
        if emotion is None:
            return "Ik kan geen gezicht detecteren."
        return self.advices.get(emotion, "Zorg goed voor jezelf.")
