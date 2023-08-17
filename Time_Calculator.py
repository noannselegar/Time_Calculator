def add_time(start_time, duration, day=None):

    days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    AMPM = ('AM', 'PM')

    start_time = start_time.replace(':', ' ').split()
    duration = duration.split(':')
    tz = start_time[2]

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

    def Toggle(t):
        if t == 'AM': 
            t = 'PM'  
        else: 
            t = 'AM'
        return t

    howlong = HowLongFor(start_time[0], start_time[1], start_time[2])
    # print(howlong)

    startminutes = int(start_time[0])*60+int(start_time[1])
    durationminutes = int(duration[0])*60+int(duration[1])
    minutes = startminutes+durationminutes
    stop_hour = (minutes-(minutes%60))//60
    for i in range(stop_hour//12):
        if stop_hour > 12:
            stop_hour -= 12
    
    if durationminutes > howlong:
        daydiff = (durationminutes - howlong) // 720
        if daydiff < 2:
            whichday = '(Next day)'
        else:
            whichday = f'({int(daydiff)} days later)'
    else:
        daydiff = 0
        whichday = '(same day)'

    tzdiff = (durationminutes - howlong) / 360
    if durationminutes < howlong:
        tz = tz
    elif tzdiff < 1:
        tz = Toggle(tz)
    else:
        for _ in range(int(tzdiff)):
            tz = Toggle(tz)


    stop_string = f'{stop_hour}:{minutes%60:02d} {tz} {whichday}'
    print(stop_string)

            