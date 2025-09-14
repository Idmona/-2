from transliterate import translit
from num2words import num2words

print(translit("""Ladies and gentlemen, I'm 78 years old and I finally got 15 minutes of fame once in a lifetime and I guess that this is mine. 
People have also told me to make these next few minutes escruciatingly embarrassing and to take vengeance of my enemies.
Neither will happen.

More than 3 years ago I moved to Novo-Novsk, but worked on new Magnetic Storage for last 40. When I was 8...""", 'ru',))
print()
n1 = 78
n2 = 15
n3 = 3
n4 = 40
n5 = 8

print(n1, "-", translit(num2words(n1, lang='en'), 'ru'))
print(n2, "-", translit(num2words(n2, lang='en'), 'ru'))
print(n3, "-", translit(num2words(n3, lang='en'), 'ru'))
print(n4, "-", translit(num2words(n4, lang='en'), 'ru'))
print(n5, "-", translit(num2words(n5, lang='en'), 'ru'))
