import os
import requests
from urllib.parse import urlparse
import uuid  # to generate unique names if filename is missing

def fetch_image():
    # Step 1: Prompt user for URL
    url = input("Enter the image URL: ").strip()

    # Step 2: Create directory
    folder = "Fetched_Images"
    os.makedirs(folder, exist_ok=True)

    try:
        # Step 3: Fetch image
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()  # raise HTTPError for bad responses

        # Step 4: Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)  # extract last part of URL

        # If no filename found, generate one
        if not filename or "." not in filename:
            filename = f"image_{uuid.uuid4().hex}.jpg"

        filepath = os.path.join(folder, filename)

        # Step 5: Save the image in binary mode
        with open(filepath, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"✅ Image successfully saved as {filepath}")

    except requests.exceptions.RequestException as e:
        print(f" Error fetching the image: {e}")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")

# Run the function
if _name_ == "_main_":
    fetch_image()