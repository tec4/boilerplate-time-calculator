# A bit sloppy. Have not gone through and cleaned up function
def add_time(start, duration, dayOfWeek = None):

    # Extract hour, minute and AM/PM from starting time
    startParts = start.split(' ')
    timeParts = startParts[0].split(':')
    partOfDay = startParts[1] # AM or PM
    currentHour = int(timeParts[0])
    currentMinute = int(timeParts[1])

    # Extract hour and minutes from duration
    durationParts = duration.split(':')
    hours = int(durationParts[0])
    minutes = int(durationParts[1])

    # Convert given hour to hour in 24 hour format
    hourOfDay = None
    if partOfDay == 'AM':
        hourOfDay = 0 if currentHour == 12 else currentHour
    else:
        hourOfDay = currentHour + 12

    # Add up minutes given, extract extra hours if over 60 minutes and compute 
    # the actul hours/minutes to add to the given time.
    addedMinutes = currentMinute + minutes
    minToHours = addedMinutes / 60
    minToHoursQuotent = minToHours // 1
    totalHours = hourOfDay + hours + (minToHours // 1)
    totalMinutes = int(addedMinutes - (minToHoursQuotent * 60))

    diffInDays = int(totalHours // 24)
    militaryTimeOfDay = int((totalHours - (diffInDays * 24)))
    amOrPm = 'AM' if militaryTimeOfDay < 12 else 'PM'

    newHourOfDay = 12 if militaryTimeOfDay == 0 else militaryTimeOfDay
    if newHourOfDay > 12:
      newHourOfDay = newHourOfDay - 12

    newDayOfWeek = None
    if dayOfWeek != None:
      lowerDayOfWeek = dayOfWeek.lower()
      daysOfWeek = [
          "monday",
          "tuesday",
          "wednesday",
          "thursday",
          "friday",
          "saturday",
          "sunday"
      ]

      curInx = daysOfWeek.index(lowerDayOfWeek)
      offsetInDays = diffInDays - ((diffInDays // 7) * 7)

      # if given offset would be greater than last item in array
      if offsetInDays + curInx > 6: 
          newDayOfWeek = daysOfWeek[offsetInDays - (len(daysOfWeek) - curInx)].capitalize()
      else: 
          newDayOfWeek = daysOfWeek[curInx + diffInDays].capitalize()

    newDayOfWeekStr = '' if newDayOfWeek == None else ', ' + newDayOfWeek

    diffInDaysStr = ''
    if diffInDays == 1:
        diffInDaysStr = ' (next day)'

    if diffInDays > 1:
        diffInDaysStr = ' (' + str(diffInDays) + ' days later)'

    return str(newHourOfDay) + ':' + str(totalMinutes).rjust(2, '0') + ' ' + amOrPm + newDayOfWeekStr + diffInDaysStr


# Initial implementation before finishing reading docs which
# says not to import any libraries...whoops
#
#def add_time(start, duration, dayOfWeek = None):
#    dtFormat = '%I:%M %p' if dayOfWeek == None else '%A %I:%M %p'
#    dtStr = start if dayOfWeek == None else dayOfWeek + ' ' + start
#    startDt = datetime.strptime(dtStr, dtFormat)
#
#    match = re.match('^([0-9]+):([0-9]+)$', duration)
#    if not match:
#        return None
#
#    hours = int(match.group(1))
#    minutes = int(match.group(2))
#    x = startDt + timedelta(hours=hours, minutes=minutes)
#    
#    extra = '' if dayOfWeek == None else ', %A'
#    dtStr = x.strftime('%-I:%M %p' + extra)
#
#    diffInDays = (
#        x.replace(hour=0, minute=0, second=0, microsecond=0) - 
#        startDt.replace(hour=0, minute=0, second=0, microsecond=0)
#    ).days
#
#    if diffInDays == 1:
#      dtStr = dtStr + ' (next day)'
#
#    if diffInDays > 1:
#      dtStr = dtStr + ' (' + str(diffInDays) + ' days later)'
#    
#    return dtStr
