import csv
import datetime
import sys

import requests

# Parse the arguments
from Helper import Helper

currentValue = sys.argv[1]
timestamp = sys.argv[2]
url = sys.argv[3]

# Fetch the data
res = requests.get(url).json()

# declare globals
runningTallyOfAmount = 0

helper = Helper()

assetsFilteredByUniqueAmount = helper.format_assets_and_remove_duplicates(res)

header_count = 0
with open('./studio-octo-adventure.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    for row in assetsFilteredByUniqueAmount:
        if header_count == 0:
            header_count = 1
            writer.writerow(['unix_timestamp', 'created_date', 'value'])
        writer.writerow(row)
