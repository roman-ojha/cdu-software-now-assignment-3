import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import cv2
from PIL import Image, ImageTk
import os
from image_processor import ImageProcessor
from history_manager import HistoryManager


class ImageEditorApp:
    """
    Main Application Class using Tkinter.
    Manages the UI, captures user input, and coordinates the Processor and History.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("HIT137 Group Assignment 3 - Image Editor")
        self.root.geometry("1100x700")

        # Creating instances of HistoryManager inside ImageEditorApp class
        self.processor = ImageProcessor()
        self.history = HistoryManager()

        # State Variables
        self.current_image = None
        self.filepath = None

        # Setup UI Components
        self._setup_menu()
        self._setup_layout()

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

        # 1. Control Panel on Right Side
        self.controls_frame = tk.Frame(
            self.root, width=250, bg="#f0f0f0", padx=10, pady=10)
        self.controls_frame.pack(side=tk.RIGHT, fill=tk.Y)

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
            90)).pack(side=tk.RIGHT, padx=2)
        tk.Button(btn_frame_rot, text="180°", command=lambda: self.apply_rotate(
            180)).pack(side=tk.RIGHT, padx=2)
        tk.Button(btn_frame_rot, text="270°", command=lambda: self.apply_rotate(
            270)).pack(side=tk.RIGHT, padx=2)

        # Flip Buttons
        tk.Label(self.controls_frame, text="Flip", bg="#f0f0f0",
                 font=("Arial", 10, "bold"), foreground="#000000").pack(pady=(10, 0))
        btn_frame_flip = tk.Frame(self.controls_frame, bg="#f0f0f0")
        btn_frame_flip.pack()
        tk.Button(btn_frame_flip, text="Horiz",
                  command=lambda: self.apply_flip(1)).pack(side=tk.RIGHT, padx=2)
        tk.Button(btn_frame_flip, text="Vert", command=lambda: self.apply_flip(
            0)).pack(side=tk.RIGHT, padx=2)

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

        # Creating a Container that will hold both image display and status bar
        container = tk.Frame(self.root, bg="lightgrey")
        container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # 2. Image Display Area at the Left Bottom Side
        self.display_frame = tk.Frame(container, bg="#333")
        self.display_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(
            self.display_frame, bg="#333", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # 3. Status Bar
        """Sets up the Status Bar at the top."""
        self.status_var = tk.StringVar()
        self.status_var.set("Open an image to start editing.")
        self.status_bar = tk.Label(
            container, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.TOP, fill=tk.X)

    # File Operations
    def open_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")])
        if file_path:
            self.filepath = file_path
            # Read image using OpenCV
            img = cv2.imread(file_path)
            if img is None:
                messagebox.showerror("Error", "Could not load image.")
                return

            self.current_image = img
            # Clear history when loading new image
            self.history = HistoryManager()
            self.display_image()
            self.update_status(f"Loaded: {os.path.basename(file_path)}")

    def save_image(self):
        if self.current_image is None:
            messagebox.showwarning("Warning", "No image to save.")
            return
        if self.filepath:
            cv2.imwrite(self.filepath, self.current_image)
            messagebox.showinfo("Success", "Image saved successfully.")
        else:
            self.save_image_as()

    def save_image_as(self):
        if self.current_image is None:
            messagebox.showwarning("Warning", "No image to save.")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg",
                                                 filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("BMP", "*.bmp")])
        if file_path:
            cv2.imwrite(file_path, self.current_image)
            self.filepath = file_path
            messagebox.showinfo("Success", "Image saved successfully.")

    # Display Logic
    def display_image(self):
            """Converts OpenCV BGR image to Tkinter format and displays it."""
            if self.current_image is None:
                return

            # Convert BGR from OpenCV to RGB Tkinter
            img_rgb = cv2.cvtColor(self.current_image, cv2.COLOR_BGR2RGB)

            # Resize for display if too large to maintain aspect ratio
            h, w = img_rgb.shape[:2]
            display_w, display_h = 800, 600

            if w > display_w or h > display_h:
                ratio = min(display_w/w, display_h/h)
                new_w = int(w * ratio)
                new_h = int(h * ratio)
                img_rgb = cv2.resize(img_rgb, (new_w, new_h))

            img_pil = Image.fromarray(img_rgb)
            img_tk = ImageTk.PhotoImage(img_pil)

            # Update Canvas
            self.canvas.delete("all")
            # Center the image
            canvas_w = self.canvas.winfo_width()
            canvas_h = self.canvas.winfo_height()
            # Default center if canvas isn't drawn yet
            if canvas_w < 1:
                canvas_w = 800
            if canvas_h < 1:
                canvas_h = 600

            self.canvas.create_image(
                canvas_w//2, canvas_h//2, image=img_tk, anchor=tk.CENTER)
            self.canvas.image = img_tk  # Keep reference to prevent garbage collection

    def update_status(self, message):
        """Updates the text in the status bar"""
        if self.current_image is not None:
            h, w, _ = self.current_image.shape
            info = f" | Size: {w}x{h} px"
        else:
            info = ""
        self.status_var.set(message + info)
        
    def save_state(self):
        """Helper to push current state to history before modification."""
        if self.current_image is not None:
            self.history.push_state(self.current_image)

    # Filter Callbacks (Events)
    def apply_grayscale(self):
        if self.current_image is not None:
            self.save_state()
            # If image is already grayscale (2 dim), don't fail, but processing expects BGR usually
            if len(self.current_image.shape) == 2:
                # Convert back to BGR so other filters work seamlessly
                self.current_image = cv2.cvtColor(
                    self.current_image, cv2.COLOR_GRAY2BGR)

            gray = self.processor.to_grayscale(self.current_image)
            # Convert back to BGR for consistent handling in other filters
            self.current_image = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
            self.display_image()
            self.update_status("Applied Grayscale")

    def apply_blur(self):
        if self.current_image is not None:
            self.save_state()
            val = self.blur_scale.get()
            self.current_image = self.processor.apply_blur(
                self.current_image, val)
            self.display_image()
            self.update_status(f"Applied Blur (Level {val})")

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

    # Undo / Redo
    def undo_action(self):
        prev = self.history.undo(self.current_image)
        if prev is not None:
            self.current_image = prev
            self.display_image()
            self.update_status("Undo performed")
        else:
            messagebox.showinfo("Info", "Nothing to undo")

    def redo_action(self):
        nxt = self.history.redo(self.current_image)
        if nxt is not None:
            self.current_image = nxt
            self.display_image()
            self.update_status("Redo performed")
        else:
            messagebox.showinfo("Info", "Nothing to redo")
