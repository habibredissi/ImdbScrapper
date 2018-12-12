from bs4 import BeautifulSoup
import requests
import urllib
import csv
source = requests.get('https://www.imdb.com/chart/top').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('imdb.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['title', 'year', 'rating', 'image'])


def importTopMovies():
    tab = soup.find('tbody', class_='lister-list')
    for movie in tab.find_all('tr'):
        try:
            title = movie.find('td', class_='titleColumn').a.text
            year = movie.find('span', class_='secondaryInfo').text
            rating = movie.find('td', class_='ratingColumn imdbRating').text
            image = movie.find('td', class_='posterColumn').a.img['src']
            csv_writer.writerow([title, year, rating, image])
        except Exception as e:
            raise ValueError('Error')


importTopMovies()
