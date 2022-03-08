import datetime


class Helper:

    def __init__(self):
        self.runningTallyOfAmount = 0

    def __create_reward_row(self, asset) -> list:
        """
        Removing a couple of zeros off of the unixtimestamp to get the date, because there seems to be too many.

        :param asset:
        :return:
        """
        return [str(asset[4])[0:-2],  # unix_timestamp
                datetime.datetime.fromtimestamp(int(str(asset[4])[0:-3])),  # created_date
                float(asset[11]) - self.runningTallyOfAmount]  # value

    def format_assets_and_remove_duplicates(self, assets) -> list:
        """
        Sometimes there are duplicate entries, we are keeping tracking of last updated value to determine if current
        entry is a duplicate or not.

        :param assets:
        :return: assets_filtered_by_unique_amount
        """
        assets_filtered_by_unique_amount = []
        for asset in assets:
            if self.runningTallyOfAmount != float(asset[11]):
                assets_filtered_by_unique_amount.append(self.__create_reward_row(asset))
                self.runningTallyOfAmount = float(asset[11])

        return assets_filtered_by_unique_amount
