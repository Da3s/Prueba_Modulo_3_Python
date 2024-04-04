import templates
from api_get import request_get

url = "https://aves.ninjas.cl/api/birds" 
response = request_get(url)

cadena = ""

for dicc in response:
    cadena = cadena + templates.template2.substitute(titulo_esp= dicc["name"]["spanish"], titulo_en=dicc["name"]["english"], url_img_full=dicc["images"]["full"])

file = open("AvesChile.html", "w")
message = templates.template.substitute(contenido= cadena)
file.write(message)