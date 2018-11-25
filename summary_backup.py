from bs4 import BeautifulSoup
import urllib.request


#source_code = """<span class="UserName"><a href="#">Martin Elias</a></span>"""
#soup = BeautifulSoup(source_code, "lxml")
#print(soup.a.string)
#print soup.find('span',{'class':'UserName'}).text

opener = urllib.request.FancyURLopener({})
baseurl = "https://www.redpillreligion.com/page/"

# Get the total number of Red Pill Religion pages

f = opener.open("https://www.redpillreligion.com/")
content = f.read()
soup = BeautifulSoup(content, "lxml")
pageNumbers = soup.findAll('a', {'class':'page-numbers'})
numpages = int(pageNumbers[-2].text.split()[1])

# Iterate through Red Pill Religion pages
for x in range(1,numpages + 1):
	url = baseurl + str(x)
	f = opener.open(url)
	content = f.read()
	soup = BeautifulSoup(content, "lxml")

	# Get the Red Pill Religion articles
	articles = soup.findAll('article')

	# Get the metadata of each article
	for article in articles:
		title = ''
		link = ''
		footer = ''
		author = ''
		date = ''
		category = ''
		try:
			entry = article.find('div', {'class':'entry-content'}).text
			h2 = article.find('h2', {'class':'entry-title'})
			title = h2.text
			link = h2.find('a').get('href')
			footer = article.find('footer')
			author = footer.find('a', {'class':'url fn n'}).text
			date = footer.find('time', {'class':'entry-date'}).text
			category = footer.find('a', {'rel':'category'}).text			

		except:
			title = ''
			link = ''
			footer = ''
			author = ''
			date = ''
			category = ''

		# Print article summary
		print("Title: " + title)
		print("Author: " + author)
		print("Link: " + link)
		print("Category: " + category)
		print("Date: " + date)
		print("Entry: " + entry)
		print("------------------------------------------------------")
