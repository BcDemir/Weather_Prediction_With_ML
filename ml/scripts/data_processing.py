import requests

with open('../../weather_API_secret.txt','r') as file:
    API_key = file.read()
    
lat = ''    
lon = ''
start = ''  # Start date (unix time, UTC time zone), e.g. start=1369728000
end = ''    # End date (unix time, UTC time zone), e.g. end=1369789200
    
# to be used to get live data
url = 'https://history.openweathermap.org/data/2.5/history/city?lat={lat}&lon={lon}&type=hour&start={start}&end={end}&appid={API_key}'