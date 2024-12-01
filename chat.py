import requests
import json

url = "http://127.0.0.1:5000/v1/completions"
headers = {"Content-Type": "application/json"}

while True:
    print("Selecciona el nivel de temperatura:")
    print("1. Baja (0.1) - Respuestas más precisas y deterministas")
    print("2. Media (0.5) - Equilibrio entre precisión y creatividad")
    print("3. Alta (0.9) - Respuestas más creativas e impredecibles")
    
    opcion = input("Ingresa el número de tu elección:\n> ")

    # Determinar la temperatura según la opción seleccionada
    if opcion == "1":
        temperatura = 0.1
    elif opcion == "2":
        temperatura = 0.5
    elif opcion == "3":
        temperatura = 0.9
    else:
        print("Opción inválida. Se usará temperatura media (0.5) por defecto.")
        temperatura = 0.5

    personaje_principal = input("Nombre del personaje principal:\n> ")
    personaje_secundario = input("Nombre del personaje secundario:\n> ")
    lugar = input("Lugar donde transcurre la historia:\n> ")
    accion = input("Una acción importante que debe acontecer en la historia:\n> ")

    user_message = f"Hello, I need you to create a story where the main character is {personaje_principal}, accompanied by {personaje_secundario}. The story should take place in {lugar}, and it must include {accion} as a key event."

    # Incluir la temperatura en el cuerpo de la solicitud
    body = {
        "prompt": user_message,
        "max_tokens": 2038,
        "temperature": temperatura
    }

    response = requests.post(url=url, headers=headers, json=body)
    message_response = json.loads(response.content.decode("utf-8"))
    assistant_message = message_response["choices"][0]["text"]
    print(assistant_message)
