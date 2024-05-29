import os
import sys
import subprocess

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

subprocess.run(["streamlit", "run", "view/main_view.py"])
