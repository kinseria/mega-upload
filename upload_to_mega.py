from mega import Mega
import os
import requests

MEGA_EMAIL = os.getenv('MEGA_EMAIL')
MEGA_PASSWORD = os.getenv('MEGA_PASSWORD')
REMOTE_FILE_URL = os.getenv('REMOTE_FILE_URL')
LOCAL_FILENAME = os.getenv('LOCAL_FILENAME')

def download_file(url, local_path):
    response = requests.get(url)
    response.raise_for_status()
    with open(local_path, 'wb') as f:
        f.write(response.content)

def upload_file_to_mega():
    print("Downloading file from:", REMOTE_FILE_URL)
    download_file(REMOTE_FILE_URL, LOCAL_FILENAME)

    print("Logging into MEGA...")
    mega = Mega()
    m = mega.login(MEGA_EMAIL, MEGA_PASSWORD)

    print("Uploading to MEGA...")
    file = m.upload(LOCAL_FILENAME)
    print("Uploaded file:", file)

    # Generate public link
    public_url = m.get_upload_link(uploaded)
    print("Public MEGA link:", public_url)

    # Optionally return it for later use
    return public_url

if __name__ == "__main__":
    upload_file_to_mega()
