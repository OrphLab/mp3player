import pygame
from pygame import mixer
import tkinter as tk
from layout import TkBtn, TkLabel, TkLabelFrame, TkListbox

class OrphMusic:
    def __init__(self, root):
        #Window setup
        self.root = root
        self.root.title("OrphMusic")
        self.root.geometry("1000x300")
        pygame.init() # Initialize the pygame
        
        # Music setup
        pygame.mixer.init() # Initialize the mixer
        self.track = tk.StringVar()   # Declaring track variable
        self.status = tk.StringVar()  # Declaring status variable
        self.track.set("Track: ")
        self.status.set("Status: ")
        
       # Layout
        song_frame=TkLabelFrame(self.root, "Song playing", 10, 15, 500, 100)
        song_playing=TkLabel(self.root, "This is a alot of text to test the label", 20, 40, 250, 30)        
        
        back_btn = TkBtn(self.root, "Back", 30, 80, 50, 30, self.Back_btn) 
        play_btn = TkBtn(self.root, "Play", 90, 80, 50, 30, self.Play_btn)
        pause_btn = TkBtn(self.root, "Pause", 150, 80, 50, 30, self.Pause_btn)
        stop_btn = TkBtn(self.root, "Stop", 210, 80, 50, 30, self.Stop_btn)
        next_btn = TkBtn(self.root, "Next", 270, 80, 50, 30, self.Next_btn)
        eject_btn = TkBtn(self.root, "Eject", 330, 80, 50, 30, self.Eject_btn)

        song_lib=TkListbox(self.root, 550, 20, 406, 223)                
        
    # Button Functions
    def Back_btn(self):
        print("back")


    def Play_btn(self):
        print("play")


    def Pause_btn(self):
        print("pause")


    def Stop_btn(self):
        print("stop")


    def Next_btn(self):
        print("next")


    def Eject_btn(self):
        print("eject")

root = tk.Tk()
app = OrphMusic(root)
root.mainloop()
