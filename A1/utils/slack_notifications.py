import os
import requests
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


#slack_token = os.getenv('SLACK_TOKEN')
client = WebClient(token="xoxb-5786642955568-5749504202295-x3jHIhWVjhHSiKaSxgmlHFxL")

#Give current json file path
allure_report_path = 'A1\reports\allure_result\bca8ff94-661e-4b44-aaac-603728fc748d-result.json'

#client = WebClient(token = "xoxb-5786642955568-5749504202295-x3jHIhWVjhHSiKaSxgmlHFxL") #or if not in a .env file, (token="xoxb-res_of_the_token")
result = client.chat_postMessage(channel='#projectone', text="Automation is Complete")



def send_slack_notification_with_attachment():
    try:
        with open("C:\\Users\\codoid\\PycharmProjects\\Python-Framework\\A1\\reporrt\\data\\test-cases\\963aa28ddd2b304a.json","rb") as fiel:
            response = client.files_upload(
            channels='#projectone',
            file=fiel,
            title='Allure Test Report',
            initial_comment='Here is the latest Allure test report.'
        )
        print("Slack notification sent successfully!")
    except SlackApiError as e:
        print("Error sending Slack notification:", e.response['error'])


send_slack_notification_with_attachment()
