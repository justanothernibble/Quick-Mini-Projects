import schedule, time, requests, smtplib, os
from email.message import EmailMessage
from dotenv import load_dotenv

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

load_dotenv(dotenv_path="weather-report-smtp.env")

API_KEY = os.getenv("API_KEY")
CITY = os.getenv("CITY")
TO_EMAIL = os.getenv("TO_EMAIL")
FROM_EMAIL = os.getenv("FROM_EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def fetch():
    """Fetch weather from OpenWeather API"""
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"
    response = requests.get(URL)
    data = response.json()
    if response.status_code == 200:
        print("Weather data fetched. Processing...")
        return data
    return f"Failed to retrieve weather data. Response status code: {response.status_code}"

def process(data):
    if type(data) == str:
        return data
    """Process weather data"""
    weather = data['weather'][0]['main']
    weather_desc = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 2)
    feels_like = round(data['main']['feels_like'] - 273.15, 2)
    print("Data processed success. Sending email...")
    return f"{CITY} Weather Report\nCurrently expeirencing {weather}, more specifically {weather_desc}\nThe temperature is currently {temperature} degrees, but feels like {feels_like} degrees"

def send_email():
    print(f"FROM_EMAIL: {FROM_EMAIL}, TO_EMAIL: {TO_EMAIL}")
    """Send email"""
    msg = EmailMessage()
    if not all([API_KEY, CITY, TO_EMAIL, FROM_EMAIL, EMAIL_PASSWORD]):
        print("Missing environment variables! Check your .env file.")
        exit()
    msg['Subject'] = "Weather Update"
    msg['From'] = FROM_EMAIL
    msg['To'] = TO_EMAIL
    msg.set_content(process(fetch()))
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(FROM_EMAIL, EMAIL_PASSWORD)
        smtp.send_message(msg)

schedule.every(10).seconds.do(send_email)

while True:
    schedule.run_pending()
    time.sleep(5)