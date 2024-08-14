import tkinter as tk

class PlayPlaylist:
    def __init__(self, playlist_txt):
        self.playlist_txt = playlist_txt

    def play(self, playlist):
        self.playlist_txt.insert(tk.END, "\n\nPlaying playlist:\n")
        for video in playlist:
            self.play_video(video)
            self.playlist_txt.insert(tk.END, f"Playing: {video}\n")
            self.playlist_txt.yview(tk.END)  # Scroll to the end

    def play_video(self, video):
        # This function simulates playing a video
        # You can replace this with actual video playing logic
        print(f"Simulating playing video: {video}")
