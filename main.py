# Task 1
# v1
def array_diff(a, b):
    founded_elements = []
    for compared_el in b:
        for cur_el in a:
            if cur_el == compared_el:
                founded_elements.append(cur_el)

    for founded_element in founded_elements:
        if founded_element in a:
            a.remove(founded_element)      
    return a

# v2
def array_diff(a, b):
    for n in b:
        while(n in a):
            a.remove(n)
    return a

# v3
def array_diff(a, b):
    return [x for x in a if x not in b]

# v4
def array_diff(a, b):
    return filter(lambda i: i not in b, a)


print(array_diff([1,2,2], [2]))


# Task 2
# v1
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")

# v2
def getCount(s):
    return sum(c in 'aeiou' for c in s)
    

print(get_count("bcdfghjklmnpqrstvwxza y"))



# Task 3
# v1
def myfunc(number):
    return int(number)
    
def high_and_low(numbers):
    numbers_list = list(map(myfunc, numbers.split()))
    return str(max(numbers_list)) + ' ' + str(min(numbers_list))

# v2
def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))

# v3
def high_and_low(numbers):
  numbers = [int(c) for c in numbers.split(' ')]
  return f"{max(numbers)} {min(numbers)}"

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))



# Task 4
# v1
def DNA_strand(dna):
    return dna.translate(str.maketrans({'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}))

# v2
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))


DNA_strand("ATTGC")


# Task 5
# v1
def spin_words(sentence):
    spl = sentence.split(" ")
    i = 0
    for word in spl:
        if (len(word) >= 5):
            spl[i] = ''.join(reversed(word))
        i += 1
    return " ".join(spl)

# v2
def spin_words(sentence):
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

# v3
def spin_words(sentence):
    return " ".join([word if len(word) < 5 else word[::-1] for word in sentence.split(" ")])


print(spin_words("or letter spaces the letters words"))



# Task 6
def filter_list(l):
    return [i for i in l if isinstance(i, int)] 

print(filter_list([1, 'a', 'b', 0, 15]))



# Task 7
# v1
def solution(s):
    new_str = ""
    for i in range(0, len(s)):
        if s[i].isupper():
            new_str += " "
        new_str += s[i]
    return new_str

# v2
def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)

print(solution("helloWorld"))


# Task 8
# v1
def valid_braces(string):
    if (string[0] in (")","}","]") or len(string) < 2):
        return False
    else:
        length = len(string)
        i = 0
        while i < length:
            if (string[i] == "]" and string[i - 1] == "[" or string[i] == ")" and string[i - 1] == "(" or string[i] == "}" and string[i - 1] == "{"):
                string = string[:i - 1] + string[i + 1:]
                length -= 2 
                i -= 2
            elif string[i] not in ("(","{","["):
                return False 
            i += 1
    return len(string) == 0

# v2
def validBraces(s):
  while '{}' in s or '()' in s or '[]' in s:
      s=s.replace('{}','')
      s=s.replace('[]','')
      s=s.replace('()','')
  return s==''


  # Task 9
def is_pangram(s):
uniq_s = []
for i in s:
    if i not in uniq_s and i.isalpha():
        uniq_s.append(i.lower())
return len(uniq_s) == 26

print(is_pangram("The quick, brown fox jumps over the lazy dog!"))


# Task 10
# v1
def collinearity(x1, y1, x2, y2):
    if (x2 == 0 and y2 == 0):
        return True
    elif (x1 == 0):
        if (y1 == 0):
            return True
        else:
            return (x2 == 0 and y2 != 0)            
    else:
        if (y1 == 0):
            return (x2 != 0 and y2 == 0)
        else:
            return x2 / x1 == y2 / y1 

# v2
def collinearity(x1, y1, x2, y2):
    return x1 * y2 == x2 * y1


# Task 11
def queue_time(customers, n):
    count = sum(customers)
    time = 0
    i = 0
    new_count = 0
    while (len(customers) > 0):
        if (len(customers) == 1):
            time += customers[i]     
            count -= customers[i]
            break
        else:
            new_count = n if n < len(customers) else len(customers)
            j = 0
            while j < new_count:
                customers[j] -= 1
                if (customers[j] == 0):
                    customers.pop(j)
                    new_count -= 1;
                else:
                    j += 1
            time += 1
            count -= 1        
    return time

print(queue_time([1,2,3,4,5], 1))
print(queue_time([1,2,3,4,5], 100))



# Task 12
# v1
def cog_RPM(cogs):
    length = len(cogs)
    res = 1
    if length > 0 : res = cogs[0] / cogs[length - 1] 
    if length % 2 == 0 : res *= -1
    return res

cog_RPM([100, 75])
cog_RPM([100, 100, 75])


# v2
def cog_RPM(cogs):
    length = len(cogs)
    return cogs[0] / cogs[-1] * (-1)**(length - 1) if length > 0 else 1


# Task 13
# v1
def continued_fraction(nu: int, de:int) -> list[int]:
    arr = []
    wh_part = nu
    if nu != 0:
        while (de != 0) and (wh_part // de > 0 or wh_part % de > 0): 
            arr.append(wh_part // de)
            wh_part, de = de, wh_part % de
        if (de != 0): arr.append(wh_part // de)
    return arr

# v2
def continued_fraction(nu: int, de:int) -> list[int]:
    arr = []
    while nu and de:
        arr.append(nu // de)
        nu, de = de, nu % de
    return arr

print(continued_fraction(311, 144))