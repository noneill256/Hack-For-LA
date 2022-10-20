from __future__ import print_function

from google.oauth2 import service_account
from googleapiclient.discovery import build
from github_api import CollectData
from datetime import datetime



startTime = datetime.now()
# authenticating credentials
service_acct_file = 'C:/Users/Noah/Coding/hack4la/projects_database/demo_key.json'
credentials = service_account.Credentials.from_service_account_file(
    filename = service_acct_file
    )

service_sheets = build('sheets', 'v4', credentials=credentials)
print(service_sheets)
# printing to see there's no error


# sheet specifications
google_sheets_id = '1LFResU_pcP5IMwz92dmPQRoKJ4lNa3tvr-_COJiE_hc'
worksheet_name = 'Sheet1!'


fulldf = CollectData() # collects the data
contrib_values = [(fulldf['num_of_contributors']).tolist()]
    # a Series can't be loaded into a sheet
    # AND the list must be 2-dimensional
update_values = [(fulldf['last_updated']).tolist()]

# where to insert the data
contrib_cell_range = 'Q2'
update_cell_range = 'P2'
contrib_value_range_body = {
    'majorDimension': 'COLUMNS',
    'values': contrib_values
   }
update_value_range_body = {
    'majorDimension': 'COLUMNS',
    'values': update_values
   }

# update the sheet!!!
# insert contributor data
service_sheets.spreadsheets().values().update(
    spreadsheetId = google_sheets_id,
    valueInputOption = 'USER_ENTERED',
    range = worksheet_name + contrib_cell_range,
    body = contrib_value_range_body
    ).execute()

# insert update data
service_sheets.spreadsheets().values().update(
    spreadsheetId = google_sheets_id,
    valueInputOption = 'USER_ENTERED',
    range = worksheet_name + update_cell_range,
    body = update_value_range_body
    ).execute()

print(f'runtime: {datetime.now() - startTime}')
