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
                return 'of the next day'
            if MinutesToComp // 1440 >= 1:
                for _ in range(MinutesToComp // 1440):
                    return f'({MinutesToComp // 1440+1} days later)'
        else:
            return 'of the same day'
        
    def WeekDay(firstDay, MinutesToComp, MinutesLeft):
        ind = days.index(firstDay)
        D = firstDay
        MSubDay = MinutesToComp // 1440
        if MinutesToComp >= MinutesLeft:
            if (MinutesToComp-MinutesLeft) // 1440 < 1:
                if ind == 7: ind = -1
                return days[ind+1]
            if MSubDay >= 1:
                for _ in range(MSubDay+1):
                    ind = ind+1
                    if ind >= 7: 
                        ind = -1    
                return days[ind]
        else:
            return D

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
    if day == None or day == '':
        whichday = ChangeDay(minutes, howlong)
    else:
        whichday = f'on {WeekDay(day, minutes, howlong)}'

    print(f'Check-out was at {stop_hour}:{(startminutes+minutes)%60:02d} {tz} {whichday}')
            