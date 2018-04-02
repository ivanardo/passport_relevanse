from datetime import date, datetime


def relevanse(dob="14.2.1998", passport="1.1.2012"):
    """dob - date of birthday"""
    dt_dob = datetime.strptime(dob, "%d.%m.%Y").date()
    dt_pas = datetime.strptime(passport, "%d.%m.%Y").date()
    today = date.today()

    # возраст
    age = today.year - dt_dob.year
    if today.month < dt_dob.month or (today.month == dt_dob.month and today.day < dt_dob.day):
        age -= 1

    # возраст при получении паспорта
    get_pass_age = dt_pas.year - dt_dob.year
    if dt_pas.month < dt_dob.month or (dt_pas.month == dt_dob.month and dt_pas.day < dt_dob.day):
        get_pass_age -= 1

    # Паспорт выдается в 14 лет и должен быть заменен в 20 и 45 лет, на замену паспорта дается 1 месяц.
    if 14 <= age < 20:
        if 14 <= get_pass_age < 20:
            print("паспорт действителен")
            return True
        elif (today.year*12+today.month) - ((dt_dob.year+14)*12 + dt_dob.month) <= 1:
            print("1 месяц на замену")
            return True
    elif 20 <= age < 45:
        if 20 <= get_pass_age < 45:
            print("паспорт действителен")
            return True
        elif (today.year*12+today.month) - ((dt_dob.year+20)*12 + dt_dob.month) <= 1:
            print("1 месяц на замену")
            return True
    elif age >= 45:
        if get_pass_age >= 45:
            print("паспорт действителен")
            return True
        elif (today.year*12+today.month) - ((dt_dob.year+20)*12 + dt_dob.month) <= 1:
            print("1 месяц на замену")
            return True

    print("паспорт недействителен")
    return False


if __name__ == '__main__':
    relevanse()
