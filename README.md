# Test technique Falsk API - Sewan 
Candidat: Antoine THIBAUD

In this folder, you will find the source code of the application and a docker image to test it.

To make it run, you have two options:

- Start docker image:

```sh
$ docker load < flaskapitest.tar
$ docker run -p 5000:5000 flaskapilivrable:latest
```

  - Classic install with requirements install
```sh
$ pip install -r requirements
$ python3 app.py
```

# IMPORTANT:

This app uses bootstrap CDN links for front design. It requires network access to have a correct display.


### How it works:

This Flask application allows you to send GET and POST request.

The first form is a GET request to search in the json datas, if we have clients in the city.
The second form is a POST request to add new client in the json file.

Nota:
Functions like emailing, SMS service or lorgs are only commented in the code ass possible actions to implement.

