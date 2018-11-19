#!/usr/bin/python3
from pushbullet import Pushbullet
import requests

answer = requests.get('https://www.mysite.com/')
if answer.status_code != 200:
    pb = Pushbullet('o.BqIjZXrnfzj111111')
    push = pb.push_note("Сайт упал, просыпайся", "!!!")
