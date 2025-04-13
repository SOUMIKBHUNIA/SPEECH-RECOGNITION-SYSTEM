COMPANY : CODTECH IT SOLUTIONS

NAME : SOUMIK BHUNIA

INTERN ID :CT6WWQB

DOMAIN : ARTIFICIAL INTELLIGENCE

DURATION : 6 WEEKS

MENTOR : NEELA SANTOH

CODE DESCRIPTION

This Python script creates a simple voice-controlled assistant using two primary libraries: speech_recognition and pyttsx3. The purpose of the program is to listen to the user's voice, recognize specific spoken commands, and respond using text-to-speech.

The script begins by importing the necessary libraries. speech_recognition is used to capture and convert spoken language into text, while pyttsx3 is used for converting text into spoken words. These libraries allow the assistant to both understand the user and speak back in a natural manner.

Next, the script initializes two key components: a speech recognizer (recognizer = sr.Recognizer()) and the text-to-speech engine (engine = pyttsx3.init()). The recognizer listens for input, while the engine handles the voice output.

Two important functions are defined: speak(text) and listen().

The speak() function takes a string input called text. It uses the pyttsx3 engine to say the text out loud. The engine.say() method queues the speech, and engine.runAndWait() ensures it is spoken immediately. This function is used every time the assistant needs to respond to the user verbally.

The listen() function is responsible for capturing and interpreting the user's voice. It uses the microphone as the audio input source. Inside a with statement, it starts listening, first adjusting for background noise using adjust_for_ambient_noise() to improve accuracy. It then captures the audio using recognizer.listen(). Once the audio is recorded, it is sent to Google's Speech Recognition API using recognizer.recognize_google() with the language set to English (US). If successful, the recognized speech is converted to lowercase and returned. This ensures that phrase matching is case-insensitive.

The function includes error handling to manage common issues. If the speech is unclear or not understood, an UnknownValueError is caught, and an empty string is returned. If there's a problem contacting the Google service, a RequestError is caught, and an appropriate message is printed.

The core logic resides in the main() function, which runs a continuous loop using while True. It calls the listen() function to capture user input and stores the result in the query variable.

The assistant responds to two specific voice commands:

If the user says “hey how are you”, the assistant responds with a friendly message: “I'm just a program, so I don't have feelings, but thank you for asking!”. It speaks this response and then exits the loop, ending the program.

If the user says “exit”, the assistant responds with “Goodbye!” and ends the loop.

For any other unrecognized input, the assistant responds with a prompt: “I didn't catch that. Please say 'hey how are you' or 'exit'.” This helps guide the user toward using acceptable commands.

The script ends with the standard Python idiom:

python
Copy
Edit
if __name__ == "__main__":
    main()
This ensures that the main() function is only executed when the script is run directly, not when imported as a module in another program.

In summary, this script provides a basic interactive experience using voice commands. It demonstrates how to use Python libraries for voice recognition and speech synthesis to create a simple conversational interface. While the assistant only responds to a limited set of commands, the structure can be easily expanded to handle more inputs and perform more complex tasks, making it a good foundation for building more advanced voice-enabled applications.
