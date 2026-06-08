import os
import random
from slack_bolt import App
from dotenv import load_dotenv
from slack_bolt.adapter.socket_mode import SocketModeHandler

load_dotenv()

app = App(token=os.getenv('SLACK_APP_TOKEN'))


@app.message('/dsb-leuwen-ping')
def ping(ack,respond):
    ack()
    ping_response=['Hlo lil boy so, you just pinged me?','Sup, pinged me?',"let's gooooo, hlo"]
    reply = random.choice(ping_response)
    respond(reply)

@app.message('/dsb-leuwen-dev')
def dev(ack,respond):
    ack()
    response='''
    Hi, this bot is developed by a 15yo tech geek Ayush :)
'''
    respond(response)

if __name__ == "__main__":
    handler = SocketModeHandler(
        app,
        os.getenv("SLACK_APP_TOKEN")
    )
    handler.start()