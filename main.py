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
    spl = 
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
