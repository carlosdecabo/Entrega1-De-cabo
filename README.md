
# Escuela de Natacion CDC

Una App de Club de natacion realizado con Python, usando el Django como framework


## Documentation

Creacion de projeto django 

Creacion de app django

Utilizo una plantilla de bootstrap modificada y adaptada a la necesidad, en la cual renderizo los datos desde el backend, usando la herencia de padre a hijo para altenar las diferentes vistas que cree desde ahi.

## models.pý
En este archivo se encuentra el modelaje de datos usado para el backend del producto.

## forms.py 
En este archivo se encuentra el formulario que hace envio de los datos ingresados al backend.

## views.py
Aca encontraremos las vistas creadas y moldeadas para la navegacion de la web.

## urls.py

Archivo donde esta la configuracion de rutas.

## Index

En esta page podemos encontrar un vistazo general de la web.

## Registro

En esa seccion podes ingresar un nuevo socio, datos que se cargan a la base de datos, a través del modelo y del form

## Buscarpersona

AAca podes buscar algun socio registrado en el Clud, usando el DNI del mismo, consulta la informacion con la base de datos y la compara, si no encuentra lo solicitado, da un aviso de que ingrese un dato valido, caso contrario renderiza lo solicitado.


## Authors

- [@Carlos De cabo](https://www.linkedin.com/in/carlos-eduardo-de-cabo-marchan-717430128/)


## Issue

LA App presenta un problema que no realiza aun la Busqueda por persona "Buscarpersona" en este sentido figura un error 
Page not found (404)
Request Method:	GET
Request URL:	http://127.0.0.1:8000/AppGimnasio/buscar/?dni=444

Actualmente esta en proceso de busqueda de la solucion
