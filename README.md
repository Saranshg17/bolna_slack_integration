# Bolna Slack Integration

A Django-based webhook receiver that integrates Bolna call events with Slack. This service listens for completed call alerts from Bolna and sends a formatted summary (including transcript and metadata) to a designated Slack channel.

## 🚀 Features

- **Webhook Receiver**: Dedicated endpoint to receive POST requests from Bolna.
- **Call Filtering**: Automatically ignores intermediate events and only processes `completed` calls.
- **Rich Slack Notifications**: Uses Slack's Block Kit to send beautifully formatted messages containing:
  - Call ID
  - Agent ID
  - Conversation Duration
  - Full Transcript
- **Environment Driven**: Configurable via `.env` for security and flexibility.

## 🛠️ Tech Stack

- **Framework**: Django 5.x
- **Language**: Python 3.x
- **Communication**: Slack Incoming Webhooks
- **Library**: `requests` for HTTP calls, `python-dotenv` for config management.

## 📋 Prerequisites

- Python 3.8+
- A Slack App with an **Incoming Webhook** URL.
- A Bolna account configured to send webhooks to your server.

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/Saranshg17/bolna_slack_integration.git
cd bolna_slack_integration
```

### 2. Set up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Update `.env` file in the root directory and add your Slack Webhook URL

### 5. Run Migrations (Optional)
If you plan to use the database later:
```bash
python manage.py migrate
```

### 6. Start the Server
```bash
python manage.py runserver
```

## 🔗 Webhook Configuration

Point your Bolna webhook URL to:
`http://<your-domain>/webhooks/bolna/`

*Note: For local testing, use a tool like **ngrok** to expose your local server to the internet.*

## 📂 Project Structure

- `webhooks/`: Main application logic.
  - `views.py`: Contains the logic to parse Bolna payloads and post to Slack.
  - `urls.py`: Webhook endpoint routing.
- `bolna_slack_integration/`: Project settings and core configuration.

## 📝 Example Payload Processed

The service expects a JSON payload from Bolna with at least:
- `status`: "completed"
- `id`: Call Identifier
- `agent_id`: Agent Identifier
- `transcript`: Text of the conversation
- `telephony_data`: (Optional) contains duration info.

---
