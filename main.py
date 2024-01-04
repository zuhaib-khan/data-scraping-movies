import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
web_site_data = response.text
#print(web_site_data)

soup = BeautifulSoup(web_site_data, 'html.parser')

movie_titles = soup.find_all(name='h3', class_ = 'title')
movies_list = []
for title in movie_titles:
    movies_list.append(title.getText())
    
movies_list = movies_list[::-1]
print(movies_list)

with open('movies.txt', 'w', encoding='utf-8') as file:
    for movie in movies_list:
        
        file.write(f"{movie}\n")


