import requests
from bs4 import BeautifulSoup
import threading
import time

def fetch(url, index, results):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            results[index] = response.text
        else:
            results[index] = f"Error: HTTP {response.status_code}"
    except Exception as e:
        results[index] = f"Error: {e}"

def main():
    start = time.time()

    urls = [
        "https://example.com",
        "https://www.python.org",
        "https://www.rust-lang.org/"
    ]

    results = [None] * len(urls)
    threads = []
    for index, url in enumerate(urls):
        thread = threading.Thread(target=fetch, args=(url, index, results))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Process results
    for i, result in enumerate(results):
        url = urls[i]
        if result.startswith("Error:"):
            print(f"❌ {url}: {result}")
            continue
        
        soup = BeautifulSoup(result, 'html.parser')
        headers = soup.find_all(["h1", "h2", "h3"])
        title_tag = soup.find("title")
        title = title_tag.get_text().strip() if title_tag else "No title"

        report = f"📄 {url}\nTitle: {title}\nHeaders:\n"
        
        if headers:
            header_lines = []
            for idx, header in enumerate(headers, 1):
                header_text = header.get_text().strip()
                if idx == len(headers):
                    prefix = "└─"
                else:
                    prefix = "├─"
                header_lines.append(f"{prefix} {idx}. {header_text}")
            
            # Handle line breaks between headers
            report += "\n".join(header_lines)
            
            # Add a newline after report unless it's the last result
            if i != len(results) - 1:
                report += "\n"
        else:
            report += "No headers found."

        print(report)

    end = time.time()
    print(f"\nExecution time took {(end - start):.2f} seconds")

if __name__ == "__main__":
    main()