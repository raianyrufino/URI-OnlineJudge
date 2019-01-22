subfilo = raw_input()
classe = raw_input()
alim = raw_input()

if subfilo == "vertebrado":
  if classe == "ave":
    if alim == "carnivoro":
      print "aguia"
    elif alim == "onivoro":
      print "pomba"
  elif classe == "mamifero":
    if alim == "onivoro":
      print "homem"
    elif alim == "herbivoro":
      print "vaca"

else:
  if classe == "inseto":
    if alim == "hematofago":
      print "pulga"
    elif alim == "herbivoro":
      print "lagarta"
  elif classe == "anelideo":
    if alim == "hematofago":
      print "sanguessuga"
    elif alim == "onivoro":
      print "minhoca"
