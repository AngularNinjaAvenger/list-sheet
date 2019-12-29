#import re
#from selenium import webdriver
#url = ""
#chromedriver = 'C:/users/angular_nija_avenger/downloads/chromedriver'
##driver = webdriver.Chrome(chromedriver)
##browser  = driver.get(url)
#search = re.compile(r'<h3>(.*?)</h3>')
#res=search.search(driver.page_source)
#for i in res.group:
 #  print(i)
#search = re.compile(r'<li class="yoda"><a href="">') 
#return
import bs4,requests  
url = "https://surejob.in/captcha-entry-job-sites.html"
res = requests.get(url,{"accepts":"text/html"})
print(res)
soup = bs4.BeautifulSoup(res.text,'html.parser')
store = soup.select("h3")
print(store)
for i in store:
    print() 
    print()
    print(i)



