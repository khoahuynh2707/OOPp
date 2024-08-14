import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as tkst
import csv
import os
import webbrowser

CSV_FILE = "video_library.csv"

def load_videos():
    videos = []
    expected_columns = {"Video Name", "Director Name", "Rating"}
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="r", newline='') as file:
            reader = csv.DictReader(file)
            if set(reader.fieldnames) == expected_columns:
                for row in reader:
                    videos.append(row)
            else:
                print("Error: The CSV file does not have the expected column names.")
    return videos

def update_video(original_video_name, updated_video):
    videos = load_videos()
    with open(CSV_FILE, mode="w", newline='') as file:
        fieldnames = ["Video Name", "Director Name", "Rating"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for video in videos:
            if video["Video Name"] == original_video_name:
                writer.writerow(updated_video)
            else:
                writer.writerow(video)

class VideoLibraryApp:
    def __init__(self, window):
        # Set window size
        window.geometry("800x500")
        # Set window title
        window.title("Video Library")

        # Create a notebook (tab control)
        self.notebook = ttk.Notebook(window)
        self.notebook.pack(expand=1, fill="both")

        # Create tabs
        self.create_tab = ttk.Frame(self.notebook)
        self.update_tab = ttk.Frame(self.notebook)
        
        self.notebook.add(self.create_tab, text="Create Video")
        self.notebook.add(self.update_tab, text="Update Video")

        self.create_video_ui()
        self.update_video_ui()

    def create_video_ui(self):
        # Create tab UI
        name_lbl = tk.Label(self.create_tab, text="Video Name:")
        name_lbl.grid(row=0, column=0, padx=10, pady=10)

        self.name_txt = tk.Entry(self.create_tab, width=50)
        self.name_txt.grid(row=0, column=1, padx=10, pady=10)

        director_lbl = tk.Label(self.create_tab, text="Director Name:")
        director_lbl.grid(row=1, column=0, padx=10, pady=10)

        self.director_txt = tk.Entry(self.create_tab, width=50)
        self.director_txt.grid(row=1, column=1, padx=10, pady=10)

        rating_lbl = tk.Label(self.create_tab, text="Rating:")
        rating_lbl.grid(row=2, column=0, padx=10, pady=10)

        self.rating_txt = tk.Entry(self.create_tab, width=50)
        self.rating_txt.grid(row=2, column=1, padx=10, pady=10)

        save_btn = tk.Button(self.create_tab, text="Save Video", command=self.save_video_clicked)
        save_btn.grid(row=3, column=0, columnspan=2, pady=20)

        search_btn = tk.Button(self.create_tab, text="Search on YouTube", command=self.search_youtube_create)
        search_btn.grid(row=3, column=1, padx=10, pady=10, sticky="E")

        self.saved_videos_txt = tkst.ScrolledText(self.create_tab, width=70, height=10, wrap="none")
        self.saved_videos_txt.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.status_lbl = tk.Label(self.create_tab, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=5, column=0, columnspan=2, sticky="W", padx=10, pady=10)

        self.load_videos(self.saved_videos_txt)

    def update_video_ui(self):
        # Update tab UI
        name_lbl = tk.Label(self.update_tab, text="Original Video Name:")
        name_lbl.grid(row=0, column=0, padx=10, pady=10)

        self.original_name_txt = tk.Entry(self.update_tab, width=50)
        self.original_name_txt.grid(row=0, column=1, padx=10, pady=10)

        new_name_lbl = tk.Label(self.update_tab, text="New Video Name:")
        new_name_lbl.grid(row=1, column=0, padx=10, pady=10)

        self.new_name_txt = tk.Entry(self.update_tab, width=50)
        self.new_name_txt.grid(row=1, column=1, padx=10, pady=10)

        director_lbl = tk.Label(self.update_tab, text="New Director Name:")
        director_lbl.grid(row=2, column=0, padx=10, pady=10)

        self.new_director_txt = tk.Entry(self.update_tab, width=50)
        self.new_director_txt.grid(row=2, column=1, padx=10, pady=10)

        rating_lbl = tk.Label(self.update_tab, text="New Rating:")
        rating_lbl.grid(row=3, column=0, padx=10, pady=10)

        self.new_rating_txt = tk.Entry(self.update_tab, width=50)
        self.new_rating_txt.grid(row=3, column=1, padx=10, pady=10)

        update_btn = tk.Button(self.update_tab, text="Update Video", command=self.update_video_clicked)
        update_btn.grid(row=4, column=0, columnspan=2, pady=20)

        self.updated_videos_txt = tkst.ScrolledText(self.update_tab, width=70, height=10, wrap="none")
        self.updated_videos_txt.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.status_update_lbl = tk.Label(self.update_tab, text="", font=("Helvetica", 10))
        self.status_update_lbl.grid(row=6, column=0, columnspan=2, sticky="W", padx=10, pady=10)

        self.load_videos(self.updated_videos_txt)

        search_btn = tk.Button(self.update_tab, text="Search on YouTube", command=self.search_youtube_update)
        search_btn.grid(row=7, column=0, columnspan=2, pady=10)

    def load_videos(self, widget):
        videos = load_videos()
        widget.delete(1.0, tk.END)  # Clear the existing content before loading new data
        for video in videos:
            widget.insert(tk.END, f"Video Name: {video['Video Name']}\n")
            widget.insert(tk.END, f"Director Name: {video['Director Name']}\n")
            widget.insert(tk.END, f"Rating: {video['Rating']}\n")
            widget.insert(tk.END, "-"*50 + "\n")

    def save_video_clicked(self):
        video_name = self.name_txt.get()
        director_name = self.director_txt.get()
        rating = self.rating_txt.get()

        if video_name and director_name and rating:
            # Define save_video function
            def save_video(video_name, director_name, rating):
                videos = load_videos()
                with open(CSV_FILE, mode="a", newline='') as file:
                    fieldnames = ["Video Name", "Director Name", "Rating"]
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    if not videos:
                        writer.writeheader()
                    writer.writerow({
                        "Video Name": video_name,
                        "Director Name": director_name,
                        "Rating": rating
                    })
        
            save_video(video_name, director_name, rating)
        
            self.name_txt.delete(0, tk.END)
            self.director_txt.delete(0, tk.END)
            self.rating_txt.delete(0, tk.END)

            self.status_lbl.configure(text="Video saved successfully!")
            self.load_videos(self.saved_videos_txt)  # Refresh the video list
        else:
            self.status_lbl.configure(text="Please fill in all fields!")

    def update_video_clicked(self):
        original_video_name = self.original_name_txt.get()
        new_video_name = self.new_name_txt.get()
        new_director_name = self.new_director_txt.get()
        new_rating = self.new_rating_txt.get()

        if original_video_name and new_video_name and new_director_name and new_rating:
            updated_video = {
                "Video Name": new_video_name,
                "Director Name": new_director_name,
                "Rating": new_rating
            }
            update_video(original_video_name, updated_video)
            
            self.updated_videos_txt.delete(1.0, tk.END)
            self.load_videos(self.updated_videos_txt)
            
            self.original_name_txt.delete(0, tk.END)
            self.new_name_txt.delete(0, tk.END)
            self.new_director_txt.delete(0, tk.END)
            self.new_rating_txt.delete(0, tk.END)

            self.status_update_lbl.configure(text="Video updated successfully!")
        else:
            self.status_update_lbl.configure(text="Please fill in all fields!")

    def search_youtube_create(self):
        video_name = self.name_txt.get()
        if video_name:
            query = video_name.replace(" ", "+")
            url = f"https://www.youtube.com/results?search_query={query}"
            webbrowser.open(url)
        else:
            self.status_lbl.configure(text="Please enter a video name to search!")

    def search_youtube_update(self):
        video_name = self.new_name_txt.get()
        if video_name:
            query = video_name.replace(" ", "+")
            url = f"https://www.youtube.com/results?search_query={query}"
            webbrowser.open(url)
        else:
            self.status_update_lbl.configure(text="Please enter a video name to search!")

if __name__ == "__main__":
    window = tk.Tk()
    app = VideoLibraryApp(window)
    window.mainloop()
