import time

def displayCurrentTime():
    currentTime = time.time()

    totalSeconds = int(currentTime)

    currentSecond = totalSeconds % 60

    totalMinutes = totalSeconds // 60

    currentMinute = totalMinutes % 60

    totalHours = totalMinutes // 60

    currentHour = totalHours % 24

    return str(currentHour) + ":" + str(currentMinute) + ":" + str(currentSecond)

print("Current time: "+displayCurrentTime())

