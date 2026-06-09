import os
import random
from slack_bolt import App
from dotenv import load_dotenv
from slack_bolt.adapter.socket_mode import SocketModeHandler

load_dotenv('.env')

app = App(token=os.environ["SLACK_BOT_TOKEN"])


@app.command('/dsb-leuwen-ping')
def ping(ack,respond):
    ack()
    ping_response=[
        'Hlo lil boy so, you just pinged me?',
        'Sup, pinged me?',
        "let's gooooo, hlo"
    ]

    reply = random.choice(ping_response)
    respond(reply)

@app.command('/dsb-leuwen-dev')
def dev(ack,respond):
    ack()
   
    respond(block=[
        {
  "blocks": [
    {
      "type": "header",
      "text": {
        "type": "plain_text",
        "text": "👨‍💻 About Developer"
      }
    },
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "*Ayush* — a 15-year-old developer & builder 🚀\n\nI love turning ideas into real projects using code. Currently exploring *Python, C++, Flask, Web Dev & IoT (Arduino)*.\n\n💡 I enjoy building startups, hackathon projects, and AI-based systems that solve real problems.\n\n⚡ Always learning, always building, always improving."
      }
    },
    {
      "type": "divider"
    },
    {
      "type": "context",
      "elements": [
        {
          "type": "mrkdwn",
          "text": "🧠 Skills: Python | C++ | Arduino | Flask | HTML/CSS | Git & GitHub | DSA (learning)"
        }
      ]
    }
  ]
}
    ])


if __name__ == "__main__":
    handler = SocketModeHandler(
        app,
        os.environ["SLACK_APP_TOKEN"]
    )
    handler.start()