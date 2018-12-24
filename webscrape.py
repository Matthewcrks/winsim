from bs4 import BeautifulSoup





soup = BeautifulSoup(, 'html.parser')


#Select things directly
print(soup.body)
print(soup.head)
print(soup.head.title)


#find()
# gives you only the first one it finds
el = soup.find('div')



#find_all() or findAll()

el = soup.find_all('div')[1]
# ^ addresses a specific index of the list so would only give you the 2nd listed div


el=soup.find(id='section-1')
el=soup.find(class_='items')
el = soup.find(attrs={"data-hello": "hi"}) 


#select
el = soup.select('.item')[0]



#get_text()
el = soup.find(class_='item').get_text()


#loop thru items
#for item in soup.select('.item'):
#	print(item.get_text())



#Navigation
el = soup.body.contents[1].contents[0].find_next_sibling()
el = soup.find(id='section-2').find_previous_sibling()
el = soup.find(class_='item').find_parent()






print(el)