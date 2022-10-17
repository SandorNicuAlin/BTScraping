from apscheduler.schedulers.background import BackgroundScheduler
import requests

def job():
    r = requests.get('http://localhost:8000/scraping/bt')
    print(r.status_code)

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, 'interval', minutes=1)
    scheduler.start()