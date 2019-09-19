class roman_to_integer:
    def romanToInt(self, s: str) -> int:
        
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


    def converToArabicNums(self, string):
        elements = list(string)
        number = []
        for i in range(len(elements)):
            r = self.romanNumbers(elements[i])
            num = next(r)[1]
            number.append(num)
        return number


