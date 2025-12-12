meme_dict = {
  "CRINGE" :"Algo que causa pena o embarazoso";
  "LOL" :"Una respuesta comun a algo gracioso";
  "ROLF":"Se utiliza como reacción a algo gracioso, similar al LOL";
  "POV":"Punto de vista";
  "RANDOM":"Aleatorio sin sentido";
  "FUNAR": "Cancelar o criticar algo";
  "STALKEAR": "Mirar perfiles en redes sociales sin interactuar";
  "CHEVERE": "Algo que esta bien hecho";
  
}
word = input ("Escribe una palabra moderna que no entiebndas (¡Utiliza Mayusculas!): ")

if word in meme_dict.keys():
  print(meme_dict[word])

else:
  print("Todavia no tenemos esa palabra... pero estamos trabajando en ella. ")
