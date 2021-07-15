import datetime
import sys


def calculate_time(_hour, _minute, _task, curr_time):
    current_hour = curr_time.split(":")[0]
    current_minute = curr_time.split(":")[1]

    #  Calculating current time
    now = datetime.datetime.now()
    now = now.replace(hour=int(current_hour), minute=int(current_minute))

    day = "today"

    if _task == "/bin/run_me_daily":
        if _hour == "*":
            _hour = now.hour
        if _minute == "*":
            _minute = now.minute

        if int(_hour) < now.hour:
            day = "tomorrow"
        if int(_hour) == now.hour and int(_minute) < now.minute:
            day = "tomorrow"

    elif _task == "/bin/run_me_hourly":
        if _minute == "*":
            _minute = now.minute

        if now.minute > int(_minute) and _hour == "*":
            _hour = (now.hour + 1) % 24
        else:
            _hour = now.hour

        if int(_hour) < now.hour:
            day = "tomorrow"

    elif _task == "/bin/run_me_every_minute":

        if _hour == "*":
            _hour = now.hour

        if now.hour > int(_hour) and _minute == "*":
            _minute = (now.minute + 1) % 59
        else:
            _minute = now.minute

        if int(_minute) < now.minute:
            day = "tomorrow"

    elif _task == "/bin/run_me_sixty_times":

        _minute = 00

        if int(_hour) < now.hour or (int(_hour) == now.hour and int(_minute) < now.minute):
            day = "tomorrow"

    result = str(_hour).zfill(2) + ":" + str(_minute).zfill(2) + " " + day + " - " + _task

    print(result)
    return result


def check_time(curr_time):
    try:
        datetime.datetime.strptime(curr_time, '%H:%M')


    except Exception as e:
        print("Given time is not in 24 hour - HH:MM format")
        raise Exception


if __name__ == '__main__':

    #  Getting new time input
    current_time = sys.argv[1]

    check_time(current_time)

    for i in iter(sys.stdin.readline, ''):

        minute = i.split()[0]
        hour = i.split()[1]
        task = i.split()[2]

        if hour != "*" and (int(hour) <= 0 or int(hour) >= 24):
            print("Error calculating hour at line : " + i)
            raise Exception

        if minute != "*" and (int(minute) <= 0 or int(minute) >= 59):
            print("Error calculating minute at line : " + i)
            raise Exception

        calculate_time(hour, minute, task, current_time)
