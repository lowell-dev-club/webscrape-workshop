# import libraries
from bs4 import BeautifulSoup as bs4
from requests import get

url = 'https://www.atomtickets.com/movies/avengers-endgame/284981'

# Request Page
r = get(url)
page = r.text

# Parse Page Data
soup = bs4(page, 'html.parser')

theater = soup.find('div', attrs={'class': 'venue-header__cell venue-header__cell--info venue-header__cell--padded'})
print(theater.text)

showtimes_panel = soup.find_all('div', attrs={'class': 'format-showtimes clearfix'})
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
