import requests
"""
Documentation at 
https://documenter.getpostman.com/view/10808728/SzS8rjbc
"""

# 1. get the API data from the web server
# This API server does not require an API key
# 2. Convert the data into a useful python objects: usually a list or dictionaries
url = "https://api.covid19api.com/summary"

#megan moore
response = requests.get(url)
data = response.json()
print(data)
print(type(data))
global_stats = data['Global']
print(type(global_stats))
deaths = global_stats['TotalDeaths']
print(type(deaths))
cases = global_stats['TotalConfirmed']
print(type(cases))
mortality_rate=deaths/cases
print(f"Total Deaths: {deaths:,}")
print(f"Total Confirmed Cases: {cases:,}")
print(f"Mortality Rate: {mortality_rate:.3f}")
