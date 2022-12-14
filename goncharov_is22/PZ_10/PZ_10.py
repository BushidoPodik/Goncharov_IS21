magnit = {"moloko", "sol", "sahar"} 
pyatorka = {"myaso", "moloko", "sir"} 
perekr = {"moloko", "tvorog", "sir", "sahar"} 
print("Полный список товаров: ") 
print(f"magnit: {magnit}, pyaterka: {pyatorka}, perekrestok: {perekr}") 
print("В каких магазинах есть молоко и сыр:") 
if "moloko" and "sir" in magnit: 
 print("magnit") 
if "moloko" and "sir" in pyatorka: 
 print("pyaterka") 
if "moloko" and "sir" in perekr: 
 print("perekrestok") 
print("В каких магазинах есть сахар:") 
if "sahar" in magnit: 
 print("magnit") 
if "sahar" in pyatorka: 
 print("pyaterka") 
if "sahar" in perekr: 
 print("perekrestok")
