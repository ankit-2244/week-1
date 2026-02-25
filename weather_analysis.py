import statistics

# Weather data for Gandhinagar - Last 10 days
temperature = [32, 34, 33, 35, 36, 31, 30, 34, 33, 32]
humidity = [45, 50, 55, 60, 52, 48, 47, 53, 49, 51]

# Calculate average
avg_temp = sum(temperature) / len(temperature)
avg_humidity = sum(humidity) / len(humidity)

# Calculate median
median_temp = statistics.median(temperature)
median_humidity = statistics.median(humidity)

print("Temperature - Avg:", avg_temp)
print("Temperature - Median:", median_temp)
print("Humidity - Avg:", avg_humidity)
print("Humidity - Median:", median_humidity)
