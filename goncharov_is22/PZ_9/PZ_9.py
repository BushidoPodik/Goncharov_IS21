a = {"slovo": "word", 
 "a": "b", 
 "s": "g"} 
s = {"burgerking": "klass", 
 "ant": "paint", 
 "space": "gold"} 
d = {"abc": "def", 
 "animal": "tree", 
 "frog": "card"} 
soed = {**a, **s, **d} 
print(a, s, d) 
print(f"Соединенный список: {soed}")
