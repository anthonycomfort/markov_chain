from bs4 import BeautifulSoup
import urllib2
import re

def createSoup(URL):
  response = urllib2.urlopen(URL)
  raw_html = response.read()
  soup = BeautifulSoup(raw_html, 'html.parser')
  new_soup = soup.find('div', {'class' : re.compile('post-content')})
  #creates a variable that contains all content within a div that has the string, 'post-content' in its name
  formatted_soup = ''.join(text for text in new_soup.find_all(text=True) if text.parent.name == 'p')
  #creates a variable that joins the text of all text tagged with 'p'- so, the content of the article
  updated_soup = re.sub('[^A-Za-z]+',' ', formatted_soup)
  #runs a regex on the text to get rid of special characters and numbers
  #Need to parse this into an array, find lengths of 1 and remove.
  return updated_soup
