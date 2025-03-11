"""
Output:
📄 https://example.com
Title: Example Domain
Headers: ['Example Domain']

📄 https://httpbin.org/html
Title: HTTPBIN
Headers: ['Herman Melville - Moby-Dick']

📄 https://www.python.org
Title: Welcome to Python.org
Headers: ['Welcome to Python.org', 'The Python Software Foundation']
"""



import aiohttp
import asyncio
from bs4 import BeautifulSoup
import requests
import time

"""def fetchHeaders(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        headers = soup.find_all(["h1", "h2", "h3"])
        if headers:
            report = ""
            i=1
            print(f"There are: {len(headers)} headers")
            for header in headers:
                report+=f"{i}. {header.get_text().strip()}"
                i+=1
                if i!=len(headers)+1:
                    report+="\n"
            return report
        else:
            return "No headers"
            
    else:
        return f"Error: {response.status_code}"""

async def fetch(url): # Standard function with error handling
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()
    except Exception as e:
        return f"Error: {e}"

async def main():
    start = time.time()

    urls = [ # "https://httpbin.org/get",
        "https://example.com",
        "https://www.python.org",
        "https://www.rust-lang.org/"
    ]

    tasks = []
    for i in range(len(urls)):
        tasks.append(fetch(urls[i]))
    
    results = await asyncio.gather(*tasks)

    if results:
        urlNum: int = 0 # Tracks the URL number
        rNum = 0 # Tracks the result number
        for result in results:
            soup = BeautifulSoup(result, 'html.parser')
            headers = soup.find_all(["h1", "h2", "h3"])
            title = soup.find("title")

            report = ""
            report+=f"📄 {urls[urlNum]}\nTitle: {title.get_text().strip()}\nHeaders:\n"
            
            urlNum+=1
            
            if headers:
                headers = [header.get_text().strip() for header in headers]
                
                hNum = 0 # Counter for tracking the numbeer of headers
                i=1 # Counter for the suffix position of headers in the printing
                for header in headers:
                    if hNum!=len(headers)-1:
                        report+=f"├─ {i}. {header}"
                    elif not rNum == len(results)-1:
                        report+=f"└─ {i}. {header}\n"
                    else:
                        report+=f"└─ {i}. {header}"
                    i+=1
                    if i!=len(headers)+1 and headers[hNum]!=len(headers)-1:
                        hNum+=1
                        report+="\n"
                print(report)
                rNum+=1
                
            else:
                print("No headers.")
            

    else:
        print("Nothing")
    end = time.time()
    print(f"Time of execution took {(end-start):.2f} seconds")

asyncio.run(main())
