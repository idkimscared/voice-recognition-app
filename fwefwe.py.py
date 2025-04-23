import speech_recognition as sr
import tkinter as tk
from tkinter import scrolledtext
import webbrowser

def start_speech_recognition():
    global recognizer
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("listening...")
        audio_data = recognizer.listen(source)

    try:
        global message
        message = recognizer.recognize_google(audio_data)
        print(f"You said: {message}")

        if message == "open Google":
            webbrowser.open("https://www.google.com")

        if message == "open Steam":
            webbrowser.open("https://store.steampowered.com/")
        if message == "open YouTube":
            webbrowser.open("https://www.youtube.com/")
        if message == "open Roblox":
            webbrowser.open("https://www.roblox.com/")
        if message == "open Discord":
            webbrowser.open("https://discord.com/")
        if message == "open Spotify":
            webbrowser.open("https://www.spotify.com/")
        if message == "close":
            app.destroy()

        
        
        
        text_box.config(state=tk.NORMAL)  
        text_box.delete("1.0", tk.END)  
        text_box.insert(tk.END, message)  
        text_box.config(state=tk.DISABLED)  
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")


app = tk.Tk()
app.title("Speech Recognition")
app.geometry("500x350")


button = tk.Button(app, text="Start", command=start_speech_recognition)
button.pack(pady=20)


label = tk.Label(app, text="Recognized Words:", font=("Arial", 16))
label.pack(pady=10)


text_box = scrolledtext.ScrolledText(app, wrap=tk.WORD, font=("Courier", 12), height=10, state=tk.DISABLED)
text_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)


app.mainloop()