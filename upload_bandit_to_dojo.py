import json
from defectdojo_api import defectdojo_apiv2 as defectdojo

# Replace these values with your actual DefectDojo instance details
DOJO_URL = 'https://your-defectdojo-instance.com'
API_KEY = 'your_api_key'
USERNAME = 'your_username'

# Initialize the DefectDojo API client
dd = defectdojo.DefectDojoAPIv2(
    dojo_url=DOJO_URL,
    api_key=API_KEY,
    user=USERNAME,
    verify_ssl=False
)

# Define the parameters for the import
engagement_id = 1  # Replace with your actual engagement ID
product_id = 1     # Replace with your actual product ID
scan_type = "Bandit Scan"
file_path = "bandit-report.json"

# Read the Bandit JSON report
with open(file_path, 'r') as file:
    report = file.read()

# Upload the Bandit report to DefectDojo
response = dd.upload_scan(
    engagement_id=engagement_id,
    scan_type=scan_type,
    file=report,
    product_id=product_id
)

if response.success:
    print("Scan uploaded successfully")
else:
    print(f"Failed to upload scan: {response.message}")
