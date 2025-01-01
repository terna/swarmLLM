import urllib.request
import ssl
import certifi
import tool

def tool() ->str:
    
    url = "https://terna.to.it/pippo1.txt"
    context = ssl._create_unverified_context()
    with urllib.request.urlopen(url, context=context) as response:
        file_content1 = response.read().decode('utf-8')

    url = "https://terna.to.it/pippo2.txt"
    context = ssl._create_unverified_context()
    with urllib.request.urlopen(url, context=context) as response:
        file_content2 = response.read().decode('utf-8')

    url = "https://terna.to.it/pippo3.txt"
    context = ssl._create_unverified_context()
    with urllib.request.urlopen(url, context=context) as response:
        file_content3 = response.read().decode('utf-8')

    return file_content1+'Pp-'+file_content2+'Hp-'+file_content3+'uMA'