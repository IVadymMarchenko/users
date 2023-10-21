from datetime import date, datetime,timedelta


from datetime import datetime, timedelta, date

def get_birthdays_per_week(users):
    days = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": [],'Saturday':[],'Sunday':[]}
    start_data = datetime.today()
    end_data=datetime.today()+timedelta(days=6)
    while start_data != end_data:
        for i in users:
            user_start=i["birthday"].strftime('%A %d %B %Y').split()[1:3]
            user_end=start_data.strftime('%A %d %B %Y').split()[1:3]
            day=start_data.strftime('%A %d %B %Y').split()[0]
            a=' '.join(user_start)
            b=' '.join(user_end)

            if a==b and i['name'] not in days[day] and day!='Sunday' and day!='Saturday':
                days.get(day,[]).append(i['name'])
            if user_start==user_end and i['name'] not in days[day]:
                days.get('Monday',[]).append(i['name'])


        start_data += timedelta(days=1)
    days.pop('Saturday')
    days.pop('Sunday')
    users={i:j for i , j in days.items() if j}
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