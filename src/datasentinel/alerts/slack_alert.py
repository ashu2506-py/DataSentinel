import os

import requests


class SlackSender:

    def __init__(self):

        self.webhook = os.getenv("SLACK_WEBHOOK_URL")

    def send(
        self,
        dataset,
        passed,
        failed,
        anomalies,
        html,
        pdf,
    ):

        if not self.webhook:

            print("Slack webhook not configured.")

            return

        payload = {

            "text":

f"""
🛡️ *DataSentinel Validation Report*

📁 Dataset:
{dataset}

✅ Passed Rules : {passed}

❌ Failed Rules : {failed}

⚠️ Anomalies : {anomalies}

📄 HTML Report
{html}

📄 PDF Report
{pdf}
"""

        }

        response = requests.post(

            self.webhook,

            json=payload,

            timeout=10,

        )

        if response.status_code == 200:

            print("Slack notification sent.")

        else:

            print(

                f"Slack Error: {response.status_code}"

            )