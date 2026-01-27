import tkinter as tk
from image_editor import ImageEditorApp

if __name__ == "__main__":
    # Initialize the main Tkinter window
    root = tk.Tk()

    # Start the application
    app = ImageEditorApp(root)

    # Run the event loop
    root.mainloop()
