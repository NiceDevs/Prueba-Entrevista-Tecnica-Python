
# coding=utf-8

# def counter_vocales(texto):
#     count = 0
#     for vowel in texto:
#         if vowel in vowels:
#             count = count + 1
#     return count

vowels = 'aeiou'

def counter_vocales(texto):
    mytext = texto.lower()
    print (sum(map(mytext.count, vowels)))

def get_vowel(text):
    for letter in text:
        if letter == 'a':
            yield('e')
        elif letter == 'e':
            yield('i')
        elif letter == 'i':
            yield('o')
        elif letter == 'o':
            yield('u')
        elif letter == 'u':
            yield('a')
        

def changeVowels(text):
    counter_vocales(text)
    change_vowel = get_vowel(text)
    new_word = ''
    for letter in text:
        if letter in vowels:
            new_word += change_vowel.next()
        else:
            new_word += letter
    return new_word

print (changeVowels(
    'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys'
    'standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make'
    'a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting,'
    ' remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing'
    ' Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'
    ))
