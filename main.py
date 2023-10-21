from datetime import date, datetime,timedelta


from datetime import datetime, timedelta, date

def get_birthdays_per_week(users):
    days = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": [], 'Saturday': [], 'Sunday': []}
    start_data = date.today()
    end_data = date.today() + timedelta(days=7)
    while start_data != end_data:
        for i in users:
            day = start_data.strftime('%A')
            start_data_ = start_data.strftime('%m-%d').split('-')
            end_data_ = i["birthday"].strftime('%m-%d').split('-')
            if start_data_ == end_data_ and i['name'] not in days[day] and day != 'Sunday' and day != 'Saturday':
                days.get(day, []).append(i['name'])
            if start_data_ == end_data_ and i['name'] not in days[day]:
                days.get('Monday', []).append(i['name'])
        start_data += timedelta(days=1)
    days.pop('Saturday')
    days.pop('Sunday')
    users = {i: j for i, j in days.items() if j}
    return users

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 10, 22).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
