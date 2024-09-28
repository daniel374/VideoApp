# VideoApp
 ## Descripción
 La aplicación debe permitir ver videos, ver recomendaciones (comentarios), dar “me gusta/me disgusta” y realizar búsquedas por el nombre del título y del artista.

 ## Instalación

 1. Tenemos un ambiente virtual creado con la version de Python 3.10
 2. Se genera el requirements.txt en la raiz del proyecto el cual contiene todos los recursos de librerias y paquetes necesarios para la ejecución del proyecto:

   ![imagen](https://github.com/user-attachments/assets/99a96c90-e4a5-496a-9dd4-cce3abd1b4eb)

3. Con el comando basico instalamos:

pip install -r requirements.txt

## Ejecucion:

1. Se presenta la estructura del proyecto y el archivo main que pone en servicio la aplicación:

   ![imagen](https://github.com/user-attachments/assets/c665f1df-23f8-43a4-98f3-bdcc40e8a098)

2. Se utilizo Pycharm como Ide para el desarrollo, ejecución y depuración del proyecto. Se comparte la configuración del proyecto en Pycharm:
   ![imagen](https://github.com/user-attachments/assets/6346deb3-6800-4573-8113-272c77b4ddc3)

3. Ejecutando el proyecto:  
   ![imagen](https://github.com/user-attachments/assets/d0509f76-545b-4df9-a33a-e01459539c76)

4. Visualización de la aplicación:
   4.1 ![imagen](https://github.com/user-attachments/assets/287f324d-6c2b-4d24-8e75-c70e87f412ef)

   4.2 ![imagen](https://github.com/user-attachments/assets/174e24a6-047d-484f-af1d-94f6efbe2f79)

   4.3 ![imagen](https://github.com/user-attachments/assets/45e9e48c-1cd4-486b-b525-a11984ef9ab4)

## Configuración de Bases de datos:
   1. Se diseña el siguiente modelo de BD basandonos en la logica de negocio requerida para la aplicación:
      ![imagen](https://github.com/user-attachments/assets/b22acc66-2498-44cf-a9ef-7cedae6ab30d)
      
   2. Se comparte un script que permite alimentar la BD con data, para poderla visualizar en la aplicación.
### Alimentación de la BD por medio de Postman:
   1. Se comparte la colección con los servicios previamente configurados en Postman:
      ![imagen](https://github.com/user-attachments/assets/3fbe21f1-9a89-41e7-bd16-b4da4fff7618)

   2. Contamos con servicios basicos para agregar información y consultarla utiles para alimentar la BD:

      ![imagen](https://github.com/user-attachments/assets/fc7e2d4a-5962-44a4-8893-ee3ceb53238f)
      
   4. Ejemplo de consumo de Api que lista los videos:
      ![imagen](https://github.com/user-attachments/assets/87a138b7-58c5-4d98-bc85-002ea0d6f2e1)

## Ejemplo de ejecucion de pruebas unitarias:
![imagen](https://github.com/user-attachments/assets/e256ab59-243a-459c-a755-b5b38e34d6ed)


