import random
from datetime import datetime
from datetime import timedelta
from src.modelo.album import Medio
from faker import Faker

from faker.providers import BaseProvider

    # datos de la tabla album
class AlbumTituloProvider(BaseProvider):
    def albumTitulo(self):
        albumesTitulo = ['Latin Jazz Compilation', 'Bandas sonoras famosas', 'The Dark Side of the Moon', 'The Bodyguard', 'Rumours', 'Saturday Night Fever', 'El fantasma de la ópera', 'Come on Over']
        return random.choice(albumesTitulo)

class AlbumAnioProvider(BaseProvider):
    def albumAnio(self):
        anio = [2018, 2019, 2020, 2021]
        return random.choice(anio)

class AlbumDescripcionProvider(BaseProvider):
    def albumDescripcion(self):
        descripcion = ["Album original", "Compilación"]
        return random.choice(descripcion)

class AlbumMedioProvider(BaseProvider):
    def albumMedio(self):
        self.medios = [ Medio.CD , Medio.CASETE , Medio.DISCO ]
        return random.choice(self.medios)

class AlbumFechaProvider(BaseProvider):
    def AlbumFecha(self):
        new_date = datetime(2019, 2, 28, 00, 00, 00, 00000)
        fecha = [new_date, new_date + timedelta(days=-1), new_date + timedelta(days=-2)]
        return random.choice(fecha)


    # datos de la tabla cancion
class cancionTituloProvider(BaseProvider):
    def cancionTitulo(self):
        cancionesTitulo = ['Forced Displacement', 'Green Sky', 'Alegría', 'Caravan']
        return random.choice(cancionesTitulo)

class CancionMinutosProvider(BaseProvider):
    def cancionMinutos(self):
        minutos = [2, 3, 4]
        return random.choice(minutos)

class CancionSegundosProvider(BaseProvider):
    def cancionSegunndos(self):
        segundos = [20, 40, 60]
        return random.choice(segundos)

class CancionCompositorProvider(BaseProvider):
    def cancionCompositor(self):
        compositor = [ "Samuel Torres", "Manuel Tadros", "Van Morrison", "Desconocido"]
        return random.choice(compositor)


    #datos de la tabla interprete
class InterpreteNombreProvider(BaseProvider):
    def interpreteNombre(self):
        nombre = ["Samuel Torres", "Aldo Gavilan", "Arturo Sandoval", "Cirque du Soleil"]
        return random.choice(nombre)

class InterpreteTexto_curiosidadesProvider(BaseProvider):
    def interpreteTexto_curiosidades(self):
        texto_curiosidades = ["Es colombiano y vive en NY", "Canto a Cuba", "No sabía quien era"]
        return random.choice(texto_curiosidades)