import os
import requests
import threading
import time

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.realpath(__file__))
# Create the logos directory if it doesn't exist
logos_dir = os.path.join(script_dir, 'logos')
os.makedirs(logos_dir, exist_ok=True)

def fetch(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        filename = os.path.basename(url)
        file_path = os.path.join(logos_dir, filename)
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"✅ Downloaded: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to download {url}: {e}")

def main():
    start = time.time()
    urls = [
        "https://www.python.org/static/community_logos/python-logo.png",
        "https://www.rust-lang.org/logos/rust-logo-blk.svg",
        "https://isocpp.org/assets/images/cpp_logo.png"
    ]
    
    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch, args=(url,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

    end = time.time()
    print(f"⏱️ Time taken: {end - start:.2f} seconds")

if __name__ == "__main__":
    main()
