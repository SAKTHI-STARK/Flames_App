import tkinter as tk
from PIL import Image, ImageTk
#animation for gif class
class AnimatedGIF(tk.Label):
    def __init__(self, master, path, delay=100):
        super().__init__(master)
        self.delay = delay
        self.frames = []
        self.load_frames(path)
        self.current_frame = 0
        self.update_frame()
    #fuction to initialize GIF frame
    def load_frames(self, path):
        gif = Image.open(path)
        for frame in range(gif.n_frames):
            gif.seek(frame)
            frame_image = ImageTk.PhotoImage(gif.copy())
            self.frames.append(frame_image)
    #function to update the frames
    def update_frame(self):
        self.config(image=self.frames[self.current_frame])
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.after(self.delay, self.update_frame)

