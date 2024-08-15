import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
from pydub.playback import play

# Membuat jendela utama
root = tk.Tk()
root.title("Music Player")

# Mendefinisikan fungsi untuk memutar musik
def play_music():
    file_path = filedialog.askopenfilename()
    if file_path:
        audio = AudioSegment.from_file('Lagu.mp3')
        play(audio)

# Membuat tombol play
play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack()

# Menjalankan loop acara Tkinter
root.mainloop()