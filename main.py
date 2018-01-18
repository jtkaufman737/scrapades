import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.yangtse.com/')
soup = BeautifulSoup(r.text,'html.parser')
'''
//*[@id="main"]/div[2]/div[7] - main
 //*[@id="main"]/div[2]/div[7]/div[1] - box white
   //*[@id="main"]/div[2]/div[7]/div[1]/div[2] - box text
    //*[@id="main"]/div[2]/div[7]/div[1]/div[2]/div[1] title
    //*[@id="main"]/div[2]/div[7]/div[1]/div[2]/div[2] time
    //*[@id="main"]/div[2]/div[7]/div[1]/div[2]/div[3] text
'''

#print(r.text[0:500])
#print(soup)

results = soup.find_all('div', attrs={'class':'box white'})
results2 = soup.find_all('div', attrs={'class':'box2 white'})
#print(len(results) + len(results2))

first_result = results[0]
#print(first_result)
first_link=first_result.find('a').text
first_date=first_result.find('span').text
first_text=first_result.find('div',{'class':'box-text-text'}).text

#print(first_link)
#print(first_date)
#print(first_text)

'''
second_result = results2[0]
#print(first_result)
second_link=second_result.find('a').text
second_date=second_result.find('span').text
second_text=second_result.find('div',{'class':'box-text-text'}).text
'''

def news_stand(results,results2):
    while len(results + results2) <= 100: #Keeping it 100
        for x in range(0,len(results)):
            section1=results[x]
            print(
                'Title: ' + section1.find('a').text + '. '
                'Date: ' + section1.find('span').text + '. '
                'Article: ' + section1.find('div', {'class':'box-text-text'}).text + '. '
                )
        for y in range(0,len(results2)):
            section2=results2[y]
            print(
                'Title: ' + section2.find('div', {'class':'box2 name'})..text + '. '
                'Date: ' + 'Unlisted Date. '
                'Article: ' + section2.find('div', {'class':'box-text-text'}).text + '. '
                )
news_stand(results,results2)
