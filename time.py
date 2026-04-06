import time
t = time.strftime('%H:%M:%S', time.localtime())
hour = int(time.strftime('%H', time.localtime()))
print("Current Time:", t)

if hour >= 0 and hour < 12:
    print("Good Morning")
    
elif hour >= 12 and hour < 17:
    print("Good Afternoon")
elif hour >= 17 and hour < 19:
    print("Good Evening")
elif hour >= 19 and hour < 24:
    print("Good Night")
