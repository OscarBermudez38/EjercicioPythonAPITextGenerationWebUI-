import requests
import json

url=  "http://127.0.0.1:5000/v1/completions"
headers = {"Content-Type": "application/json"}

while True:

    personaje_principal = input("Nombre del personaje principal:\n> ")
    personaje_secundario = input("Nombre del personaje secundario:\n> ")
    lugar = input("Lugar dondE transcurre la historia:\n> ")
    accion = input("    Una acción importante que debe acontecer en la historia:\n> ")

    user_message = f"Hello, I need you to create a story where the main character is {personaje_principal}, accompanied by {personaje_secundario}. The story should take place in {lugar}, and it must include {accion} as a key event."


    body = {"prompt": user_message, "max_tokens": 4096}
    response = requests.post(url=url, headers=headers, json=body)
    message_response = json.loads(response.content.decode("utf-8"))
    assistant_message = message_response["choices"][0]["text"]
    print(assistant_message)
