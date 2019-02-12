# VulEdiWi

# Description
A tool to find all the publicly editable wiki of an organization and publish your demo page on it.
This code works wells on Mac OS. In case you are looking to run it on ubuntu servers use 

```
pyvirtualdisplay
```

# Requirements
1) Gecko Driver (https://github.com/mozilla/geckodriver/releases)
2) Your Github Cookies (I would suggest using a temporary account)
3) All those PIP installsss
4) Python3x


# Instructions
1) Make sure you are using python 3
2) Keep your geckodriver file in 
```
/usr/local/bin/
```
else you have to menton the path of the file in the code
3) How to add cookies ?
```
c1 = {'name' : 'NAME_OF_THECOOKIE' , 'value' : 'VALUE_OF_THE_COOKIE'}
```
Set all the cookie and it value in variables c1 , c2 ....

Then make sure you add all the cookies 

```
driver.add_cookie(c1)
driver.add_cookie(c2)
etc.
```

3) Some organisations have more than 100 repos and through the Github API call only 100 can be fetched per page. To fetch more repos. Just set the "page=1" to "page=2" and so on. 

```
data = os.popen('curl -s "https://api.github.com/users/'+enter+'/repos?per_page=100&page=1"  | grep -o '+"'https://github.com[^\"]*\.git'").read()
```



