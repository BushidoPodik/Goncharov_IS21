import random
ru_letters = u"абвгдеёзийклмнопрстуфхъыьэАБВГДЕЁЗИЙКЛМНОПРСТУФХЪЫЬЭ"
en_letters = u"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = u"0123456789"
letters = ru_letters + en_letters + digits
C = random.choice(letters)
print("Символ: ", C)
if ru_letters.find(C) != -1:
    print("Russian")
elif en_letters.find(C) != -1:
    print("Latin")
elif digits.find(C) != -1:
    print("Digit")
    