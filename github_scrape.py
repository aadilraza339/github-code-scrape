from bs4 import BeautifulSoup
from urllib.request import urlopen
from PIL import Image   
import webbrowser,wget,os,requests
user=input('enter user name of github>>\n')
response=requests.get('https://github.com/{}'.format(user)) 
soup =BeautifulSoup(response.text,'html.parser')
im=soup.find('div',class_='float-left col-3 col-md-12 pr-3 pr-md-0')
image=im.find('a').get('href')
if os.path.exists(image[41:-10]):
	img = Image.open('/home/ajay/Desktop/'+image[41:-10])
	img.show()
else:
	wget.download(image)
	img = Image.open('/home/ajay/Desktop/'+image[41:-10])
	img.show()
response=requests.get('https://github.com/{}?tab=repositories'.format(user)) 
soup =BeautifulSoup(response.text,'html.parser')
li=soup.find('div',{'id':'user-repositories-list'})
all_li=li.find_all('li')
list_href=[]
count=0
def list_of(data):
	global count
	for i in data:
		dic=i.find('div',class_='d-inline-block mb-1')
		href=dic.find('a').get('href')
		name=dic.find('a')
		list_href.append(href)
		count+=1
		print(count,name.text.strip())
list_of(all_li)
user=int(input('which you  want open'))
link=('https://github.com'+list_href[user-1])
print(link)
response=requests.get(link)
soup =BeautifulSoup(response.text,'html.parser')
tbody=soup.find('table',class_='files js-navigation-container js-active-navigation-container')
focus=tbody.find_all('td',class_='content')
files=[]
count=0
for td in focus:
	snap=td.find('a')
	if snap!=None:
		count+=1
		print(count,snap.text)
		files.append(snap.text)
user_file=int(input('which file do want to see view'))
check=files[user_file-1]
code_url='{}/blob/master/{}'.format(link,files[user_file-1])
response=requests.get(code_url)
soup =BeautifulSoup(response.text,'html.parser')
if check=='README.md':
	read=soup.find('article',class_='markdown-body entry-content p-3 p-md-6')
	print(read.text)
elif check!='a':
	new_tbody=soup.find_all('tr')
	a=1
	for i in new_tbody:
		name=i.find('td',{'id':'LC{}'.format(a)})
		a+=1
		print(name.text)
else:
	print('you can not open this')


