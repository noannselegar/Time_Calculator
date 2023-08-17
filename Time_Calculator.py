def add_time(start_time, duration, day=None):

    days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    AMPM = ('AM', 'PM')

    start_time = start_time.replace(':', ' ').split()
    duration = duration.split(':')

    def HowLongFor(st0, st1, st2):
        if st2 == 'PM':
            hourdif = 11 - int(st0)
            if st1 != '00':
                mindif = 60 - int(st1)
            else:
                mindif = 0
                hourdif += 1
        if st2 == 'AM':
            hourdif = 23 - int(st0)
            if st1 != '00':
                mindif = 60 - int(st1)
            else:
                mindif = 0
                hourdif += 1
        minut = hourdif*60 + mindif
        return minut

    def ToggleTZ(t, MinutesLeft, MinutesToComp):
        n = 0
        if MinutesToComp < MinutesLeft:
            return t
        elif MinutesToComp >= MinutesLeft:
            RealMinutes = MinutesToComp - MinutesLeft
            NumOfTog = RealMinutes//720
            if NumOfTog > 1:
                n += NumOfTog
            for _ in range(n+1):
                if t == 'AM': t = 'PM'
                else: t = 'AM'
            return t


    def ChangeDay(MinutesToComp, MinutesLeft):
        if MinutesToComp >= MinutesLeft:
            if (MinutesToComp-MinutesLeft) // 1440 < 1:
                return 'next day'
            if MinutesToComp // 1440 >= 1:
                for _ in range(MinutesToComp // 1440):
                    return f'{MinutesToComp // 1440+1} days later'
        else:
            return 'same day'

    def Hour(Min, Smin):
        M = Min+Smin
        h = (M-(M%60))//60
        if h > 12:
            for x in range(h//12):
                h -= 12
        return h
    
    howlong = HowLongFor(start_time[0], start_time[1], start_time[2])
    startminutes = int(start_time[0])*60+int(start_time[1])
    minutes = int(duration[0])*60+int(duration[1])
    stop_hour = Hour(minutes, startminutes)
    whichday = ChangeDay(minutes, howlong)
    tz = ToggleTZ(start_time[2], howlong, minutes)

    stop_string = f'{stop_hour}:{minutes%60:02d} {tz} {whichday}'
    print(stop_string)

            