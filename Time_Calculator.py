def add_time(start_time, duration, day=None):

  days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
          'Sunday')
  timezone = ('PM', 'AM')

  start_time, tz = start_time.split()
  start_time = [int(i) for i in start_time.split(':')]
  duration = [int(i) for i in duration.split(':')]
  tz_index = timezone.index(tz)
  if day != None:
    day = day.capitalize()


  start_min = start_time[0]*60 + start_time[1]
  duration_min = duration[0]*60 + duration[1]
  minutesLeft = (720 + (tz_index*720)) - start_min
  
  def ChangeDay(minutesLeft, duration_min, day=day):
    if day == None:
      if duration_min < minutesLeft:
        return ''
      elif minutesLeft + 1440 > duration_min > minutesLeft:
        return ' (next day)'
      else:
        d = (duration_min - minutesLeft) // 1440
        return f' ({d+1} days later)'
    else:
      day_index = days.index(day)
      d = (duration_min - minutesLeft) // 1440
      for _ in range(d+1):
        day_index += 1
        if day_index >= len(days):
          day_index = 0

      if duration_min < minutesLeft:
        return f', {days[day_index]}'
      elif minutesLeft + 1440 > duration_min > minutesLeft:
        return f', {days[day_index]} (next day)'
      else:
        return f', {days[day_index]} ({d+1} days later)'
      

  def Hour(start_min, duration_min, t=tz_index):
    M = start_min+duration_min
    h = (M-(M%60))//60
    m = M%60
    if h >= 12:
        for x in range(h//12):
            h -= 12
            t = t+1 if t == 0 else t-1
    if h == 0: 
        h = 12
    return h, m, t


  #stop_time = f'{(((start_min + duration_min) - (start_min + duration_min)%60)//60)}:{(start_min + duration_min)%60}' 
  h, m, t = Hour(start_min, duration_min)
  m = '{:02d}'.format(m)
  tz = timezone[t]
  d = ChangeDay(minutesLeft, duration_min)

  new_time = f'{h}:{m} {tz}{d}'       

  return new_time
