#remove vowel letters
def disemvowel(string):
    disemvowel = ''
    for i in string:
         if i not in ['a','A','i','I','u','U','e','E','o','O']:
             disemvowel += i
    return disemvowel


#Other wayes
def disemvowel(string):
    string = "".join([i for i in string if i.lower() not in ['a', 'i', 'u', 'e', 'o']])
    return string


def disemvowel(string):
    string = "".join(filter(lambda x: x.lower() not in 'aeiou', string))
    return string
  

print(disemvowel("This website is for losers LOL!"))



    
