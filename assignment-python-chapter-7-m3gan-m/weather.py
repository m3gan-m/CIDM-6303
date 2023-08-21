# Follow the instructions for coding a weather app
#megan moore
daily_high_temperature = [62,64,79,52,46,50,58,66,71,77,78,78,76,79,77]
daily_low_temperature = [42,48,47,24,28,28,32,37,43,46,48,47,48,49,50]
humidity = [0.48,0.53,0.46,0.44,0.4,0.6,0.58,0.5,0.48,0.43,0.41,0.39,0.39,0.38,0.4]

high_temp = max(daily_high_temperature)
low_temp = min(daily_low_temperature)
avg_hightemp = sum(daily_high_temperature)/len(daily_high_temperature)
avg_lowtemp = sum(daily_low_temperature)/len(daily_low_temperature)
avg_humidity = sum(humidity)/len(humidity)

"""print(high_temp)
print(low_temp)
print("%.0f" % avg_hightemp)
print("%.0f" % avg_lowtemp)
print("%.2f" % avg_humidity)
"""


print(f"Weather forecast for the next 15 days:")
print(f"The average high will be {avg_hightemp:.0f} and the average low will be {avg_lowtemp:.0f}.")
print(f"The highest temperature will be {high_temp:.0f}. The lowest temperature will be {low_temp:.0f}.")
print(f"The average humidity will be {avg_humidity:.2f}.")
print("-"*20)
