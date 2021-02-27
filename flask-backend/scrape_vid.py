import urllib.request
from bs4 import BeautifulSoup
import sys

query = "heart"

url = 'https://www.youtube.com/results?search_query=' + query



# Perform the request
request = urllib.request.Request(url)

request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
raw_response = urllib.request.urlopen(request).read()

# Read the repsonse as a utf-8 string
html = raw_response.decode("utf-8")

#print(html)


#FOR FINDING DEFINITION

# Construct the soup object
soup = BeautifulSoup(html, 'html.parser')

# Let's print the title to see if everything works

title = soup.title

divs = soup.select("#search a.yt-simple-endpoint")

print((divs))



"""
res = []
for div in divs:
    # For now just print the text contents.
    res.extend(div.find_all(text = 'src'))

print(res)
"""