<p align="center">
  <img src="assets/banner.png" alt="Slack Bot Banner" width="100%">
</p>

# 🤖 Hack Club Slack Bot

A feature-rich and interactive Slack bot built using the **Slack Bolt for Python** framework and run via **Socket Mode**. This bot is live in the [Hack Club Slack](https://hackclub.com/slack/) server and is deployed on **NEST** (Hack Club's custom server environment).

---

## 🚀 Live on Hack Club Slack!

This bot is fully deployed and active on the Hack Club Slack server. You can interact with it using Slack slash commands.
* **Hosted on:** [NEST](https://nest.hackclub.com) (Hack Club's hosting platform for club members)
* **Framework:** Python Slack Bolt SDK (Socket Mode)

---

## ✨ Features & Commands

The bot supports the following commands:

### 1. `/dsb-leuwen-ping`
A fun command that responds with one of several random playful greetings to check if the bot is alive.
* **Sample responses:**
  * *"Hlo lil boy so, you just pinged me?"*
  * *"Sup, pinged me?"*
  * *"let's gooooo, hlo"*

### 2. `/dsb-leuwen-dev`
An interactive command that leverages **Slack Block Kit** to display details about the developer behind this bot. It renders a rich container containing:
* Developer intro (Ayush, a 15-year-old developer & builder 🚀)
* Tech interests (Python, C++, Flask, Web Dev, IoT/Arduino)
* Skill badges (Python | C++ | Arduino | Flask | HTML/CSS | Git & GitHub | DSA)

### 3. `/dsb-leuwen-matrix`
Generates and displays a random $3 \times 3$ integer matrix with values between 0 and 99 formatted inside a code block.

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Framework:** [Slack Bolt for Python](https://slack.dev/bolt-python/concepts)
* **Connection Mode:** Socket Mode (enables real-time communication without setting up a public HTTP endpoint/tunnel)
* **Configuration:** dotenv (for local credential management)

---

## 📦 Setup & Local Development

To run this bot locally, follow these steps:

### 1. Prerequisites
Ensure you have Python 3.9+ installed.

### 2. Clone the Repository
```bash
git clone https://github.com/your-username/Hackclub-slack-bot.git
cd Hackclub-slack-bot
```

### 3. Create a Virtual Environment (Optional but recommended)
```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables
Copy `.env.template` to a new file named `.env`:
```bash
cp .env.template .env
```
Fill in your Slack API credentials in the `.env` file:
```env
SLACK_BOT_TOKEN=xoxb-your-bot-token
SLACK_APP_TOKEN=xapp-your-app-token
```
> **Note:** To use Socket Mode, ensure **Socket Mode** is enabled in your Slack App settings, and your App Token (`xapp-...`) has the `connections:write` scope.

### 6. Run the Bot
```bash
python app.py
```

---

## 🌐 Deployment on NEST

This bot is configured to run continuously on **NEST** using a process manager (such as `pm2` or systemd).

To keep the bot running in the background on NEST:
1. SSH into your NEST environment.
2. Clone the repository and configure the `.env` file.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the app using a process manager (e.g. using `nohup` or `pm2` if node is installed):
   ```bash
   nohup python app.py > bot.log 2>&1 &
   ```
   *Or using `screen`/`tmux`:*
   ```bash
   screen -S slack-bot python app.py
   ```

---

## 👨‍💻 Developer Info

Created and maintained by **Ayush** — a 15-year-old developer & startup/AI builder.
Feel free to connect or ask questions in the Hack Club Slack!