import calendar
import csv
import datetime
import os

from collections import Counter

# change directory
path = 'D:\Programming\Python\Xtern-Data-Science-Screen'
os.chdir(path)

# read checkin_dataset.csv
with open('checkin_dataset.csv', 'r') as file :
    csv_reader = csv.reader(file)

    users = []

    # count the number of users
    for row in csv_reader :
        if(row[1]) not in users and row[1] != 'user':
            users.append(row[1])
    users = sorted(users)

    # number of users
    print('Number of users: ' + str(len(users)))

    file.close()

""" 
    what can we look for that tells us more about the users?
        -- what days people are most active
        -- what locations people are most active in
"""

with open('checkin_dataset.csv', 'r') as file :
    csv_reader = csv.reader(file)
    # make dictionary with users and their timestamps
    times = {}
    coordinate_dict = {}

    for row in csv_reader :

        clock_time = row[2]
        # make dictionary where each user has a list of their active times
        if row[1] in times.keys() :
            times[row[1]].append(clock_time)
        else :
            times[row[1]] = []

        # make dictionary where each user has list of all their coordinates
        # coordinates are tuples of x and y coordinates respectively, and are rounded since we
        # will just need a general location
        if row[3] != 'xcoordinate' :
            coordinates = (round(float(row[3]), 2), round(float(row[4]), 2))
            if row[1] in coordinate_dict.keys() :
                coordinate_dict[row[1]].append(coordinates)
            else :
                coordinate_dict[row[1]] = []

    active_days = {}
    # make dictionary containing the number of users active on each day
    for key, values in times.items() :
        for value in values :
            day = value[:10]
            if day in active_days.keys() :
                active_days[day] += 1
            else :
                active_days[day] = 0

    # This prints out day-to-day user activity
    for key in sorted(active_days.keys()) :
        # compile the date in datetime so we can print out the actual weekdays -- this will help
        # determine which days of the week the users are most active, which could be useful for
        # implementing features of the OS
        date = datetime.date(int(key[0:4]), int(key[5:7]), int(key[8:10]))
        weekday = list(calendar.day_abbr)[int(date.strftime('%w'))]
        print(key + ' (' + weekday + '): '+ str(active_days[key]))

    # Features of the OS could be customized for a person's mode location (i.e. where they are most often)
    for key in sorted(coordinate_dict.keys()) :
        # find most common coordinates, print it out for each user
        data = Counter(coordinate_dict[key])
        print('User ' + key + ': ' + str(data.most_common(1)))
