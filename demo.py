from bs4 import BeautifulSoup
import urllib2

start = "http://en.wikipedia.org/wiki/Mandarin_Chinese"
end = "http://en.wikipedia.org/wiki/Thomas_the_Tank_Engine"

def getLinks(url):
    webpage = urllib2.urlopen(url)
    soup = BeautifulSoup(webpage)
    prefix = "http://en.wikipedia.org"
    return [prefix + l["href"] for l in soup.findAll("a", href=True)
            if l["href"].startswith("/wiki")]

def djk(start, end):
    visited = [start]
    curr = start
    toVisit = getLinks(start)
    while toVisit != []:
        curr = toVisit.pop(0)
        visited.append(curr)
        print curr
        if curr == end:
            return end
        toVisit += [link for link in getLinks(curr) if link not in visited]

print djk(start, end)
