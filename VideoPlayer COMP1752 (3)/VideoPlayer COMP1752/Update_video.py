import tkinter as tk
from tkinter import messagebox
import video_library as lib
import font_manager as fonts

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, content) 

def errorID():
    messagebox.showwarning(title="Invalid ID", message="Please enter a valid ID")

def errorReview():
    messagebox.showwarning(title="Invalid Rating", message="Please enter a valid rating")

def success():
    messagebox.showinfo(title="New rating saved", message="New rating saved successfully")

class UpdateVideo:
    def __init__(self, window):

        window.geometry("950x350")
        window.title("Update Your Video")
        
        self.ratingdtb = {'1', '2', '3', '4', '5'}
        
        self.create_widgets(window)
        
        self.listall()
    
    def create_widgets(self, window):
       
        listall_button = tk.Button(window, text="List All Videos", command=self.listall, bg="#4158D0", fg="white", font=("Arial", 12))
        listall_button.grid(row=0, column=0, padx=10, pady=10)
        
        self.check_video = tk.Button(window, text="Check Video", command=self.displayinfo, bg="#4158D0", fg="white", font=("Arial", 12))
        self.check_video.grid(row=0, column=3, padx=10, pady=10)
        
        self.save = tk.Button(window, text="Save", command=self.NewRating, bg="#4158D0", fg="white", font=("Arial", 12))
        self.save.grid(row=0, column=6, padx=10, pady=10)
        
        self.video_box = tk.Text(window, width=50, height=7, font=("Arial", 12))
        self.video_box.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)
        
        self.Videoinfo_box = tk.Text(window, width=30, height=7, wrap="none", font=("Arial", 12))
        self.Videoinfo_box.grid(row=1, column=3, columnspan=3, sticky="W", padx=10, pady=10)
        
        self.Video_ID = tk.Label(window, font=("Arial", 15), text="Enter Video ID")
        self.Video_ID.grid(row=0, column=1, padx=10, pady=10)
        
        self.label = tk.Label(window, font=("Arial", 15), text="Enter New Rating")
        self.label.grid(row=0, column=4, padx=10, pady=10)
        
        self.status = tk.Label(window, text="", font=("Arial", 15))
        self.status.grid(row=8, column=0, columnspan=4, sticky="W", padx=10, pady=10)
        
        self.ID_input = tk.Entry(window, width=30, font=("Arial", 12))
        self.ID_input.grid(row=0, column=2, padx=8, pady=10)
        
        self.rating_input = tk.Entry(window, width=20, font=("Arial", 12))
        self.rating_input.grid(row=0, column=5, padx=8, pady=10)
  
    def DisplayInfo(self, key, name, director=None, rating=None, playcount=None):
        director, playcount, rating = self.GetInfo(key)
        info = f"{name}\n{director}\nRating: {rating}\nPlays: {playcount}"
        set_text(self.Videoinfo_box, info)

    def GetInfo(self, key):
        director = lib.get_director(key)
        playcount = lib.get_play_count(key)
        rating = lib.get_rating(key)
        return director, playcount, rating

    def GetNameAndKey(self):
        key = self.ID_input.get()
        name = lib.get_name(key)
        return key, name

    def listall(self):
        showlist = lib.list_all()
        set_text(self.video_box, showlist)
        self.status.configure(text="Status: Showing All Videos")

    def displayinfo(self):
        key, name = self.GetNameAndKey()
        director, rating, playcount = self.GetInfo(key)
        if name is not None:
            self.DisplayInfo(key, name, director, rating, playcount)
        else:
            errorID()
        self.status.configure(text="Status: Checking Video Info")

    def NewRating(self):
        key, name = self.GetNameAndKey()
        newrate = self.rating_input.get()
        if key:
            if newrate in self.ratingdtb:
                lib.set_rating(key, newrate)
                a = lib.get_rating(key)
                self.DisplayInfo(key, name, rating=a)
                success()
                self.status.configure(text="Status: Saved new rating")
            else:
                errorReview()
                self.status.configure(text="Status: No new rating was saved")
if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    app = UpdateVideo(window)
    window.mainloop()
