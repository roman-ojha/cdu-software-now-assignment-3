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

        # State Variables
        self.current_image = None
        self.filepath = None

        # --- GUI Setup ---
        self._setup_menu()

    def _setup_menu(self):
        """Initializes the Menu Bar with File and Edit options."""
        menubar = tk.Menu(self.root)

        # File Menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_image)
        file_menu.add_command(label="Save", command=self.save_image)
        file_menu.add_command(label="Save As", command=self.save_image_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        # Edit Menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.undo_action)
        edit_menu.add_command(label="Redo", command=self.redo_action)
        menubar.add_cascade(label="Edit", menu=edit_menu)

        self.root.config(menu=menubar)
