import threading
import webbrowser
from .gui import NgaoSecGUI
from .web.server import start_server

def main():
    # Start the web server in a separate thread
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    
    # Open the browser
    webbrowser.open("http://127.0.0.1:9090")
    
    # Start the Tkinter GUI
    app = NgaoSecGUI()
    app.mainloop()

if __name__ == "__main__":
    main()
