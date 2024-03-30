from bs4 import BeautifulSoup
import requests

movies_web = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/").text
movies_soup = BeautifulSoup(movies_web, "html.parser")

movies_list = movies_soup.find_all(name="h3", class_="title")
titles_list = [movie.getText() for movie in movies_list]

with open("./movies.txt", mode="w") as movies:
    for index in range(len(titles_list)-1, -1, -1):
        title = titles_list[index]
        if index != 0:
            title += "\n"
        movies.write(title)

## bs syntax:

# if 'html.parser' can't read the website, try: 
    # import lxml
    # soup = BeautifulSoup(contents, "lxml")

# soup.find_all(name="a")
# soup.get("href") --> only returns the first item that meet the condition
# soupItem.getText()
# soup.find(name="h1", class_="heading", id="name") --> returns first one
# soup.select_one(selector=".heading p a")