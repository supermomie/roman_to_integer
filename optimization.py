from datetime import datetime

def romanToInt(s):
        roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        init_val = 0
        for i in range(len(s)):
            #print(roman_numbers[s[i]])
            if i > 0 and roman_numbers[s[i]] > roman_numbers[s[i - 1]]:
                #print(roman_numbers[s[i]], "---", roman_numbers[s[i - 1]])
                #print(roman_numbers[s[i]] - 2 * roman_numbers[s[i - 1]])
                init_val += roman_numbers[s[i]] - 2 * roman_numbers[s[i - 1]]
                #print("init_val " ,init_val)
            else:
                init_val += roman_numbers[s[i]]
        return init_val




start = datetime.now()

romanToInt("MCMXCII")
print("one time : ", datetime.now()-start)

for i in range(100000):
    
   res= romanToInt("MCMXCII")

print(res)
print("looped 1M time : ",datetime.now()-start) #0.1s
