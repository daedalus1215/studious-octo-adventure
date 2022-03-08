import csv
import datetime
import sys

import requests

# Parse the arguments
currentValue = sys.argv[1]
timestamp = sys.argv[2]
url = sys.argv[3]

# Fetch the data
res = requests.get(url).json()

# declare globals
runningTallyOfAmount = 0

assetsFilteredByUniqueAmount = list(filter(lambda asset: only_grab_entries_with_changed_amount(asset), res))


def only_grab_entries_with_changed_amount(asset) -> bool:
    """
    We only want to grab entries if the amount changed, because there are a lot of entries that have duplicate amounts

    :param asset: individual rewards
    :return: true if the rewards is unique
    """
    global runningTallyOfAmount
    if runningTallyOfAmount == float(asset[11]):
        return False
    else:
        runningTallyOfAmount = float(asset[11])
        return True


check = list(map(lambda x: create_reward_row(x), assetsFilteredByUniqueAmount))


def create_reward_row(entry) -> list:
    """
    Removing a couple of zeros off of the unixtimestamp to get the date, because there seems to be too many.

    :param entry:
    :return:
    """
    return [str(entry[4])[0:-2], datetime.datetime.fromtimestamp(int(str(entry[4])[0:-3])), float(entry[11])]


header_count = 0
with open('./studio-octo-adventure.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    for row in check:
        if header_count == 0:
            header_count = 1
            writer.writerow(['unix_timestamp', 'created_date', 'value'])
        writer.writerow(row)
