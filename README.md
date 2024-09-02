## Instrucciones

Para subir los archivos XML, usaremos este script

### 1. Conseguir credenciales

Copiar el archivo `.env.example` y llamar al nuevo archivo `.env`. 

Completar todas las credenciales que necesita.

### 2. Colocar archivos en la carpeta `/files`

Conseguirse los archivos XML y copiarlos a la carpeta

### 3. Preparar el ambiente

Usaremos virtual environment para no instalar infinitas cosas en el PC

```shell
python3 -m venv myenv
```

#### En MacOs

```shell
source myenv/bin/activate
```

#### En Windows

```shell
myenv\Scripts\activate
```

### 4. Instalar dependencias

Una vez que está activo el virtual env, instalamos las dependencias

```shell
pip install -r requirements.txt
```

### 5. Correr script

```shell
python3 main
```

#### Al terminar, se debe desactivar el ambiente

```shell
deactivate
```