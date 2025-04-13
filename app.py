import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user's voice and recognize speech
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-US')  # Use Google Web API
            print(f"You said: {query}")
            return query.lower()  # Convert to lowercase for easier matching
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""

# Main function to detect specific phrases and respond
def main():
    while True:
        query = listen()

        if "hey how are you" in query:
            response = "I'm just a program, so I don't have feelings, but thank you for asking!"
            print(response)
            speak(response)
            break  # Exit after responding

        elif "exit" in query:
            print("Exiting the program...")
            speak("Goodbye!")
            break  # Exit the loop

        else:
            response = "I didn't catch that. Please say 'hey how are you' or 'exit'."
            print(response)
            speak(response)

if __name__ == "__main__":
    main()