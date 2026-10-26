# Convert total seconds into hours, minutes, seconds.
total_seconds = int(input("Enter total seconds: "))
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds 
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)
