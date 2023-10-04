import requests, bs4

# res = requests.get('https://nostarch.com')
# res.raise_for_status()
# noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
# print(noStarchSoup)
# print(type(noStarchSoup)) # <class 'bs4.BeautifulSoup'>

res_weather = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.78873500000003&lon=-122.3945')
res_weather.raise_for_status()
weather_soup = bs4.BeautifulSoup(res_weather.text, 'html.parser')
summary=weather_soup.select('h1')
# print(summary)
# [<h1 style="font-size: 11pt;">Severe Weather for the Plains; Record Warmth for the Great Lakes and Northeast</h1>]
# print(weather_soup.select('h1 + p'))
# [<p>
#             Thunderstorms, associated with large hail, wind damage, a few tornadoes alongside the chance of excessive rainfall, are expected this afternoon and evening across parts of the Great Plains. For the eastern shores of Florida, dangerous surf and rip currents are expected with a persistent onshore flow through today. Record high temperatures from the Great Lakes to the Northeast are expected today.  
#             <a href="http://www.wpc.ncep.noaa.gov/discussions/hpcdiscussions.php?disc=pmdspd" target="_blank">Read More &gt;</a>
# </p>]

# print(str(summary[0])) # <h1 style="font-size: 11pt;">Severe Weather for the Plains; Record Warmth for the Great Lakes and Northeast</h1>
# print(summary[0].getText()) # Severe Weather for the Plains; Record Warmth for the Great Lakes and Northeast
# print(summary[0].attrs) # {'style': 'font-size: 11pt;'}
# print(summary[0].get('style')) # font-size: 11pt;
print(summary[0].get('nonexistentAttr')) # None