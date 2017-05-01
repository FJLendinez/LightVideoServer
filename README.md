# LightVideoServer

## Quickstart

### To run locally

1.- Install all dependencies with pip

``` pip install -r requeriments.txt ```

2.- Create a empty folder called 'video'

|->Instance
            |->deploy.py
            ...
|->video
|->templates
            |->list.html
            ...
|->views
        |->list.py
        ...
|->run_it.py
...

2.- Execute it

``` python run_it.py ```

### To run to serve with a WEB server

1.- Install all dependencies with pip

``` pip install -r requeriments.txt ```

2.- Edit the WSGI file

3.- Follow the instructions to bind WSGI applications on WEB server