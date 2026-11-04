# 1: WAQ for the following,tuple and count
# Input: [('apple',5),('banana',3),('apple',2),('orange',5)]
# Output: {'apple':7,'banana':3,'orange':5}
# solution:

pairs = [('apple',5),('banana',3),('apple',2),('orange',5)]
output = {}

## The dict.get() method in Python retrieves the value 
## of a specified key from a dictionary while providing a fallback safety net.
for k,i in pairs:
    output[k] = output.get(k, 0) + i
    ## 0 a default value if key is not present

print(output)

# -----------------------------------------
# -------------------------------------------
## Group Anagrams

# 2. WAQ for the following, group the anagrams...
# Input: ['tea','eat','tan','ate','nat','bat']
# Output: [['eat','tea','ate'],['tan','nat'],['bat']]
# solution: 
from collections import defaultdict

words = ['tea','eat','tan','ate','nat','bat']   # anagrams [Deloitte]
groups = defaultdict(list)
## A Dictionary in which keys will have empty list as it's default va;ue

for w in words:
    groups[''.join(sorted(w))].append(w)
    ## Here sorted(w) is making anagrams level and it will be treated as a key
    ## so group['aet'] will have all tea,eat and ate combination going to it

print(list(groups.values()))
# print(groups) --check this: a dictionary with sorted anagram as keys and 
# anagrams as it's values.

# --------------------------------------------------
# ---------------------------------------------------
# 3. WAP to get the first non repetitive character from a string

def first_char(s):
    seen = {}
    for i in s:
        if i.isalpha():
            seen[i] = seen.get(i,0) + 1
    print(seen)

    for ch in s:
        if ch.isalpha() and seen[ch]==1:
            return ch
    return None


# print(result)
s = "aditya"
print(first_char(s))

