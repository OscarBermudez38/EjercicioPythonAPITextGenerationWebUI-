# EjercicioPythonAPITextGenerationWebUI-
Ejercicio en el cual probamos diferentes LLM para ver cual es mejor generando una historia

Lo primero que debemos de hacer es ejecutar TextGenerationWebUI, una vez ejecutado tendremos que descargar y posteriormente instalar cada modelo en este caso hemos intentado utilizar varios modelos para probar pero la mayoría nos dio fallo de descarga o de carga elúnico que fue perfectamente fue Qwen_Qwen2-0.5B-Instruct.
1. .\start_windows.bat
2. Una vez dentro buscaremos enuestro buscador http://127.0.0.1:7860/
3. A continuación tendremos que elegir un modelo de HuggingFace y copiar su nombre el cual esta compuesto del creador/nombre-del-modelo.
4. Ahora que entramos vamos al apartado models.
5. Ahora en models debemos poner el modelo previamente copiado en el apartado de download.
6. Una vez descargado el modelo podremos inicializar TextGenerationWebUI con el parámetro --api, con el comando: --api o .\start_windows.bat --api --model {nombre del modelo}
![imagen-cliente-TextGenerationWebUI](images/cap-download.png)

## ¿Qué hace el parámetro --api?

* Activa un endpoint HTTP que puedes utilizar para enviar entradas (prompt) y recibir salidas (texto generado).
* Por defecto, la API estará disponible en http://localhost:5000.

## Modificación de parámetros 
Para modificar los parámetros lo que haremos es editarlos a la hora de enviarle el body, siendo el max_tokens por defecto 2038 y la temperatura es elegida por el usuario :

`   
body = {
        "prompt": user_message,
        "max_tokens": 2038,
        "temperature": temperatura
    }
    `

## Edición de parámetros interfaz gráfica 
También se puede editar el max_lenght y la temperature desde la linea de comandos de la aplicación, en nuestro caso hemos añadido la opción de que el usuario elija la temperatura dándole 3 opciones.

### Parámetros por defecto

![imagen-cliente-TextGenerationWebUI](images/parameters-default.png)

### Parámetros editados

`    body = {"prompt": user_message, "max_tokens": 4096, "temperature": 0.8}
`
![imagen-cliente-TextGenerationWebUI](images/parameters-editados.png)

## Ejemplo de ejecución

### Qwen_Qwen2-0.5B-Instruct con 2038 caracteres y 1 de temperatura

![ejecucuion-Qwen_Qwen2-0.5B-Instruct](images/ejemplo-qwen-1.png)


### Qwen_Qwen2-0.5B-Instruct con 2038 caracteres y 2 de temperatura

![ejecucuion-Qwen_Qwen2-0.5B-Instruct](images/ejemplo-qwen.png)

### Qwen_Qwen2-0.5B-Instruct con 2038 caracteres y 3 de temperatura

![ejecucuion-Qwen_Qwen2-0.5B-Instruct](images/ejemplo-qwen-3.png)

## Conclusión
Como hemos podido observar parece que trabaja mejor cuanta más temperatura tiene, donde mejor siguió las normas que le pedimos fue en el 3 llegando añadir todos los personajes y sacando una historia de 7 capitulos (los añadiré a images pero no en el readme.md para no hacerlo más tedioso).

### Errores
A lo largo del ejercicio he tenido múltiples errores a la hora de descargar y cargar modelos pese a tener el acceso a la api, aquí dejo la lista de todos los modelos que intenté utilizar, al final utilicé diferentes modelos de Qwen ya que esos modelos si me funcionan.

#### Lista de modelos que se intentaron utilizar

![ejecucuion-Qwen_Qwen2-0.5B-Instruct](images/modelos-probados.png)

