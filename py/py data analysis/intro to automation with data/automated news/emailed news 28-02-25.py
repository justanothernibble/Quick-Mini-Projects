"""
(method) def get_top_headlines(
    q: Any | None = None,
    qintitle: Any | None = None,
    sources: Any | None = None,
    language: str = "en",
    country: Any | None = None,
    category: Any | None = None,
    page_size: Any | None = None,
    page: Any | None = None
) -> Any
"""

from newsapi import NewsApiClient
import smtplib, os
from datetime import date
from email.message import EmailMessage
from dotenv import load_dotenv

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

load_dotenv()

TO_EMAIL = os.getenv("TO_EMAIL")
FROM_EMAIL = os.getenv("FROM_EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def convertDate(dDate):
    """Converts YYYY-MM-DD ISO format"""
    conv = ""
    dateList = dDate.split("-")
    day = dateList[2]
    month = dateList[1]
    year = dateList[0]

    # Day Logic
    if day[0] == "1":
        conv += f"{day}th "
    elif day[1] == "1":
        conv += f"{day}st "
    elif day[1] == "2":
        conv += f"{day}nd "
    elif day[1] == "3":
        conv += f"{day}rd "
    else:
        conv += f"{day}th "

    # Month Logic
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    monthName = months[int(month) - 1]
    conv += f"{monthName} "

    # Year Logic
    conv+=f"{year}"
    return conv

client = NewsApiClient(api_key='')

def makeNewsReport():
    hl_response=client.get_top_headlines(sources='bbc-news')
    if hl_response['status'] == 'ok':
        hlr = hl_response
        hl_report = (f"Here are the current top {hlr['totalResults']} headlines:\n\n")
        i=1
        for article in hlr['articles']:
            
            hl_report+=f"{i}. {article['title']}\n"
            hl_report+=f"News agent: {article['source']['name']} --- Published at: {convertDate(article['publishedAt'][:10])}\n"
            hl_report+=f"Summary: {article['description']}\n"
            hl_report+=f"Read more here: {article['url']}\n\n"
            i+=1
            
        return hl_report
            
    else:
        print(f"Error: {hl_response['status']}")

def sendNewsReport():
    print(f"FROM_EMAIL: {FROM_EMAIL}, TO_EMAIL: {TO_EMAIL}")
    """Send email"""
    msg = EmailMessage()
    # Checking if .env is loaded proper.
    if not all([TO_EMAIL, FROM_EMAIL, EMAIL_PASSWORD]):
        print("Missing environment variables! Check your .env file.")
        exit()

    msg['Subject'] = f"Top Headlines as of {convertDate(str(date.fromisoformat(str(date.today()))))}"
    msg['From'] = FROM_EMAIL
    msg['To'] = TO_EMAIL
    msg.set_content(makeNewsReport())
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(FROM_EMAIL, EMAIL_PASSWORD)
        smtp.send_message(msg)

sendNewsReport()