# import libraries
from bs4 import BeautifulSoup as bs4
from requests import get

url = 'https://www.atomtickets.com/movies/avengers-endgame/284981'

# Request Page
r = get(url)
page = r.text

# Parse Page Data
soup = bs4(page, 'html.parser')

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

# http = urllib3.PoolManager()

# # specify the url
# quote_page = 'https://www.fandango.com/avengers-endgame-2019-215871/movie-times'
# # for loop
# data = []
# # query the website and return the html to the variable 'page'
# page = http.request('GET', quote_page)
# # parse the html using beautiful soap and store in variable 'soup'
# soup = BeautifulSoup(page, 'html.parser')
# # Take out the <div> of name and get its value
# name_box = soup.find('section', attrs={'class': 'js-theaterShowtimes-loading theaters-lazy-load'})
# print(name_box)
# name = name_box.text.strip() # strip() is used to remove starting and trailing
# print(name)
# # # get the index price
# # price_box = soup.find('div', attrs={'class':'price'})
# # price = price_box.text
# # # save the data in tuple
# # data.append((name, price))
# print(data) 
