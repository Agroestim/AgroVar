<!-- TODO: Poner las imagenes del producto final -->

<!-- TODO: Añadir soporte al Ingles -->

# AgroVar

![AgroVar Brand Assets](/assets/images/agrovar-brand-product.png "Agrovar Product Screenshot")

AgroVar es una API publica para consultar datos tecnicos de diferentes campañas de cosechas registradas por el INTA.

El proposito de este servicio es permitir que nuestros clientes web oficiales puedan consultar sobre un conjunto de datos ya procesados por este servicio y poder visualizar de forma grafica ciertas estadisticas relevantes.

[English](/README.md) | [Spanish](/README-ES.md)

## Tabla de contenidos

- Status del proyecto
- Documentacion del desarrollador
  1. Instalacion
  2. Despliegue local
  3. Docker
- Estructura del proyecto

# Status del proyecto

Este proyecto aun esta en desarrollo y recomendamos ser pascientes con los **manteiners** dado que no tenemos disponible mucho tiempo. Para recivir asistencia con los issues, pull request, u otras cosas, te pedimos encarecidamente esperar y no abusar de las menciones en github.

Actualmente el proyecto se encuentra en la fase final de desarrollo para la version 0.1.0 estable, la cual posee de los requerimientos especificados. Pensamos implementar en siguientes versiones automatico que permite convertir los ficheros que contienen los datos de las campañas en conjuntos de Json que puedan almacenarce en la base de datos, facilitando porcesos intermedios de conversion y filtracion.

# Documentacion del desarrollador

> Actualmente el proyecto se encuentra en mantenimiento, solo el personal autorizado tiene acceso a modificar el codigo fuente.

En esta seccion encontraras toda la informacion necesaria para poder llevar a cabo el desarrollo de la API.

## Instalacion

1. Clona el repositorio en tu espacio de trabajo.

```powershell
git clone https://github.com/Agroestim/AgroVar.git && cd AgroVar
```

2. Crea un entorno virtual para el proyecto.

```powershell
python -m venv venv
```

> Si no tienes instalado **viertualenv**, utiliza el comando `pip install virtualenv`.

3. Abre el proyecto en tu editor de preferencia y habilita el entorno virtual usando el siguiente comando.

```powershell
cd .\venv\Scripts\ && ./activate && cd ../../
```

4. Instala las dependencias del proyecto usando el siguiente comando.

```powershell
pip install -r requirements.txt
```

5. Si utilizas Visual Studio Code como editor preferido, te recomendamos instalar las extenciones que se recomiendan al momento de abrir el proyecto, no es obligatorio este paso.

## Despliegue local

Recomendamos encarecidamente el uso de Docker como infraestructura local de despliegue ya que haber problemas con ciertas dependencias del proyecto que no son compatibles con sistemas Windows como los son [Gunicorn](https://gunicorn.org/).

### Configuracion previa

1. Antes de lanzar la aplicacion necesitas crear las migraciones de la base de datos.

```powershell
  # Sobre el directorio raiz -> AgroVar, debes hacer lo siguiente:
  python manage.py migrate

  # Si ocurre que no se han creado correctamente los modelos, haz lo siguiente:
  python manage.py migrate api

  # Una vez haya terminado satisfactoriamente el comando, debes hacer lo siguiente:
  python manage.py makemigrations
```

2. Luego necesitas configurar los archivos estaticos que necesitan servirse hacia los clientes.

```powershell
# Sobre el directorio raiz -> AgroVar, debes hacer lo siguiente:
python manage.py collecstatic
```

3. Y para finalizar con esto, necesitaras revisar si tu sistema operativo presenta algun cortafuegos que impida correr una aplicacion en tu red local, si es asi deberas ir a la configuracion y desactivarlo. En Windows es probable que te pida ingresar tu contraseña o etc, para permitir correr la aplicacion.

### Ahora si, despliegue local

Por defecto la aplicacion tiene un usuario administrador que por un consenso entre los desarrolladores y el jefe del projecto, se mantendra como tal sin modificar.

Es por ello que si quieren usar el panel de administrador por qualquier motivo deberan crear un usuario administrador personal, para ello deben tener en cuenta la siguiente forma:

`admin-<cuatro ultimos numeros del DNI>`

De esta forma se mantiene una froma mas ordenada y segura sobre quienes tiene acceso a la base de datos.

1. Registrar la contraseña

```powershell
  # Crea tu usuario con su contraseña y que sea segura :).
  python manage.py createsuperuser
```

2. Inicia el servidor

```powershell
  python manage.py runserver
```

3. Abre Chrome

Dirigete hacia [aqui](localhost:8000/admin) y verifica que el servidor funciona correctamente.

Puedes ver en los logs del terminal donde corriste el comando, si hubo algun error durante el proceso.
