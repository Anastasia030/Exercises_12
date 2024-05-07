class Date:
    """
    Date class
    """
    month = {1: 'янв', 2: 'фев', 3: 'мар', 4: 'апр', 5: 'май', 6: 'июн', 7: 'июл', 8: 'авг',
             9: 'сен', 10: 'окт', 11: 'ноя', 12: 'дек'}

    def __init__(self, date):
        """
        Initializes the date object
        :param date: str, a string containing the date in the standard format
        """
        if isinstance(date, str):
            year = int(date[6:])
            month = int(date[3:5])
            day = int(date[:2])
            if 1 <= day <= 31 and 1 <= month <= 12 and 0 < year and len(date[6:]) == 4:
                if (month == 2 and day <= 29 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) or
                        month == 2 and day <= 28 or (month in [4, 6, 9, 11] and day <= 30) or
                        (month in [1, 3, 5, 7, 8, 10, 12] and day <= 31)):
                    self.__date = date
                else:
                    print('ошибка')
                    self.__date = None
            else:
                print('ошибка')
                self.__date = None
        else:
            print('ошибка')
            self.__date = None

    @property
    def date(self):
        """
        Allows to create managed attributes (features)
        :return: str, the value of the instance attribute
        """
        return self.__date

    @date.setter
    def date(self, value):
        """
        Sets the valid value of the instance attribute
        :param value: str, a string containing the date in the standard format
        """
        if isinstance(value, str):
            year = int(value[6:])
            month = int(value[3:5])
            day = int(value[:2])
            if 1 <= day <= 31 and 1 <= month <= 12 and 0 < year and len(value[6:]) == 4:
                if (month == 2 and day <= 29 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) or
                        month == 2 and day <= 28 or
                        (month in [4, 6, 9, 11] and day <= 30) or
                        (month in [1, 3, 5, 7, 8, 10, 12] and day <= 31)):
                    self.__date = value

    @date.getter
    def date(self):
        """
        Sets the form in which the value of the instance attribute is returned
        :return: str, a string containing the date in the specified format
        """
        if self.__date is None:
            return None
        else:
            return f'{int(self.__date[:2])} {Date.month[int(self.__date[3:5])]} {self.__date[6:]} г.'

    def to_timestamp(self):
        """
        Counts the number of seconds elapsed between the set date and 01.01.1970
        :return: int, the number of seconds since 01.01.1970
        """
        SEC_DAY = 86400
        day = int(self.__date[:2])
        month = int(self.__date[3:5])
        year = int(self.__date[6:10])
        scnd_years = 0
        scnd_mnth = 0
        scnd_days = day * SEC_DAY
        nmbr_days_leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        nmbr_days_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            counter = 1
            while counter != month:
                scnd_mnth += (SEC_DAY * nmbr_days_leap_year[counter - 2])
                counter += 1
        else:
            counter = 1
            while counter != month:
                scnd_mnth += (SEC_DAY * nmbr_days_year[counter - 2])
                counter += 1

        for year in range(1971, year + 1):
            scnd_year = 0
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                for day in nmbr_days_leap_year:
                    scnd_year += (SEC_DAY * day)
            else:
                for day in nmbr_days_year:
                    scnd_year += (SEC_DAY * day)
            scnd_years += scnd_year

        all_seconds = scnd_years + scnd_mnth + scnd_days - SEC_DAY
        return all_seconds

    def __eq__(self, other):
        """
        Redefining the comparison operation: equality
        :param other: str, a string containing the date in the standard format
        :return: bool, the result of comparing two dates
        """
        return self.to_timestamp() == other.to_timestamp()

    def __lt__(self, other):
        """
        Redefining the comparison operation: less
        :param other: str, a string containing the date in the standard format
        :return: bool, the result of comparing two dates
        """
        return self.to_timestamp() < other.to_timestamp()

    def __ne__(self, other):
        """
        Redefining the comparison operation: inequality
        :param other: str, a string containing the date in the standard format
        :return: bool, the result of comparing two dates
        """
        return self.to_timestamp() != other.to_timestamp()

    def __le__(self, other):
        """
        Redefining the comparison operation: less than or equal to
        :param other: str, a string containing the date in the standard format
        :return: bool, the result of comparing two dates
        """
        return self.to_timestamp() <= other.to_timestamp()

    def __ge__(self, other):
        """
        Redefining the comparison operation: greater than or equal to
        :param other: str, a string containing the date in the standard format
        :return: bool, the result of comparing two dates
        """
        return self.to_timestamp() >= other.to_timestamp()

    def __gt__(self, other):
        """
        Redefining the comparison operation: more
        :param other: str, a string containing the date in the standard format
        :return: bool, the result of comparing two dates
        """
        return self.to_timestamp() > other.to_timestamp()

    def __repr__(self):
        """
        A string representation that is easy for the developer to read
        :return: str, a string containing the value of the instance attribute
        """
        if self.__date is None:
            print('ошибка')
        return f'{self.__date}'
