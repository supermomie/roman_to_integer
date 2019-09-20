from datetime import datetime


class roman_to_integer:
    def romanToInt(self, s: str) -> int:
        result = self.checkCombination(s)
        return sum(result)

    def romanNumbers(self, val):
        roman_numbers = {"I" : 1,
                        "V" : 5,
                        "X" : 10,
                        "L" : 50,
                        "C" : 100,
                        "D" : 500,
                        "M" : 1000}
        matches = ([x, y] for x, y in roman_numbers.items() if val == x)
        return matches


    def converToIntegerNums(self, string):
        elements = list(string)
        number = []
        for i in range(len(elements)):
            r = self.romanNumbers(elements[i])
            num = next(r)[1]
            number.append(num)
        return number


    def checkCombination(self, s):
        translate = self.converToIntegerNums(s)
        for i in range(len(translate)):
            if i != (len(translate)-1):
                if translate[i] < translate[i+1]:
                    translate[i] = -translate[i]
        return translate


start = datetime.now()
sol = roman_to_integer()

for i in range(100000):
    res = sol.romanToInt("MCMXCII") # 1992


print(res)
print("looped 1M times : ",datetime.now()-start)
