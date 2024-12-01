# EjercicioPythonAPITextGenerationWebUI-
Ejercicio en el cual probamos diferentes LLM para ver cual es mejor generando una historia

Lo primero que debemos de hacer es ejecutar TextGenerationWebUI, una vez ejecutado tendremos que descargar y posteriormente instalar cada modelo en este caso vamos a probar 2 modelos diferentes priemro Qwen_Qwen2-0.5B-Instruct y segundo ............, comandos necesarios:

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
Por defecto están los caracteres capados a 512 entonces para arreglar eso debemos modificar los parámetros, para ello entramos en parameters y aunmentamos el número, aprovechando que estamos en esta pantalla aunmentaresmo también la temperatura así el modelo tendrá más creatividad.

## Ejemplo de ejecución

### Qwen_Qwen2-0.5B-Instruct
![ejecucuion-Qwen_Qwen2-0.5B-Instruct](images/ejemplo-qwen.png)

###
