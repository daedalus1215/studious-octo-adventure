
import requests
import datetime
import sys


class Reward:
    date = ''
    value = ''

    def __init__(self, date, value):
        self.date = date
        self.value = value

currentValue = sys.argv[1]
timestamp = sys.argv[2]
url = sys.argv[3]

res = requests.get(url).json()
print(res)
# dt = datetime.datetime.fromtimestamp(0)
# print(dt)
# unix_conversion = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
# print(unix_conversion)
# timestamp = round(datetime.datetime(2021, 12, 1).timestamp())

print('timestamp:')
print(timestamp)

assetFilteredByTimestamp = list(filter(lambda asset: asset[4] > timestamp, res))

check = list(map(lambda x: Reward(x[4], x[11] - currentValue), assetFilteredByTimestamp))

print(check[0].date, check[0].value)




