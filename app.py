import csv
import datetime
import sys

import requests


class Reward:
    unix_timestamp = ''
    created_date = ''
    value = ''

    def __init__(self, unix_timestamp, date, value):
        self.unix_timestamp = unix_timestamp
        self.created_date = date
        self.value = value

    def __getitem__(self):
        return (dict({
            'unix_timestamp': self.unix_timestamp,
            'created_date': self.date,
            'amount': self.value
        }))

    currentValue = sys.argv[1]
    timestamp = sys.argv[2]
    url = sys.argv[3]

    res = requests.get(url).json()
    # print(res)
    # dt = datetime.datetime.fromtimestamp(0)
    # print(dt)
    # unix_conversion = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    # print(unix_conversion)
    # timestamp = round(datetime.datetime(2021, 12, 1).timestamp())

    print('timestamp:')
    print(timestamp)

    runningTallyOfAmount = 0

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

    assetFilteredByTimestamp = list(filter(lambda asset: only_grab_entries_with_changed_amount(asset), res))

    check = list(map(lambda x: Reward(str(x[4])[0:-2], datetime.datetime.fromtimestamp(int(str(x[4])[0:-3])),
                                      float(x[11]) - float(currentValue)),
                     assetFilteredByTimestamp))

    header_count = 0
    with open('./studio-octo-adventure.csv', 'w', encoding='UTF8', newline='') as f:
        # writer = csv.DictWriter(f, fieldnames=fieldnames = ['created_date', 'value'])
        writer.writeheader()
        writer.writerows()
    writer = csv.writer(f)
    writer.writerows(list(check))
    # list(forEach(lambda x: writer.writerow(print(str(x.created_date) + '  ' + str(x.value)), check)))

    f.close()
