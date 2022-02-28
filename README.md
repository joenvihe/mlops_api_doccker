# Analítica como un Servicio
## MAAS
En este repositorio se genera la creación del api para el model.

## PASOS A REALIZAR

- Se creo una variable de entorno y se instalo las librerias necesarias
```bash
>conda create -n envMLopsApi
>pip install -r requirements.txt
```

- Ejecutar de forma local
```bash
>uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8008
```

- En la web colocar la url **http://127.0.0.1:8008/ping**

- Haciendo la prueba de la llamada al modelo, abrir el **git bash**
```bash
>curl --header "Content-Type: application/json" --request POST --data '{"duration":"2","month":"3","date":"16","age":"57","balance":"0.452462","pout":"1","job":"4","camp":"1","contact":"2","house":"1"}' http://127.0.0.1:8008/predict
```

- Se loguea a **heroku**
```bash
>heroku login
```

- Se debe levantar el **docker desktop**

- Se loguea a **heroku container**
```bash
>heroku container:login
```

- Se carga el contenedor a la plataforma de **Heroku**, previamente se debio crear el app
```bash
>heroku container:push web --app docker-fastapi-joenvihe
```