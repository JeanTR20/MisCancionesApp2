import datetime
import unittest
import random

from faker import Faker

from src.logica.coleccion import Coleccion
from src.modelo.album import Album,Medio
from src.modelo.cancion import Cancion,AlbumCancion
from src.modelo.interprete import Interprete
from src.modelo.declarative_base import Session
from fake_providers import InterpreteNombreProvider, InterpreteTexto_curiosidadesProvider

class interpreteTestCaseFake(unittest.TestCase):
    def setUp ( self ) :
        self.logica = Coleccion()
        self.session = Session ( )
        self.data_factory = Faker ( )

        # Generación de datos con libreria Faker
        self.data_factory.add_provider ( InterpreteNombreProvider )
        self.data_factory.add_provider ( InterpreteTexto_curiosidadesProvider )

        self.data=[]
        self.interprete=[]
        for i in range ( 0 , 2 ) :
            self.data.append(
                (
                    self.data_factory.unique.interpreteNombre ( ),
                    self.data_factory.interpreteTexto_curiosidades ( ),
                )
            )
            self.interprete.append(
                Interprete(
                    nombre = self.data[ -1 ][ 0 ] ,
                    texto_curiosidades = self.data[ -1 ][ 1 ] ,
                    cancion = [ ]
                )
            )
            self.session.add ( self.interprete[ -1 ] )

        '''
            Persiste los objetos
            En este setUp no se cierra la sesión para usar
            los albumes en las pruebas
        '''
        self.session.commit ( )
        #self.session.close()

    def tearDown ( self ) :
        self.session = Session ( )

        busqueda_interprete = self.session.query ( Interprete ).all ( )
        for interprete in busqueda_interprete :
            self.session.delete ( interprete )

        self.session.commit()
        self.session.close()

    def test_constructor ( self ) :
        for interprete , dato in zip ( self.interprete , self.data ) :
            self.assertEqual ( interprete.nombre , dato[ 0 ] )
            self.assertEqual ( interprete.texto_curiosidades , dato[ 1 ] )

    def test_agregar_interprete ( self ) :
        interpreteNombre=self.data_factory.unique.interpreteNombre ( )
        interpreteTexto_curiosidades=self.data_factory.interpreteTexto_curiosidades ( )

        resultado=self.logica.agregar_album(interpreteNombre, interpreteTexto_curiosidades)

        self.assertEqual ( resultado , True )

    def test_agregar_interprete1 ( self ) :
        self.data.append (
            (
                self.data_factory.unique.interpreteNombre ( ) ,
                self.data_factory.interpreteTexto_curiosidades ( )
            )
        )
        resultado = self.logica.agregar_interprete (
            nombre = self.data[ -1 ][ 0 ] ,
            texto_curiosidades = self.data[ -1 ][ 1 ])

        self.assertEqual ( resultado , True )

