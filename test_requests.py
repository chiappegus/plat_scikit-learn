import requests

# 1. Define the URL of the website you want to download
url = 'https://www.python.org'
# The URL scheme (http:// or https://) is required

# 2. Send a GET request to the URL and get the response object
try:
    response = requests.get(url)
    # Raise an exception if the request was unsuccessful (e.g., 404 error)
    response.raise_for_status()

    # 3. Specify the local filename to save the content
    filename = "downloaded_website.html"

    # 4. Open a local file in write-binary mode ('wb') and write the content
    # Using 'wb' (write binary) is a good practice as it handles all content types correctly
    with open(filename, 'wb') as f:
        f.write(response.content)

    print(f"Successfully downloaded the website content to {filename}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
