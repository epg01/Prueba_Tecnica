# Prueba_Tecnica

[![LinkedIn][linkedin-shield]][linkedin-url]


[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/emmanuel-palacio/

<!-- Tabla de contenido -->
<details open="open">
  <summary>Tabla de contenido</summary>
  <ol>
    <li>
      <a href="#acerca-del-proyecto">Acerca de la prueba ténica</a>
      <ul>
        <li><a href="#construido-con">Construido con</a></li>
      </ul>
    </li>
    <li>
      <a href="#comencemos">Comenzamos</a>
      <ul>
        <li><a href="#prerequisito">Requisitos</a></li>
        <li><a href="#pasos-para-probarlo-en-tu-local">Pasos para probarlo en tu local</a></li>
      </ul>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## Acerca del proyecto
Extraer cierta información en un archivo pdf que contiene imagenes

### Construido con
El BackEnd se contruyo con:

* [Python](https://www.python.org/)
* [PostgreSQL](https://www.postgresql.org/)
* [Docker](https://www.docker.com/)

## Comencemos

### Prerequisito
Tener instalado docker y docker-compose

### Pasos para probarlo en tu local

Primero, clonar el repositorio: ``` git clone https://github.com/epg01/Prueba_Tecnica ```

Luego procedemos a contruir nuestras imagenes
 ``` cd  Prueba_Tecnica```
 ``` sudo docker-compose build ```

Una vez construido las imagenes, ponemos a correr nuestros contenedores
``` sudo docker-compose up -d ```

Luego debemos de crear nuestra base de datos, para ello ejecutamos el siguiente comando
``` make CreateDB ```

Por último debemos de enlazar Django con postgreSQL  
``` make MigrateDjango ```

Para poder ver si todos los contenedores se montaron correctamente, procedemos como sigue:
``` docker-compose ps -a ```

| Name           | Command                         |  State                 | Ports                                                 |
| :---           |     :---:                       |          -----         |:---                                                   |
| backpython     |  python3 /project/manage.py ... | up                     | 0.0.0.0:8000->8000/tcp,:::8000->8000/tcp              |
| posgres12      |  docker-entrypoint.sh postgres  | up                     | 0.0.0.0:5432->5432/tcp,:::5432->5432/tcp              |


Si por algún motivo el servidor no enciende, ejecutamos el siguiente comando: 

 ``` make RunServer ```
 
Para poder probar la extración de archivos tenemos tres rutas, ya que la extracción de archivos se hace de manera local  

**doc_path=/project/Docs/Doc2.pdf**

**doc_path=/project/Docs/Doc3.pdf**

**doc_path=/project/Docs/Doc4.pdf**

Para poder ver toda la información almecenada en la base de datos:

**table_name=EXTRACTION**

## Ejemplo

``` http://127.0.0.1:8000/extract/?doc_path=/project/Docs/Doc2.pdf ```
 
   
## Contacto

Your Name - [@SixTanDeveloper](https://twitter.com/SixTanDeveloper) - sixtandev@gmail.com

Project Link: [Technical test](https://github.com/epg01/PruebaTecnica)
