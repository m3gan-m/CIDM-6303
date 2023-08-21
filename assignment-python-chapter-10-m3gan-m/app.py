import requests
#megan Moore 
#Chapter 10.2 - Pip
#if not installed, install the requests package from
#a terminal using pip or pip3 for mac.
#pip install requests
#pip3 install requests
response = requests.get("http://google.com")
print(response)
print(response.url)
#displays the html text returned by the web server
print(response.text)
