import schedule
import time
from cybercrow_agent import run

schedule.every().day.at("08:00").do(run)

while True:
    schedule.run_pending()
    time.sleep(60)
