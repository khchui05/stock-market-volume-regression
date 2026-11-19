"""Download the raw Smarket dataset into data/00-raw/.

Run from the repository root:
    python modules/get_data.py
"""
import os
import urllib.request

FILES = [
    {
        "url": "https://raw.githubusercontent.com/intro-stat-learning/ISLP/main/ISLP/data/Smarket.csv",
        "filename": "Smarket.csv",
    },
]


def get_raw(file_list, destination_directory):
    """Download each {'url', 'filename'} entry in file_list into destination_directory."""
    os.makedirs(destination_directory, exist_ok=True)
    for info in file_list:
        path = os.path.join(destination_directory, info["filename"])
        urllib.request.urlretrieve(info["url"], path)
        print(f"Downloaded {info['filename']} -> {path}")


if __name__ == "__main__":
    get_raw(FILES, os.path.join("data", "00-raw"))
