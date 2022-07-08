"""1. Assign a string to a variable name str_txt and display"""


from operator import index


str_txt = 'Wellcome Nguyen Van Tan'
print (str_txt)

""" 2. String as array: display some characters of str_txt
 3 first character
 4 last character
 - characters from position 1 to position 4
 - characters from position first to position 5
 - characters from position second to position last
"""


print (str_txt[0])
print (str_txt[-1])
print (str_txt[1:5])
print (str_txt[:5])
print (str_txt[2:])


""" 3. loop through string
 Print all characters of str_txt, using for loop iteration
"""

for character in str_txt:
    print (character)

"""
 4. length of string
 Print length of string str_txt
"""
print(len(str_txt))

"""
5. check if string srt_txt contains other string.
if has, print start position of that substring.
"""


subtring = 'anh'
if subtring in str_txt:
    print(str_txt.index(subtring))
else:
    print ('not in string')

"""
6. print str_txt with all charaters are capitalized/nomalized.
print str_txt with all first characters of each words ar capitalized.
"""
print(str_txt.upper())
print(str_txt.lower())
print(str_txt.title())

"""
7. remove all whitespace from str_txt string
"""
print_str_txt = str_txt.split(' ')
print (''.join(print_str_txt))
print (str_txt.replace(' ',''))
"""
8. replace all h characters with m character
"""
print (str_txt.replace('h','m'))
"""
9. split str_txt by whitespace an display second item of array
"""
for index,v in enumerate(print_str_txt):
    if (index == 2):
        print(v)