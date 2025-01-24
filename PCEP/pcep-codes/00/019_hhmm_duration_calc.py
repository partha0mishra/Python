hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

mins += dura
hour += int(mins/60) # INT conversion is KEY
mins %= 60
hour %= 24

print("ETA: "+str(hour)+":"+str(mins))
# test data > output
# 12 17 59 > 13:16
# 23 58 642 > 10:40
# 0 1 2939 > 1:0