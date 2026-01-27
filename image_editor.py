import tkinter as tk


# The Main GUI Class. Handles View and Controller logic.
class ImageEditorApp:
    """
    Main Application Class using Tkinter.
    Manages the UI, captures user input, and coordinates the Processor and History.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("HIT137 Group Assignment 3 - Image Editor")
        self.root.geometry("1100x700")
