

# username for my GitHub account: David Ortiz
# other username for GitHub account: davidortiz336
#should return a link for the profile image to that account

import requests
from bs4 import BeautifulSoup as bs


github_user = input("Input GitHub User: ")

#sending a request to url: https://github.com/davidortiz336
url = "https://github.com/"+github_user
r = requests.get(url)
soup = bs(r.content, 'html.parser')
profile_image = soup.find('img', {'alt' : 'Avatar'})['src']# gets an image tag with a 
print(profile_image)






