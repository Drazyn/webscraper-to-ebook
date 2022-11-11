## Starting Configuration

MainPage_URL = "https://www.isekailunatic.com/tsuki-ga-michibiku-isekai-douchuu/"
EbookTitle = "Fourth Tome: Chapters 201-208"
EbookCover = "https://static.wikia.nocookie.net/tsukigamichibikuisekaidouchuu/images/1/18/TsukiMichi-LN-JP-v07-Cover.png"
minChapter = 201
maxChapter = 300

## Ending Configuration

import subprocess
import sys

import requests
from bs4 import BeautifulSoup

# let's create a function that will download all the content and export to html file.
def get_ebook_from_urls(urls, ebookTitle, ebookCover):
	
	file = open("output.html", "w+", encoding="utf-8")

	start = """<!DOCTYPE html>
	<html lang="pt-br">
		<head>
			<style>
				body {
					
				}
				h1 {
					text-align: center;
				}
				p {
					margin-top: 1rem;
					margin-bottom:1rem;
				}
			</style>
			<meta charset="UTF-8"/>
		</head>
		<body>"""
	file.write(start)
	
	for url in urls:
		page = requests.get(url)
		soup = BeautifulSoup(page.content, "html.parser")
		results = soup.find(id="primary")
  
		title = results.find_all("h1", class_="entry-title")[0].text
		chapter = title[8:11]

		file.write("<div><h2 class=\"chapter\">"+ title + "</h2><hr>")
		
		elements = results.find_all("div", class_="entry-content")
		paragraphs = []
		for element in elements:
			x = element.find_all('span')
			for y in x:
				paragraphs.append(f"<p>{y.text}</p>\n")
		paragraphs = paragraphs[2:]
  
		for line in paragraphs:
			file.write(line)
		
		file.write("</div>")


	file.write("</body></html>")

	file.close()
	subprocess.call(["ebook-convert",f'output.html',f'output.mobi', "--title", ebookTitle, "--cover", ebookCover])

page = requests.get(MainPage_URL)
soup = BeautifulSoup(page.content, "html.parser")

chaptersUrl = []

for a in soup.find_all('a', href=True):
	chapter = a.text
	url = a['href']
	
	if chapter[8:11].isdigit():
		if int(chapter[8:11]) >= minChapter and int(chapter[8:11]) <= maxChapter:
			chaptersUrl.append(url)

get_ebook_from_urls(chaptersUrl, EbookTitle, EbookCover)
