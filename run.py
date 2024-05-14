import subprocess

comando = ["streamlit", "run", "view/main_view.py"]

subprocess.Popen(comando, shell=True)
