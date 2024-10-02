import requests
from bs4 import BeautifulSoup

source = requests.get('https://www.worldometers.info/coronavirus/').text
soup = BeautifulSoup(source, 'lxml')


def getWorldCases(type):
    allOf = soup.find("div", {"class": "content-inner"})
    totalCasesHTML = allOf.findAll("div", {"id": "maincounter-wrap"})[type]
    totalCasesInner = totalCasesHTML.find("div", {"class": "maincounter-number"})
    finalCases = totalCasesInner.find("span")
    return finalCases.text

def getUpdateTime():
    allOf = soup.find("div", {"class": "content-inner"})
    updatedAt = allOf.find("div", {"style": "font-size:13px; color:#999; margin-top:5px; text-align:center"})
    return updatedAt.text.replace("Last updated: ", "")

def getCountry(type, country):
    try:
        cData = requests.get('https://www.worldometers.info/coronavirus/country/{loc}/'.format(loc=country)).text
        cSoup = BeautifulSoup(cData, 'lxml')
        allOf = cSoup.find("div", {"class": "content-inner"})
        totalCasesHTML = allOf.findAll("div", {"id": "maincounter-wrap"})[type]
        totalCasesInner = totalCasesHTML.find("div", {"class": "maincounter-number"})
        finalCases = totalCasesInner.find("span")
        return finalCases.text
    except:
        return 'Invalid Entry'        
