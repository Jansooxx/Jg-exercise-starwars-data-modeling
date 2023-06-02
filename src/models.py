import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

    # TABLAS DE FAVORITOS INICIO

class Planet_fav(Base):
    __tablename__ = 'planet_fav'
    id = Column(Integer, primary_key=True)
    planeta_id = Column(Integer,ForeignKey('planeta.id'))
    usuario_planeta = Column(Integer,ForeignKey('usuario.id'))

class Vehicle_fav(Base):
    __tablename__ = 'vehicle_fav'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    fav_vehicle = Column(Integer,ForeignKey('vehicle.id'))




class Personaje_fav(Base):
    __tablename__ = 'personaje_fav'
    id = Column(Integer, primary_key=True)
    personaje_id = Column(Integer, ForeignKey('personaje.id'))
    usuario_id = Column(Integer, ForeignKey('usuario.id'))

    # TABLAS DE FAVORITOS FINAL




class Personaje(Base):
    __tablename__ = 'personaje'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    fav_person = relationship('Personaje_fav', backref = 'personaje', lazy=True)



class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    fav_planet = relationship('Planet_fav', backref = 'planeta', lazy=True)



class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    crew = Column(String(250), nullable=False)
    vehicle_class = Column(String(250), nullable=False)
    fav_vehicle = relationship('Vehicle_fav', backref = 'vehicle', lazy=True)




class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    fav_user = relationship('Users_fav', backref = 'usuario', lazy=True)
    fav_user_character = relationship('Personaje_fav', backref = 'usuario', lazy=True)



    


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
