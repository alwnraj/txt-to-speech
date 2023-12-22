import pyttsx3

val = input("Enter your statement: ")

engine = pyttsx3.init()

engine.say(val)

engine.save_to_file(val, 'test.mp3')

engine.runAndWait()


