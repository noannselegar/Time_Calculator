def add_time(start_time, duration, day=None):

    days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    AMPM = ('AM', 'PM')

    start_time = start_time.replace(':', ' ').split()
    duration = duration.split(':')

    def HowLongFor(hrs, min, timezone):
        if timezone == 'PM':
            hourdif = 11 - int(hrs)
            if min != '00':
                mindif = 60 - int(min)
            else:
                mindif = 0
                hourdif += 1
        if timezone == 'AM':
            hourdif = 23 - int(hrs)
            if min != '00':
                mindif = 60 - int(min)
            else:
                mindif = 0
                hourdif += 1
        minut = hourdif*60 + mindif
        return minut
      
    def Toggle(tt):
        if tt == 'AM': 
            tt = 'PM'
        else: 
            tt = 'AM'
        return tt

    def ChangeDay(MinutesToComp, MinutesLeft):
        if MinutesToComp >= MinutesLeft:
            if (MinutesToComp-MinutesLeft) // 1440 < 1:
                return 'next day'
            if MinutesToComp // 1440 >= 1:
                for _ in range(MinutesToComp // 1440):
                    return f'{MinutesToComp // 1440+1} days later'
        else:
            return 'same day'

    def Hour(Min, Smin, t):
        M = Min+Smin
        h = (M-(M%60))//60
        if h >= 12:
            for x in range(h//12):
                h -= 12
                t = Toggle(t)
        if h == 0: 
            h = 12
        return h, t
    
    howlong = HowLongFor(start_time[0], start_time[1], start_time[2])
    startminutes = int(start_time[0])*60+int(start_time[1])
    minutes = int(duration[0])*60+int(duration[1])
    stop_hour, tz = Hour(minutes, startminutes, start_time[2])
    whichday = ChangeDay(minutes, howlong)

    stop_string = f'{stop_hour}:{(startminutes+minutes)%60:02d} {tz} {whichday}'
    print(stop_string)
    print(howlong, minutes)
            