import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

# Function to convert speech to text
def speech_to_text():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Error with Google Speech Recognition: {e}")
        return None

# Main function to demonstrate the conversion
def main():
    while True:
        choice = input("Choose '1' for Speech-to-Text or '2' for Text-to-Speech (or 'q' to quit): ")
        if choice == '1':
            speech_text = speech_to_text()
            if speech_text:
                print(f"Recognized Speech: {speech_text}")
        elif choice == '2':
            text = input("Enter the text you want to convert to speech: ")
            text_to_speech(text)
        elif choice == 'q':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
