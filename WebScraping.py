import requests
from bs4 import BeautifulSoup
import csv

page = requests.get("https://krittikaiitb.github.io/team/")

soup = BeautifulSoup(page.content, 'html.parser')

years = soup.find_all('div', attrs={"class": "card shadow-lg container mt-4 mb-5 aboutCard"})   #the set of all parent year elements


data = []
for year in years:
    for i in range(len(year.find_all('p', attrs={"class": "card-text"}))):       #no. of iterations = no. of club members in that year, which is derived from their designations in the html code
        row = []
        row.append(year.find_all('h5', attrs={"class": "card-title mb-0"})[i].get_text())     #appends the NAME of the club member
        row.append(year.find_all('p', attrs={"class": "card-text"})[i].get_text())            #appends the DESIGNATION of the club member
        row.append(year.find_all('p', attrs={"class": "display-4 pt-4 pb-4 text-center"})[0].get_text())    #appends the year
        data.append(row)

#converts data into a csv file
with open("Team.csv", "w", newline='') as file:
    info = csv.writer(file)
    info.writerows(data)