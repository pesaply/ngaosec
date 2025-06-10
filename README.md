# NgaoSec

A local browser-based security application with GUI.

## Installation

```bash
pip install ngaosec

text

## How to Package and Distribute

1. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the package in development mode:

bash
pip install -e .
Build the package:

bash
python setup.py sdist bdist_wheel
Upload to PyPI (you'll need a PyPI account):

bash
pip install twine
twine upload dist/*
Features
Local Web Server: Runs on 127.0.0.1:9090 for security

Tkinter GUI: Provides a local control panel

Easy Installation: Can be installed via pip

Cross-platform: Works on Windows, macOS, and Linux

Notes
The web server and GUI run in separate threads to avoid blocking

All processing happens locally - no data is sent to external servers

You can extend this basic structure to add more functionality

Would you like me to add any specific features to this basic structure?

New chat
