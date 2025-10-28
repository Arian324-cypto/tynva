import speech_recognition as sr
from googletrans import Translator

def voice_to_text(lang='bn'):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Speak something...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language=lang)
            print("📝 You said:", text)
            return text
        except Exception as e:
            print("❌ Error:", e)
            return None

def translate_text(text, dest_lang='en'):
    translator = Translator()
    translated = translator.translate(text, dest=dest_lang)
    print(f"🌐 Translated ({dest_lang}):", translated.text)
    return translated.text

if __name__ == "__main__":
    spoken_text = voice_to_text('bn')  # 'bn' for Bangla
    if spoken_text:
        translate_text(spoken_text, 'en')
