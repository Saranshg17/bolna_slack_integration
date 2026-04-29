from django.shortcuts import render

# Create your views here.
import json
import os
import requests
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@csrf_exempt
@require_POST
def bolna_webhook(request):
    try:
        # Parse the JSON payload from Bolna
        payload = json.loads(request.body)
        print(payload)
        print(f"Received webhook from Bolna: {payload.get('id')}")

        # Bolna sends webhooks at various stages. We only want the alert when the call ends.
        if payload.get('status') != 'completed':
            return HttpResponse('Ignored: Call is not yet completed.', status=200)
        else:
            print("Call completed")

        # Extract the required fields
        call_id = payload.get('id', 'N/A')
        agent_id = payload.get('agent_id', 'N/A')
        transcript = payload.get('transcript', 'No transcript available.')
        
        # Duration might be at the root or nested in telephony_data
        telephony_data = payload.get('telephony_data', {})
        duration_from_telephony_data = telephony_data.get('duration', 'Unknown') if telephony_data is not None else 'Unknown'
        duration = payload.get('conversation_duration', duration_from_telephony_data)

        # Construct the Slack message payload using Slack's Block Kit
        slack_message = {
            "blocks": [
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": "📞 Bolna Call Ended",
                        "emoji": True
                    }
                },
                {
                    "type": "section",
                    "fields": [
                        {
                            "type": "mrkdwn",
                            "text": f"*Call ID:*\n{call_id}"
                        },
                        {
                            "type": "mrkdwn",
                            "text": f"*Agent ID:*\n{agent_id}"
                        },
                        {
                            "type": "mrkdwn",
                            "text": f"*Duration:*\n{duration} seconds"
                        }
                    ]
                },
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*Transcript:*\n_{transcript}_"
                    }
                }
            ]
        }

        # Send to Slack
        slack_url = os.environ.get('SLACK_WEBHOOK_URL')
        if slack_url:
            response = requests.post(slack_url, json=slack_message)
            response.raise_for_status()
            print('✅ Alert successfully sent to Slack.')
        else:
            print('⚠️ SLACK_WEBHOOK_URL is missing in the .env file.')

        # Acknowledge receipt to Bolna
        return HttpResponse('Webhook processed successfully', status=200)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        print(f'❌ Error processing webhook: {e}')
        return JsonResponse({'error': 'Internal Server Error'}, status=500)