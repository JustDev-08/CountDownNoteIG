from instagrapi import Client
cl = Client()
USERNAME = ""
PASSWORD = ""
cl.login(USERNAME, PASSWORD)
cl.dump_settings('session.json')