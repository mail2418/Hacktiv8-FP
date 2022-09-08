import pyttsx3

engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def bicara(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    bicara("Hello, How are you today?")