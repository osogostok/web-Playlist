import argparse
import requests
from bs4 import BeautifulSoup

SERVER_URL = 'http://127.0.0.1:8888/'


def read_args():
    parser = argparse.ArgumentParser(description='Great Description')
    parser.add_argument('action', choices=[
                        'upload', 'list'], help="Chose list or upload")
    parser.add_argument('file', nargs='?', help='Path to the audio file')
    args = parser.parse_args()
    return args


def action_list(response):
    soup = BeautifulSoup(response.text, "html.parser")
    audio_block = soup.find_all(class_="audio-block")
    for audio in audio_block:
        p_element = audio.find('p')
        if p_element:
            print(p_element.text)


def action_upload(file_path):
    with open(file_path, 'rb') as file:
        files = {'audioFiles': file}
        requests.post(SERVER_URL, files=files)


def main():
    args = read_args()
    response = requests.get(SERVER_URL)
    if response.status_code == 200:
        if args.action == 'list':
            action_list(response)
        if args.action == 'upload':
            action_upload(args.file)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
