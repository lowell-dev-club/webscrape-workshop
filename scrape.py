# import libraries
import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()

url = 'https://www.atomtickets.com/movies/avengers-endgame/284981'
response = http.request('GET', url)
soup = BeautifulSoup(response.data, 'html.parser')

showtimes_panel =  soup.find('div', attrs={'class': 'showtime-panel '})
print(showtimes_panel)

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