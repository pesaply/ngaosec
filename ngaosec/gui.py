import tkinter as tk
from tkinter import ttk

class NgaoSecGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("NgaoSec Local Application")
        self.geometry("400x300")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title label
        title_label = ttk.Label(
            main_frame, 
            text="NgaoSec Local Control Panel",
            font=("Helvetica", 14, "bold")
        )
        title_label.pack(pady=10)
        
        # Info label
        info_label = ttk.Label(
            main_frame,
            text="Web interface is running at http://127.0.0.1:9090\n"
                 "You can control the application from here or the web interface.",
            justify=tk.CENTER
        )
        info_label.pack(pady=10)
        
        # Status frame
        status_frame = ttk.LabelFrame(main_frame, text="Status", padding="10")
        status_frame.pack(fill=tk.X, pady=10)
        
        self.server_status = ttk.Label(
            status_frame,
            text="Web server: Running",
            foreground="green"
        )
        self.server_status.pack()
        
        # Buttons frame
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(pady=10)
        
        refresh_btn = ttk.Button(
            buttons_frame,
            text="Refresh Status",
            command=self.refresh_status
        )
        refresh_btn.pack(side=tk.LEFT, padx=5)
        
        exit_btn = ttk.Button(
            buttons_frame,
            text="Exit",
            command=self.destroy
        )
        exit_btn.pack(side=tk.RIGHT, padx=5)
    
    def refresh_status(self):
        # Here you could add actual status checking
        self.server_status.config(text="Web server: Running", foreground="green")
