# Read the command line arguments from sys.argv.
# Fetch the search result page with the requests module.
# Find the links to each search result.
# Call the webbrowser.open() function to open the web browser.

#! python3
# lucky.py - opens several google search results

import sys, requests, bs4, webbrowser

print('Googling...')
#res = requests.get('https://google.com/search?q=' + '+'.join(sys.argv[1:]))
res = requests.get('https://google.com/search?q=' + '+'.join(['python', 'programming', 'tutorials']))

# retrieve top search result links
soup = bs4.BeautifulSoup(res.text, "html.parser")

# open a browser tab for each result
#linkElems = soup.select('.g a')
linkElems = soup.select('.kCrYT a')
##for link in linkElems:
##    print(link)
numOpen = min(5, len(linkElems))

for i in range(numOpen):
    #print(linkElems[i].get('href'))
    webbrowser.open('https://google.com' + linkElems[i].get('href'))
