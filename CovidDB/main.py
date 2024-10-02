from COVID_Cases import getWorldCases, getUpdateTime, getCountry
import colorama
from colorama import Fore, Back, Style

colorama.init()
worldCasesInt, worldDeathInt, worldRecoveredInt = 0, 1, 2

ended = 0


print(Style.BRIGHT + Fore.CYAN + "Welcome to " + Fore.RED + "COVID-19 " + Fore.CYAN + "Cases Checker" + Fore.WHITE + Style.DIM + ' - Type "Quit" to quit at any time \n' + Fore.RESET + Style.BRIGHT)
print("There have been {numCases}cases of ".format(numCases=getWorldCases(worldCasesInt)) + Fore.RED + "COVID-19 " + Fore.RESET + "worldwide.")
print("There have been {numCases} deaths from ".format(numCases=getWorldCases(worldDeathInt)) + Fore.RED + "COVID-19 " + Fore.RESET + "worldwide.")
print("There have been {numCases} recovered from ".format(numCases=getWorldCases(worldRecoveredInt)) + Fore.RED + "COVID-19 " + Fore.RESET + "worldwide.")
print()
print()
print(Back.GREEN + "Updated at: " + getUpdateTime()  + Back.RESET)
print()
print()
while ended == 0:
    countryAns = input("Type a Country: ")
    countryAnswer = countryAns.replace(" ", "-")
    if countryAnswer.lower() == "quit":
        exit()
    print()
    if getCountry(worldCasesInt, countryAnswer) != 'Invalid Entry':
        print("There have been {numCases}cases of ".format(numCases=getCountry(worldCasesInt, countryAnswer)) + Fore.RED + "COVID-19 " + Fore.RESET + "in {country}.".format(country=countryAnswer.capitalize()))
        print("There have been {numCases} deaths from ".format(numCases=getCountry(worldDeathInt, countryAnswer)) + Fore.RED + "COVID-19 " + Fore.RESET + "in {country}.".format(country=countryAnswer.capitalize()))
        print("There have been {numCases} recovered from ".format(numCases=getCountry(worldRecoveredInt, countryAnswer)) + Fore.RED + "COVID-19 " + Fore.RESET + "in {country}.".format(country=countryAnswer.capitalize()))
        print()
        print()
        print(Back.GREEN + "Updated at: " + getUpdateTime() + Back.RESET)
    else:
        print(Back.RED + 'Invalid Entry' + Back.RESET)
    print()
    print()
