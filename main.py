import random
from datetime import datetime, timedelta
import re


def get_days_from_today(date):
    pattern = r"[;,\-:!\./]"
    change = "."
    text = re.sub(pattern, change, date)
    format = datetime.strptime(text, "%Y.%m.%d")
    result = format - datetime.now()
    result = result.days
    if result < 0:
        return result
    else:
        return result


def get_numbers_ticket(min, max, quantity):
    try:
        minA = int(min)
        maxB = int(max)
        quantityC = int(quantity)
        list = []
        for index in range(minA, maxB + 1):
            list.append(index)
        result = random.sample(list, quantityC)
        return sorted(result)
    except:
        print(TypeError("Only integers are allowed"))


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5467\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]


def normalize_phone(phone_number):
    pettern1 = r"\D"
    matches = re.sub(pettern1, "", phone_number)
    checkNumber = bool(re.search(r"^380\d{9}$", matches))
    checkNum = bool(re.search(r"^0\d{9}$", matches))
    if checkNumber:
        return "+" + matches
    elif checkNum:
        return "+38" + matches
    else:
        TypeError("the number format is not correct")


result = [normalize_phone(num) for num in raw_numbers]



def get_upcoming_birthdays(users):
    lists = list()
    for user in users:
        patternValue = r"[\W\;,\-:!\.\_]"
        parseValue1 = re.sub(patternValue, " ", user.values().__str__())
        pattern = r'(\w+\s\w+)\s+(\w+\s\w+)\s+(\d+\s\d+\s\d+)'
        parseOnGroup = re.search(pattern, parseValue1.__str__())
        parseUserName = parseOnGroup.group(2)
        parseYear = parseOnGroup.group(3)
        yearNormal = re.sub(r"(\d{4})\s(\d{2})\s(\d{2})",
                            r"\1.\2.\3",
                            parseYear.__str__()).strip()
        yearDateUserFormat = datetime.strptime(yearNormal,"%Y.%M.%d").date()
        defaultDate = datetime.strptime("2024.01.22","%Y.%m.%d").date()
        dateHappyBirthday = defaultDate + timedelta(days=abs(defaultDate.day - yearDateUserFormat.day))
        if dateHappyBirthday.isoweekday() == 6:
           dateHappyBirthday = dateHappyBirthday + timedelta(days=2)
           lists.append({"name" : parseUserName, "congratulation_date" : dateHappyBirthday.__str__() })
        elif dateHappyBirthday.isoweekday() == 7:
            dateHappyBirthday = dateHappyBirthday + timedelta(days=1)
            lists.append({"name": parseUserName, "congratulation_date": dateHappyBirthday.isoformat().__str__()})
        else:
            lists.append({"name": parseUserName, "congratulation_date": dateHappyBirthday.isoformat().__str__()})
    print(lists)

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

get_upcoming_birthdays(users)
