import requests
import json
import os

def upload_bandit_report():
    # DefectDojo instance details
    defectdojo_url = os.getenv('DEFECTDOJO_URL')
    api_key = os.getenv('DEFECTDOJO_API_KEY')
    engagement_id = os.getenv('DEFECTDOJO_ENGAGEMENT_ID')

    headers = {
        'Authorization': f'Token {api_key}',
        'Content-Type': 'application/json'
    }

    # Read Bandit report
    with open('bandit-report.json', 'r') as report_file:
        bandit_report = json.load(report_file)

    # Prepare payload for DefectDojo
    payload = {
        'engagement': engagement_id,
        'scan_type': 'Bandit Scan',
        'file': json.dumps(bandit_report),
        'tags': ['bandit', 'ci']
    }

    response = requests.post(
        f'{defectdojo_url}/api/v2/import-scan/',
        headers=headers,
        data=json.dumps(payload)
    )

    if response.status_code == 201:
        print('Report uploaded successfully.')
    else:
        print('Failed to upload report:', response.content)

if __name__ == '__main__':
    upload_bandit_report()
