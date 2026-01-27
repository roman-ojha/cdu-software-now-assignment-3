import tkinter as tk


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

        # Setup UI Components
        self._setup_menu()
        self._setup_layout()
        self._setup_status_bar()

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

    def _setup_layout(self):
        """Sets up the main frames with controls button on left side and image display on right side."""

        # 1. Control Panel on Left Side
        self.controls_frame = tk.Frame(
            self.root, width=250, bg="#f0f0f0", padx=10, pady=10)
        self.controls_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Section Label
        tk.Label(self.controls_frame, text="Filters & Effects",
                 bg="#f0f0f0", font=("Arial", 12, "bold"), foreground="#000000").pack(pady=10)

        # Buttons for simple filters
        tk.Button(self.controls_frame, text="Grayscale", width=20,
                  command=self.apply_grayscale).pack(pady=2)
        tk.Button(self.controls_frame, text="Edge Detection",
                  width=20, command=self.apply_edge_detection).pack(pady=2)

        # Rotation Buttons
        tk.Label(self.controls_frame, text="Rotate", bg="#f0f0f0",
                 font=("Arial", 10, "bold"), foreground="#000000").pack(pady=(10, 0))
        btn_frame_rot = tk.Frame(self.controls_frame, bg="#f0f0f0")
        btn_frame_rot.pack()
        tk.Button(btn_frame_rot, text="90°", command=lambda: self.apply_rotate(
            90)).pack(side=tk.LEFT, padx=2)
        tk.Button(btn_frame_rot, text="180°", command=lambda: self.apply_rotate(
            180)).pack(side=tk.LEFT, padx=2)
        tk.Button(btn_frame_rot, text="270°", command=lambda: self.apply_rotate(
            270)).pack(side=tk.LEFT, padx=2)

        # Flip Buttons
        tk.Label(self.controls_frame, text="Flip", bg="#f0f0f0",
                 font=("Arial", 10, "bold"), foreground="#000000").pack(pady=(10, 0))
        btn_frame_flip = tk.Frame(self.controls_frame, bg="#f0f0f0")
        btn_frame_flip.pack()
        tk.Button(btn_frame_flip, text="Horiz",
                  command=lambda: self.apply_flip(1)).pack(side=tk.LEFT, padx=2)
        tk.Button(btn_frame_flip, text="Vert", command=lambda: self.apply_flip(
            0)).pack(side=tk.LEFT, padx=2)

        # Resize Button
        tk.Button(self.controls_frame, text="Resize Image",
                  width=20, command=self.apply_resize).pack(pady=10)

        # Sliders for Adjustable Effects

        # Blur Slider
        tk.Label(self.controls_frame, text="Blur Intensity",
                 bg="#f0f0f0", foreground="#000000").pack(pady=(10, 0))
        self.blur_scale = tk.Scale(
            self.controls_frame, from_=0, to=20, orient=tk.HORIZONTAL, bg="#f0f0f0")
        self.blur_scale.pack(fill=tk.X)
        tk.Button(self.controls_frame, text="Apply Blur",
                  command=self.apply_blur).pack(pady=2)

        # Brightness Slider
        tk.Label(self.controls_frame, text="Brightness",
                 bg="#f0f0f0", foreground="#000000").pack(pady=(10, 0))
        self.bright_scale = tk.Scale(
            self.controls_frame, from_=-100, to=100, orient=tk.HORIZONTAL, bg="#f0f0f0")
        self.bright_scale.pack(fill=tk.X)
        tk.Button(self.controls_frame, text="Apply Brightness",
                  command=self.apply_brightness).pack(pady=2)

        # Contrast Slider
        tk.Label(self.controls_frame, text="Contrast",
                 bg="#f0f0f0", foreground="#000000").pack(pady=(10, 0))
        self.contrast_scale = tk.Scale(
            self.controls_frame, from_=0.5, to=3.0, resolution=0.1, orient=tk.HORIZONTAL, bg="#f0f0f0")
        self.contrast_scale.set(1.0)
        self.contrast_scale.pack(fill=tk.X)
        tk.Button(self.controls_frame, text="Apply Contrast",
                  command=self.apply_contrast).pack(pady=2)

        # 2. Image Display Area at the Right Side
        self.display_frame = tk.Frame(self.root, bg="#333")
        self.display_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(
            self.display_frame, bg="#333", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def _setup_status_bar(self):
        """Sets up the Status Bar at the bottom."""
        self.status_var = tk.StringVar()
        self.status_var.set("Open an image to begin.")
        self.status_bar = tk.Label(
            self.root, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    # File Operations
    def open_image(self):
        pass

    def save_image(self):
        pass

    def save_image_as(self):
        pass

    # Display Logic
    def display_image(self):
        pass

    def update_status(self, message):
        pass

    # Filter Callbacks
    def apply_grayscale(self):
        pass

    def apply_blur(self):
        pass

    def apply_edge_detection(self):
        pass

    def apply_brightness(self):
        pass

    def apply_contrast(self):
        pass

    def apply_rotate(self, angle):
        pass

    def apply_flip(self, mode):
        pass

    def apply_resize(self):
        pass

    # Undo and Redo
    def undo_action(self):
        pass

    def redo_action(self):
        pass
