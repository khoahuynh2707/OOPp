import tkinter as tk
import tkinter.scrolledtext as tkst

import video_library as lib
import font_manager as fonts

# Function to set text in a text area
def set_text(text_area, content):
    # Deletes existing content in the text area
    text_area.delete("1.0", tk.END)
    # Inserts new content into the text area
    text_area.insert(1.0, content)

# Class to handle the Check Videos application
class CheckVideos():
    def __init__(self, window):
        # Set window size
        window.geometry("750x350")
        # Set window title
        window.title("Check Videos")
        #GUI
        # Button to list all videos
        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        # Label prompting user to enter video number
        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        # Text entry field for video number input
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # Button to check details of a specific video
        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)

        # ScrolledText widget to list all videos
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # Text widget to display details of a specific video
        self.video_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        # Label to show status messages
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        # Automatically list all videos when the application starts
        self.list_videos_clicked()

    # Method to handle the 'Check Video' button click
    def check_video_clicked(self):
        # Get the video number from the input field
        key = self.input_txt.get()
        # Fetch video details using the video number
        name = lib.get_name(key)
        if name is not None:
            director = lib.get_director(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            # Format video details for display
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            # Display video details in the text area
            set_text(self.video_txt, video_details)
        else:
            # Display an error message if the video is not found
            set_text(self.video_txt, f"Video {key} not found")
        # Update status label
        self.status_lbl.configure(text="Check Video button was clicked!")

    # Method to handle the 'List All Videos' button click
    def list_videos_clicked(self):
        # Fetch the list of all videos
        video_list = lib.list_all()
        # Display the list of videos in the text area
        set_text(self.list_txt, video_list)
        # Update status label
        self.status_lbl.configure(text="List Videos button was clicked!")

# Main entry point of the application
if __name__ == "__main__":
    # Create the main window
    window = tk.Tk()
    # Configure the fonts using the font manager
    fonts.configure()
    # Initialize the CheckVideos application
    CheckVideos(window)
    # Start the main event loop
    window.mainloop()
