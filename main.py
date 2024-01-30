from instagrapi import Client
from instagrapi.exceptions import LoginRequired
import logging
import time
from datetime import datetime, timedelta
import pytz

USERNAME = ""
PASSWORD = ""

logger = logging.getLogger()
cl = Client()

def login_user():
    session = cl.load_settings("session.json")
    login_via_session = False
    login_via_pw = False

    if session:
        try:
            cl.set_settings(session)
            cl.login(USERNAME, PASSWORD)

            # check if session is valid
            try:
                cl.get_timeline_feed()
            except LoginRequired:
                logger.info("Session is invalid, need to login via username and password")

                old_session = cl.get_settings()

                # use the same device uuids across logins
                cl.set_settings({})
                cl.set_uuids(old_session["uuids"])

                cl.login(USERNAME, PASSWORD)
            login_via_session = True
        except Exception as e:
            logger.info("Couldn't login user using session information: %s" % e)

    if not login_via_session:
        try:
            logger.info("Attempting to login via username and password. username: %s" % USERNAME)
            if cl.login(USERNAME, PASSWORD):
                login_via_pw = True
        except Exception as e:
            logger.info("Couldn't login user using username and password: %s" % e)

    if not login_via_pw and not login_via_session:
        raise Exception("Couldn't log in user with either password or session")
    print("Logged in successfully")

login_user()
time_bet = [60*5]
index = 0
while True :
    dt1 = datetime.now()
    dt2 = datetime(year=2024, month=1, day=1, hour=0)
    difference = dt2-dt1
    sec = difference.total_seconds()
    print_text = str(int(sec//3600)) + " 𝙷𝚛𝚜 " + str(int((sec/3600-sec//3600)*60))+ " 𝙼𝚒𝚗\n 𝒕𝒐 𝑯𝑵𝒀🎉⌚\n 𝑭𝒓𝒐𝒎 🤖🇹🇭"
    print(print_text)
    try:
       cl.create_note(print_text, 0)
    except Exception as e:
        print("Noted Successs mung")
    time.sleep(time_bet[index%len(time_bet)])
    index +=1


     