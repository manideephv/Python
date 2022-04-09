from bs4 import BeautifulSoup
import requests
import pandas as pd


try:
    source = requests.get('https://www.imdb.com/chart/top/')
    source.raise_for_status()

    soup = BeautifulSoup(source.text,'html.parser')

    movies = soup.find('tbody', class_="lister-list").find_all('tr')

    movieList = []

    for movie in movies:

        #name = movie.find('td', class_="titleColumn").a.text

        movie_info = movie.find('td', class_="titleColumn").get_text(strip=True)

        rank = movie_info.split('.')[0]
        name = movie_info[movie_info.find('.'):movie_info.find('(')][1:]
        year = movie_info[movie_info.find('('):movie_info.find(')')][1:]
        
        #year = movie.find('td', class_="titleColumn").span.text.strip('()')

        rating = movie.find('td', class_="ratingColumn imdbRating").strong.text

        #print(rank,name,year, rating)
        
        movieList.append([rank,name,year, rating])

    df = pd.DataFrame(movieList, columns = ['Rank', 'Name', 'Year', 'Rating'])
    df.to_csv('Top 250 IMDB Movies.csv', index=False)
    print("CSV Created!")

except Exception as e:
    print(e)