import random

respuestas = [
    "Claro k si po bro"
    "No puedo decirlo"
    "Definitivamente no"
    "Si, pero con ciertas dificultades"
    "Sí, con seguridad"
    "Por supuesto"
    "Tal vez"
    "No lo puedo responder"
    "No puedo predecir"
    "Mejor no decirlo"
    "Espero que no"
    "No, claramente no"
    "No, pero con seguridad",
    "XD",
    "Shi",
    "Hola pe",
    "K yiko"
    "Tralalero tralala"
]

pregunta = input("Preguntame Algo: ")

respuesta = random.choice(respuestas)

print(f"Respuesta: {respuesta}")