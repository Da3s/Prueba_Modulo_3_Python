import templates
from api_get import request_get

url = "https://aves.ninjas.cl/api/birds" 
response = request_get(url)

cadena = ""

for diccionario in response:
    cadena = cadena + templates.template2.substitute(nombre_espanol= diccionario["name"]["spanish"], nombre_ingles=diccionario["name"]["english"], url_img_full=diccionario["images"]["full"])

file = open("AvesChile.html", "w")
message = templates.template.substitute(contenido= cadena)
file.write(message)