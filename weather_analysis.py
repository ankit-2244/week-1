import statistics

# Weather data for Gandhinagar - Last 10 days
temperature = [32, 34, 33, 35, 36, 31, 30, 34, 33, 32]
humidity = [45, 50, 55, 60, 52, 48, 47, 53, 49, 51]
aqi = [110, 120, 115, 130, 125, 100, 95, 140, 135, 105]

# Average calculations
avg_temp = sum(temperature) / len(temperature)
avg_humidity = sum(humidity) / len(humidity)
avg_aqi = sum(aqi) / len(aqi)

# Median calculations
median_temp = statistics.median(temperature)
median_humidity = statistics.median(humidity)
median_aqi = statistics.median(aqi)

# Store results
results = f"""
Gandhinagar Weather Analysis (Last 10 Days)

Temperature -> Avg: {avg_temp}, Median: {median_temp}
Humidity -> Avg: {avg_humidity}, Median: {median_humidity}
AQI -> Avg: {avg_aqi}, Median: {median_aqi}
"""

print(results)

with open("results.txt", "w") as file:
    file.write(results)
