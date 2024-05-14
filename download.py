import os
import time
import urllib.request
import hashlib
from urllib.error import URLError
from urllib.request import Request, urlopen

def download_file(url, shasum, save_path):
    try:
        req = Request(
            url=url,
            headers={
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0"
            }
        )
        with urlopen(req) as response:
            data = response.read()
            data_hash = hashlib.sha256(data).hexdigest()
            if data_hash != shasum:
                raise RuntimeError(f"URL: {url} failed sha256 check. \nGot: {data_hash}\n Expected: {shasum}")
            with open(save_path, "wb") as f:
                f.write(data)
        print(f"Downloaded {save_path}")
    except URLError as e:
        raise RuntimeError(f"Failed download from {url}") from e

def sanitize_path(path):
    specials = ".-_"
    spath = ""
    for c in path:
        if not c.isalnum() and c not in specials:
            c = "_"
        spath += c
    if spath == "..":
        spath = "_"

    return spath

def main():
    base_url = "https://assets.getkestrel.com"
    releases = "releases.txt"
    base_dir = "static"

    urls = []
    with open(releases, "r") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if line == "":
            continue
        tokens = line.split("|")
        url = base_url + tokens[0].strip()
        shasum = tokens[1].strip()
        urls.append((url, shasum))
    
    for url in urls:
        http_url, shasum = url
        path_parts = http_url.split("/")[3:]
        path_parts = [sanitize_path(p) for p in path_parts]
        file_path = os.path.join(base_dir, *path_parts)
        
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        download_file(http_url, shasum, file_path)
        time.sleep(0.05)

if __name__ == "__main__":
    main()
