#!/bin/python3

from twitchAPI.twitch import Twitch
from twitchAPI.helper import first
import asyncio
import os

app_id = os.getenv("APP_ID")
app_secret = os.getenv("APP_SECRET")
tw_user = os.getenv('TWITCH_USER')

print(app_id)
print(app_secret)
print(tw_user)

async def twitch_example():
    # initialize the twitch instance, this will by default also create a app authentication for you
    twitch = await Twitch(app_id, app_secret)
    print(twitch)
    # call the API for the data of your twitch user
    # this returns a async generator that can be used to iterate over all results
    # but we are just interested in the first result
    # using the first helper makes this easy.
    user = await first(twitch.get_users(logins=tw_user))
    print(user)
    # print the ID of your user or do whatever else you want with it
    print(user.id)

# run this example
asyncio.run(twitch_example())
