def alarm_clock(day, vacation):
  if 1 <= day <= 5:
    weekday = True
  else:
    weekday = False
  if weekday == True and vacation == True:
    return '10:00'
  elif weekday == False and vacation == True:
    return 'off'
  elif weekday == True and vacation == False:
    return '7:00'
  else:
    return '10:00'