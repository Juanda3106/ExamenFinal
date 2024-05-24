# ExamenFinal
# Proyecto de Conversión de Caracteres a Bytes

Este proyecto permite convertir caracteres y palabras a su representación en bytes, así como convertir bytes a su representación ASCII.

## Descripción

Este proyecto fue creado con el objetivo de proporcionar funcionalidades para la conversión de caracteres a su representación en bytes y viceversa, utilizando Python.

## Integrantes del Proyecto

- Juan David Llanos
- Juan Andres Ibarra
- Sebastián Yate Rodriguez

## Comandos de Git Utilizados

### Inicialización y Primer Fork

1. **Juan Llanos** creó el repositorio público:
    ```bash
    # Inicializar el repositorio
    git init
    ```

2. **Juan Ibarra** realizó un fork del repositorio y creó una rama para subir el código en Python:
    ```bash
    # Clonar el fork localmente
    git clone https://github.com/juanibarra/nombre-del-repositorio.git
    cd nombre-del-repositorio

    # Crear una nueva rama
    git checkout -b Ibarra_Subida_Python
    
    # Añadir y comitear el archivo
    git add conversion.py
    git commit -m "Add conversion functions in conversion.py"

    # Subir los cambios a su fork en GitHub
    git push origin Ibarra_Subida_Python
    ```

3. **Juan Ibarra** realizó un pull request desde su fork, y **Juan Llanos** lo aceptó:
    ```bash
    # Realizado en la interfaz web de GitHub
    ```

### Segundo Fork y Añadir .gitignore

4. **Sebastián** realizó un fork del repositorio ya actualizado y creó una nueva rama para añadir un archivo `.gitignore`:
    ```bash
    # Clonar el fork localmente
    git clone https://github.com/sebastian/nombre-del-repositorio.git
    cd nombre-del-repositorio

    # Crear una nueva rama
    git checkout -b Sebastian_Add_Gitignore

    # Añadir el archivo .gitignore
    echo "*.pyc\n__pycache__/" > .gitignore

    # Añadir y comitear el archivo
    git add .gitignore
    git commit -m "Add .gitignore file"

    # Subir los cambios a su fork en GitHub
    git push origin Sebastian_Add_Gitignore
    ```

5. **Sebastián** realizó un pull request desde su fork, y **Juan Llanos** lo aceptó:
    ```bash
    # Realizado en la interfaz web de GitHub
    ```

## Ramas Creadas

- **main**: Rama principal del proyecto.
- **Ibarra_Subida_Python**: Rama creada por Juan Ibarra para subir el código de conversión y validación en Python.
- **Sebastian_Subida_Gitignore**: Rama creada por Sebastián para añadir el archivo `.gitignore`.
- **Llanos_Edicion_Readme**: Reame creada por Juan David para editar el README

## Changelog

#### Added
- Funciones de conversión en 'examen_final.py' (por Juan Ibarra).
- Archivo de prueba en 'pruebas_examen_final.ipynb' (por Juan Ibarra)
- Archivo `.gitignore` para excluir archivos innecesarios (por Sebastián Yata).
- Edicion de ´README´ (por Juan David Llanos)

## Uso del Programa

El programa permite realizar las siguientes operaciones:
- Generar la representación en byte de un carácter.
- Generar la representación en byte de una palabra.
- Generar la representación ASCII de un byte.

Para ejecutar el programa, corre el archivo principal `conversion.py` y sigue las instrucciones en pantalla.
