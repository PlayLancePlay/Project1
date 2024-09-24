# Version 1
# Stage 1
num_showers = int(input("Enter the number of showers you take per week: "))
avg_shower_time = int(input("how long your average showers are:"))

# Stage 2
WATER_USAGE_PER_MINUTE = 2 # gallons per minute
Total_water_usage = num_showers *avg_shower_time * WATER_USAGE_PER_MINUTE

# Stage 3 
print("In a week, you use", Total_water_usage, "gallons of water for shower") # Output: In a week, you use 140 gallons of water for shower 
# Stage 4 
# It help other people to make sure that they don't use water too much.