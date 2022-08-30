def add_time(start, duration, day=''):
  week_days =['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
  start_am_pm = start.split()[1]
  start_min = int(start.split()[0].split(':')[0]) * 60 + int(start.split()[0].split(':')[1])
  dur_min = int(duration.split(':')[0]) * 60 + int(duration.split(':')[1])
  new_min = start_min + dur_min
  
  if start_am_pm == 'AM' and start.split()[0].split(':')[0] == '12':
    new_min -= 12 * 60

  elif start_am_pm == 'PM' and start.split()[0].split(':')[0] != '12':
    new_min += 12 * 60
  
  days_passed = new_min // (24 * 60)

  hour = (new_min % (24 * 60)) // 60
  minutes = (new_min % (24 * 60)) % 60
  am_pm = 'AM'
  
  if hour > 12:
    hour -= 12
    am_pm = 'PM'

  elif hour == 12:
    am_pm = 'PM'

  elif hour == 0:
    hour = 0

  if days_passed > 1:
    try:
      week_day = week_days[(week_days.index(day.lower().capitalize()) + days_passed) % 7]
      new_time = '{:0>2}:{:0>2} {}, {} ({} days later)'.format(str(hour), str(minutes), am_pm, week_day, days_passed)
  
    except:
      new_time = '{:0>2}:{:0>2} {} ({} days later)'.format(str(hour), str(minutes), am_pm, days_passed)

  elif days_passed == 1:
    try:
      week_day = week_days[(week_days.index(day.lower().capitalize()) + days_passed) % 7]
      new_time = '{:0>2}:{:0>2} {}, {} (next day)'.format(str(hour), str(minutes), am_pm, week_day)
  
    except:
      new_time = '{:0>2}:{:0>2} {} (next day)'.format(str(hour), str(minutes), am_pm)

  else:
    try:
      week_day = week_days[(week_days.index(day.lower().capitalize()) + days_passed) % 7]
      new_time = '{:0>2}:{:0>2} {}, {}'.format(str(hour), str(minutes), am_pm, week_day)
  
    except:
      new_time = '{:0>2}:{:0>2} {}'.format(str(hour), str(minutes), am_pm)
    
  return new_time

print(add_time("11:06 PM", "1:02"))
