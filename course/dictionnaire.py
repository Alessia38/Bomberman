phone = input("entrez un numéro de telephone !")
nombre = {
    "0" : "zero",
    "1" : "un" ,
    "2" : "deux",  
    "3" : "trois",  
    "4" : "quatre", 
    "5" : "cinq" ,
    "6" : "six" ,
    "7" : "sept" ,
    "8": "huit" ,
    "9": "neuf"
}
result = ""
for nombre in phone : 
    result += nombre.get(nombre) + " "

    print(result)