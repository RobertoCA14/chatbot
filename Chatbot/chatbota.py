from posixpath import split
#expresiones regulares
import re
import random

from Preguntas import saludar,como_estas, propuesta_ayuda, ubicacion, compra, agradecer, envios, costoenvio, confirmar, tiempoenvio

def get_respuesta(salida_usuario):
    division_mensajes = re.split(r'\s|[,:;.?!-_]\s*', salida_usuario.lower())
    respuesta = check_all_messages(division_mensajes)
    return respuesta

def message_probability(mensaje_usuario, reconocimiento_palabra, respuesta_unica=False, Palabra_requerida=[]):
    message_certainty = 0
    has_Palabra_requeridas = True

    for word in mensaje_usuario:
        if word in reconocimiento_palabra:
            message_certainty +=1

    percentage = float(message_certainty) / float (len(reconocimiento_palabra))

#si no hay ninguna palabra requerida el bucle termina ahi 
    for word in Palabra_requerida:
        if word not in mensaje_usuario:
            has_Palabra_requeridas = False
            break
        # y en caso de que si haya una palabra requerida entonces se da la respuesta con mas probabilidad
    if has_Palabra_requeridas or respuesta_unica:
        return int(percentage * 100)
    else:
        return 0
def check_all_messages(message):
        highest_prob = {}
 #Definimos las respuesta, lista de palabras y la respuesta unica y requerida
        def respuesta(bot_respuesta, list_of_words, respuesta_unica = False, Palabra_requeridas = []):
            nonlocal highest_prob
            highest_prob[bot_respuesta] = message_probability(message, list_of_words, respuesta_unica, Palabra_requeridas)

        respuesta( saludar, ['hola', 'klk', 'saludos', 'buenas', 'whats up'], respuesta_unica = True)
        respuesta(como_estas, ['como', 'estas', 'va', 'vas', 'sientes'], Palabra_requeridas=['como'])
        respuesta(propuesta_ayuda, ['bien', 'mas o menos', 'muy bien', 'tranquilo', 'en la brega', 'que bueno', 'me alegroclose'], respuesta_unica = True)
        respuesta(ubicacion, ['ubicados', 'direccion', 'donde', 'ubicacion'], respuesta_unica=True)
        respuesta(compra, ['comprar','compra', 'equipo', 'obtener', 'realizar'], respuesta_unica=True)
        respuesta(agradecer, ['gracias', 'te lo agradezco', 'thanks'], respuesta_unica=True)
        respuesta(envios, ['envio','envios', 'casa', 'mandarlo'], respuesta_unica=True)
        respuesta(costoenvio, ['costo', 'cuesta', 'valor'], respuesta_unica=True)
        respuesta(confirmar, ['comprar', 'enviar', 'enviame', 'confirmar'], respuesta_unica=True)
        respuesta(tiempoenvio, ['tiempo', 'tarda', 'dura'], respuesta_unica=True)
        best_match = max(highest_prob, key=highest_prob.get)
      
        

        return unknown() if highest_prob[best_match] < 1 else best_match


def unknown():
    respuesta = ['puedes decirlo de nuevo?', 'No estoy seguro de lo quieres', 'búscalo en google a ver que tal'][random.randrange(3)]
    return respuesta
#Esto mantiene el bucle para siempre preguntarle al ususario
while True:
    print("Bot: " + get_respuesta(input('You: ')))