Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
SyntaxError: unexpected indent
>>> import requests
>>> import bs4
>>> res = requests.get('https://learncodeonline.in')
>>> type(res)
<class 'requests.models.Response'>
>>> res.text

>>> soup = bs4.BeautifulSoup(res.text,'lxml')
>>> type(soup)
<class 'bs4.BeautifulSoup'>
>>> hi = soup.select('title')
>>> hi
[<title>Home - LearnCodeOnline INC</title>]
>>> hi[0].getText()
'Home - LearnCodeOnline INC'
>>> hi[1].getText()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    hi[1].getText()
IndexError: list index out of range
>>> hi.getText()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    hi.getText()
AttributeError: 'list' object has no attribute 'getText'
>>> hi[0].getText()
'Home - LearnCodeOnline INC'
>>> 
>>> import requests
>>> import bs4
>>> res = requests.get('https://www.udemy.com/python-for-data-science-and-machine-learning-bootcamp/')
ty
>>> type(res)
<class 'requests.models.Response'>
>>> res.text
'<!DOCTYPE html> <html lang="en"> <head> <meta charset="utf-8"> <meta name="viewport" content="width=device-width, initial-scale=1"> <title>Access to this page has been denied.</title> <!-- Custom CSS -->  <link href="https://fonts.googleapis.com/css?family=Open+Sans:300" rel ="stylesheet"> <style> html,body{ margin: 0; padding: 0; font-family: \'Open Sans\', sans-serif; color: #000; } a{ color: #c5c5c5; text-decoration: none; } .container{ align-items: center; display: flex; flex: 1; justify-content: space-between; flex-direction: column; height: 100%; } .container > div { width: 100%; display: flex; justify-content:center; } .container > div > div { display: flex; width: 80%; } .customer-logo-wrapper{ padding-top: 2rem; flex-grow: 0; background-color: #fff; visibility: hidden; } .customer-logo{ border-bottom: 1px solid #000; } .customer-logo > img{ padding-bottom: 1rem; max-height: 50px; max-width: auto; } .page-title-wrapper{ flex-grow: 2; } .page-title { flex-direction: column-reverse; } .content-wrapper{ flex-grow: 5; } .content{ flex-direction: column; } .page-footer-wrapper{ align-items: center; flex-grow: 0.2; background-color: #000; color: #c5c5c5; font-size: 70%; } @media (min-width:768px){ html,body{ height: 100%; } } </style> <script src="https://www.google.com/recaptcha/api.js" async defer></script> </head> <body> <section class="container"> <div class="customer-logo-wrapper"> <div class="customer-logo"> <img src=\'\' alt="Logo"/> </div> </div> <div class="page-title-wrapper"> <div class="page-title"> <h1>Please verify you are a human</h1> </div> </div> <div class="content-wrapper"> <div class="content"> <p> Please click "I am not a robot" to continue </p> <div class="g-recaptcha" data-sitekey="6Lcj-R8TAAAAABs3FrRPuQhLMbp5QrHsHufzLf7b" data-callback="handleCaptcha" data-theme="dark"> </div> <p> Access to this page has been denied because we believe you are using automation tools to browse the website. </p> <p> Th is may happen as a result of the following: </p> <ul> <li> Javascript is disabled or blocked by an extension (ad blockers for example) </li> <li> Your browser does not support cookies </li> </ul> <p> Please make sure that Javascript and cookies are enabled on your browser and that you are not blocking them from loading. </p> <p> Reference ID: #d6567d30-3d93-11e9-b7cf-03a3c66303c7 </p> </div> </div> <div class="page-footer-wrapper"> <div class="page-footer"> <p> Powered by <a href="https://www.perimeterx.com">PerimeterX</a> , Inc. </p> </div> </div> </section> <!-- Px --> <script> ( function (){ window._pxAppId = \'PXZHh9f9x0\'; var clientSrc = \'//client.perimeterx.net/\' + window._pxAppId + \'/main.min.js\'; var p = document.getElementsByTagName("script")[0], s = document.createElement("script"); s.async = 1; s.src = clientSrc; p.parentNode.insertBefore(s, p); } () ); </script> <script> window.px_vid="";window.px_uuid="d6567d30-3d93-11e9-b7cf-03a3c66303c7"; function handleCaptcha(response){ var vid = ""; var uuid = "d6567d30-3d93-11e9-b7cf-03a3c66303c7"; var name = "_pxCaptcha"; var expiryUtc = new Date(Date.now()+1000*10).toUTCString(); var cookie = name + \'=\' + JSON.stringify({r: response, v: vid, u: uuid}) + \'; expires=\' + expiryUtc + \'; path=/\'; document.cookie = cookie; location.reload(); } </script> </body> </html>'
>>> soup = bs4.BeautifulSoup(res.text,'csv')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    soup = bs4.BeautifulSoup(res.text,'csv')
  File "C:\Users\cw\AppData\Local\Programs\Python\Python37-32\lib\site-packages\bs4\__init__.py", line 196, in __init__
    % ",".join(features))
bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: csv. Do you need to install a parser library?
>>> soup = bs4.BeautifulSoup(res.text,'lxml')
>>> type(soup)
<class 'bs4.BeautifulSoup'>
>>> h1 = soup.select('title')
>>> h1
[<title>Access to this page has been denied.</title>]
>>> hi[0].getText()
'Home - LearnCodeOnline INC'
>>> h1[0].getText()
'Access to this page has been denied.'
>>> 
