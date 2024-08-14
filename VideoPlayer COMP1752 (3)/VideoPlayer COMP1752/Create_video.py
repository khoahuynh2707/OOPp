import tkinter as tk
import tkinter.scrolledtext as tkst
import video_library as lib  # Assuming this module contains get_name() and increment_play_count()
from PlayPlaylist import PlayPlaylist  # Import the PlayPlaylist class

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert("1.0", content)

class CreateVideoList:
    def __init__(self, window):
        self.playlist = []
        self.window = window

        self.setup_window()
        self.create_widgets()
        self.layout_widgets()

    def setup_window(self):
        self.window.geometry("1000x800")
        self.window.title("Create Video List")

    def create_widgets(self):
        # Labels and Entries
        self.enter_lbl = tk.Label(self.window, text="Enter Video Number")
        self.input_txt = tk.Entry(self.window, width=10)

        # Buttons
        self.add_video_btn = tk.Button(self.window, text="Add to Playlist", command=self.add_to_playlist)
        self.play_playlist_btn = tk.Button(self.window, text="Play Playlist", command=self.play_playlist)
        self.reset_playlist_btn = tk.Button(self.window, text="Reset Playlist", command=self.reset_playlist)  # New button for resetting playlist

        # ScrolledText widget
        self.playlist_txt = tkst.ScrolledText(self.window, width=70, height=20, wrap="none")

        # Status label
        self.status_lbl = tk.Label(self.window, text="", font=("Helvetica", 10))

    def layout_widgets(self):
        # Layout
        self.enter_lbl.grid(row=0, column=0, padx=10, pady=10)
        self.input_txt.grid(row=0, column=1, padx=10, pady=10)
        self.add_video_btn.grid(row=0, column=2, padx=10, pady=10)
        self.play_playlist_btn.grid(row=2, column=3, padx=10, pady=10)
        self.reset_playlist_btn.grid(row=2, column=4, padx=10, pady=10)  # New reset button layout
        self.playlist_txt.grid(row=1, column=0, columnspan=7, padx=10, pady=10)
        self.status_lbl.grid(row=2, column=0, columnspan=7, sticky="W", padx=10, pady=10)

    def add_to_playlist(self):
        video_id = self.input_txt.get().strip()
        if not video_id:
            self.status_lbl.configure(text="Please enter a video number.")
            return

        name = lib.get_name(video_id)
        if name:
            if video_id not in self.playlist:
                self.playlist.append(video_id)
                self.update_playlist_display()
                self.status_lbl.configure(text=f"Added video {name} to playlist!")
            else:
                self.status_lbl.configure(text=f"Video {name} is already in the playlist.")
        else:
            self.status_lbl.configure(text=f"Video {video_id} not found!")

    def play_playlist(self):
        if not self.playlist:
            self.status_lbl.configure(text="Playlist is empty. Add videos first.")
            return

        # Increment play counts and update display
        for video_id in self.playlist:
            lib.increment_play_count(video_id)
        self.update_playlist_display()

        # Play the playlist using PlayPlaylist class
        player = PlayPlaylist(self.playlist_txt)
        playlist_names = [lib.get_name(video_id) for video_id in self.playlist]
        player.play(playlist_names)
        
        self.status_lbl.configure(text="Playlist played and play counts updated.")

    def reset_playlist(self):
        """Resets the playlist and clears the display."""
        self.playlist = []  # Clear the playlist
        self.update_playlist_display()  # Clear the playlist display
        self.status_lbl.configure(text="Playlist has been reset.")

    def update_playlist_display(self):
        playlist_names = [lib.get_name(video_id) for video_id in self.playlist]
        set_text(self.playlist_txt, "\n".join(playlist_names))

if __name__ == "__main__":
    window = tk.Tk()
    app = CreateVideoList(window)
    window.mainloop()
