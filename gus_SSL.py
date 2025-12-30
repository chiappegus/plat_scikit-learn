import requests
import urllib3

# Desactivar advertencias de SSL (opcional)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://www.python.org'

try:
    # Añadir verify=False para saltar la verificación SSL
    response = requests.get(url, verify=False)
    response.raise_for_status()

    filename = "Welcome to Python.org.html"
    with open(filename, 'wb') as f:
        f.write(response.content)

    print(f"Successfully downloaded the website content to {filename}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")