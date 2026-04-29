# **Bolna Slack Integration**


This is a simple Django service that listens for call events from Bolna and sends a clean, readable summary to Slack. Whenever a call is completed, the service captures the important details and posts them to a Slack channel so you don’t have to dig through logs or dashboards.

## **What it does**


The app exposes a webhook endpoint that Bolna can call. It ignores unnecessary or in-progress events and focuses only on completed calls. When a call finishes, it sends a nicely formatted message to Slack that includes the call ID, agent ID, duration, and the full transcript.
Everything is configurable using environment variables, so you don’t have to hardcode anything sensitive.


## **Tech stack**


This project is built using Django with Python. It uses Slack incoming webhooks to send messages and relies on the requests library for HTTP communication. Environment variables are handled using python-dotenv.

## **Requirements**


You’ll need Python 3.8 or above. You also need a Slack app with an incoming webhook URL and a Bolna account that can send webhook events to your server.

## **Setup instructions**


First, clone the repository and move into the project directory.

```bash
git clone https://github.com/Saranshg17/bolna_slack_integration.git
cd bolna_slack_integration
```

Create a virtual environment and activate it.

```bash
python -m venv venv
source venv/bin/activate
```

If you’re on Windows, use:
```bash
venv\Scripts\activate
```

Install the required dependencies.
```bash
pip install -r requirements.txt
```

Next, update the .env file in the root directory and add your Slack webhook URL.

If you plan to use the database, run migrations.
```bash
python manage.py migrate
```
Start the development server.
```bash
python manage.py runserver
```

## **Webhook configuration**


For this either you can create a new agent yourself or import using pre-existing template from 
d311e737-70e6-4075-bef6-c0ef3a7026b4
Set your Bolna webhook URL to point to:
http://<your-domain>/webhooks/bolna/
If you are testing locally, you can use a tool like ngrok to expose your local server to the internet.

## **Project structure**


The main logic lives inside the webhooks app. The views file handles parsing the Bolna payload and sending data to Slack. The URLs file defines the webhook route.
The main project folder contains settings and core configuration.

## **Expected payload**


The service expects a JSON payload from Bolna that includes the following fields:
status should be completed
id is the call identifier
agent_id is the agent identifier
transcript contains the conversation text
telephony_data may include duration details



## **Results**
![Bolna Setup](https://drive.google.com/file/d/1nSaJZ-BG5hdi5pTYIBEPFc5cz6UWVBTw/view?usp=sharing)

![Slack Alerts](https://drive.google.com/file/d/1q2fY3R5a7ogZBeh9e9sRV2Ta9PSrcKtd/view?usp=share_link)

![Bolna Call logs](https://drive.google.com/file/d/1p7GyP0Ck4cDetr2Xk7spDlAkoIEYGIRa/view?usp=sharing)

