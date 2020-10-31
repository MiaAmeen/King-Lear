import os
from html.parser import HTMLParser
from urllib.request import urlopen
import ssl
import re

if os.getcwd() == "/Users/destroyerofworlds/Desktop":
    pass
else:
    os.chdir('/Users/destroyerofworlds/Desktop')


def ifUser():
    playname= input("Enter play name:")
    tag= input("Enter tag:")
    url= input("Enter url:")
    while True:
        scenes= input("Enter number of scenes:")
        acts= input("Enter number of acts:")
        if scenes.isdigit() and acts.isdigit():
            scenes= int(scenes)
            acts=  int(acts)
            break
        else:
            print("Enter a numeric digit!")

        acts= {}


def createurl():
    global urlist
    url= "https://www.litcharts.com/shakescleare/shakespeare-translations/king-lear/act-"
    urlist= []
    acts= {1: [1,2,3,4,5], 2: [1,2,3,4], 3: [1,2,3,4,5,6,7], 4:[1,2,3,4,5,6,7], 5:[1,2,3]}
    for act in acts:
        for scene in acts[act]:
            urlist.append(url+str(act)+"-scene-"+str(scene))

createurl()

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


tag= input("Enter tag:")
#<div class='translation-content'>
KLpirate= open('iStoleKingLear', 'x')

for url in urlist:
    name= re.findall("(act-[0-9]-scene-[0-9])", url)
    print("\n",name[0],"\n")
    data= ""
    play= []
    html = urlopen(url, context=ctx).read()
    open(str(name), 'wb').write(html)

    with open(str(name)) as KL:
        play= KL.readlines()
        for line in play:
            if line.startswith(tag):
                speaker= re.findall('(?:<p class="acs-character-heading">)([A-Z]*)(?:</p>)', line)
                if speaker!= []:
                    line= line.replace(speaker[0],'')
                    data = data+ speaker[0]+ ': '+ line+ '\n'
                else:
                    data = data+ line+ '\n'
                speaker=[]

    class MyHTMLParser(HTMLParser):
        def handle_data(self, data):
            print(data)
            KLpirate.write(data)


    hp = MyHTMLParser()
    hp.feed(data)
    hp.close()

    os.remove(str(name))

KLpirate.close()
