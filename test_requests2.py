import subprocess
import os

url = 'https://www.python.org'
filename = "Welcome to Python.org.html"

try:
    # Usar curl que maneja mejor los certificados en algunos entornos
    with open(filename, 'w', encoding='utf-8') as f:
        result = subprocess.run(['curl', '-s', '-L', url], 
                              capture_output=True, 
                              text=True, 
                              check=True)
        f.write(result.stdout)
    
    print(f"Successfully downloaded using curl to {filename}")
    
except subprocess.CalledProcessError as e:
    print(f"Error with curl: {e}")
except Exception as e:
    print(f"An error occurred: {e}")