import datetime
import requests
from time import sleep
from apscheduler.schedulers.background import BlockingScheduler


current_time = datetime.datetime.now()  # outputs in UTC


def send_message(val):
    json = {
        "content": val,
        # Embeds could go here, but I opted to keep it simple with just a message
    }
    print(json)
    webhookURL = 'REPLACE-URL-HERE'
    result = requests.post(webhookURL, json=json)
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))


# Set up scheduler
sched = BlockingScheduler()

if __name__ == '__main__':

# Set scheduled date/time in UTC (or whatever your local machine timezone is set to) and copy as much as needed. Can run in screen to keep alive if you disconnect from your terminal session

    sched.add_job(send_message,'date',run_date=datetime.datetime(2022, 12, 31, 5, 0, 0),args=['Happy New Year to everyone in part of Kiribati! :partying_face::partying_face::partying_face::confetti_ball::one::calendar_spiral::one::confetti_ball::partying_face::partying_face::partying_face:'])
    sched.add_job(send_message, 'date', run_date=datetime.datetime(2022, 12, 31, 6, 0, 0), args=[
        'Happy New Year to everyone in Samoa, Tokelau, Tonga, and the rest of Kiribati! :partying_face::partying_face::partying_face::confetti_ball::one::calendar_spiral::one::confetti_ball::partying_face::partying_face::partying_face:'])
    sched.add_job(send_message, 'date', run_date=datetime.datetime(2022, 12, 31, 6, 15, 0), args=[
        "Happy New Year to everyone in New Zealand's Chatham Islands! :partying_face::partying_face::partying_face::confetti_ball::one::calendar_spiral::one::confetti_ball::partying_face::partying_face::partying_face:"])
    sched.add_job(send_message, 'date', run_date=datetime.datetime(2022, 12, 31, 7, 0, 0), args=[
        "Happy New Year to everyone in Fiji, Marshall Islands, Nauru, Tuvalu, Wake Island, Wallis and Futuna, parts of Russa, and the rest of Kiribati and New Zealand! :partying_face::partying_face::partying_face::confetti_ball::one::calendar_spiral::one::confetti_ball::partying_face::partying_face::partying_face:"])
    
    sched.start()
