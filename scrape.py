# import libraries
from bs4 import BeautifulSoup as bs4
from requests import get

url = 'https://www.atomtickets.com/movies/avengers-endgame/284981'

# Request Page
r = get(url)
page = r.text

# Parse Page Data
soup = bs4(page, 'html.parser')

# Find the name of the theater
theater = soup.find('div', attrs={'class': 'venue-header__cell venue-header__cell--info venue-header__cell--padded'})
print(theater.text)

# showtimes_panel = soup.find('ul', attrs={'class': 'format-showtimes__list clearfix'})
# times = showtimes_panel.findChildren('li')
# for time in times:
# 	print(time.text)

showtimes_panel = soup.find_all('ul', attrs={'class': 'format-showtimes__list clearfix'})
'''
time_list = []

for i in showtimes_panel:
	times = i.findChildren('li')
	for time in times:
		time_stamp = time.text
		time_stamp = time_stamp[:-5]
		time_list.append(time_stamp)
'''
for i in showtimes_panel:
	times = i.findChildren('li')
	for time in times:
		print(time.text)
