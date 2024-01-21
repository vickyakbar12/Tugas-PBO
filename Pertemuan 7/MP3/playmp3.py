import pygame
import tkinter as tk

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")

        self.label = tk.Label(root, text="Spotify TIF22")
        self.label.pack(pady=10)

        self.current_song = 0
        self.songs = ["Dawai.mp3", "Sunshine.mp3", "Lammer.mp3"]  
        
        # Ganti dengan nama lagu yang ingin Anda gunakan
        self.play_button = tk.Button(self.root, text="Play", command=self.play_music)
        self.play_button.pack(pady=15)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.stop_button.pack(padx=15)

        self.change_button = tk.Button(self.root, text="Ganti Lagu", command=self.change_song)
        self.change_button.pack(pady=15)

        

        pygame.init()
        self.player = pygame.mixer.music

    def play_music(self):
        pygame.mixer.init()
        self.player.load(self.songs[self.current_song])
        self.player.play()

    def stop_music(self):
        self.player.stop()

    def change_song(self):
        self.stop_music()
        self.current_song = (self.current_song + 1) % len(self.songs)
        print(f"Playing: {self.songs[self.current_song]}")
        self.play_music()

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
