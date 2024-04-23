"""
Given a list of city names and their corresponding populations, write a program to output a city name subject to the following constraint: the probability of the program to output a city's name is based on its population divided by the sum of all cities' population. Assume the program will be repeatedly called many times.

Example:
* NY: 7 Million
* SF: 5 Million
* LA: 8 Million
* Total: 20 Million
The probability to generate NY is 7/20, SF is 1/4.

dic = {
"NY": 7, 
"SF": 5, 
"LA": 8
}

cityDict = {
    "NY": 7, 
    "SF": 5, 
    "LA": 8
}
"""

totalPop = 0
# resMap = {}
idxToCity = {}

def getRandomNumber(lower, higher):
    # fill later
    return random.int(lower, higher)

# 1 to 7 => NY
# 8 to 12 => SF
# 13 to 20 => LA
def getCityName(num):
    for idx, city in idxToCity:
        for l, r in idx:
            if l <= num <= r:
                return city
    # binary search or search range (segment tree) => logn

def genCity(pop_dict) -> str: # city name
    if totalPop == 0: # precomputation about index to city map
        for city, pop in pop_dict:
            totalPop += pop # 20 = 7 + 5 + 8
        
        l, r = 0, 0
        for city, pop in pop_dict:
            # resMap[city] = pop / totalPop # (7 / 20)
            l = r + 1 # 1, 8
            r = pop + r - 1 # 7, 12
            idxToCity[(l, r)] = city # (1,7) => NF, (8,12) => SF, (13,20) => LA


    num = getRandomNumber(1, totalPop) # [1, 20]
    city = getCityName(num)
    print(city)

main():
  genCity(dic)
  genCity(dic)
  genCity(dic)
  genCity(dic)
  genCity(dic)
  genCity(dic)
