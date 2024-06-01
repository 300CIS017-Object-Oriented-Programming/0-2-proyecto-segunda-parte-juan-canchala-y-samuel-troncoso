import pytest
import os
import json
from unittest import mock
from your_module import mostrar_pagina_evento, cargar_eventos, cargar_boletos, eliminar_evento, Artista, EventoBar

# Configuramos los datos de prueba
@pytest.fixture
def mock_eventos_file(tmp_path):
    eventos_path = tmp_path / "eventos.json"
    eventos_path.write_text(json.dumps([
        {"nombre": "Evento 1", "fecha": "2024-01-01", "hora_apertura": "18:00:00", "hora_show": "20:00:00", "lugar_show": "Lugar 1", "direccion": "Direccion 1", "ciudad": "Ciudad 1", "estado": "por realizar", "precio_regular": 100, "precio_preventa": 80, "aforo_total": 200, "codigo_cortesia": "CORTESIA1", "artistas": [{"nombre": "Artista 1", "nombre_artistico": "Nombre Artistico 1"}]}
    ]))
    return eventos_path

@pytest.fixture
def mock_boletos_file(tmp_path):
    boletos_path = tmp_path / "boletos.json"
    boletos_path.write_text(json.dumps([
        {"evento": "Evento 1", "nombre_comprador": "Comprador 1", "cantidad": 2}
    ]))
    return boletos_path

@mock.patch("your_module.open", new_callable=mock.mock_open, read_data='[]')
def test_cargar_eventos(mock_file, mock_eventos_file):
    eventos = cargar_eventos()
    assert isinstance(eventos, list)
    assert len(eventos) == 1
    assert eventos[0]["nombre"] == "Evento 1"

@mock.patch("your_module.open", new_callable=mock.mock_open, read_data='[]')
def test_cargar_boletos(mock_file, mock_boletos_file):
    boletos = cargar_boletos()
    assert isinstance(boletos, list)
    assert len(boletos) == 1
    assert boletos[0]["evento"] == "Evento 1"

def test_eliminar_evento(mock_eventos_file):
    eventos = [
        {"nombre": "Evento 1"},
        {"nombre": "Evento 2"}
    ]
    eventos = eliminar_evento(eventos, "Evento 1")
    assert len(eventos) == 1
    assert eventos[0]["nombre"] == "Evento 2"

def test_crear_artista():
    artista = Artista("Nombre Artista", "12345678", "email@ejemplo.com", "555-5555", "Nombre Artistico", "Evento")
    assert artista.nombre == "Nombre Artista"
    assert artista.nombre_artistico == "Nombre Artistico"

def test_crear_evento_bar():
    artista = Artista("Nombre Artista", "12345678", "email@ejemplo.com", "555-5555", "Nombre Artistico", "Evento")
    evento = EventoBar(artista, "Evento Bar", "2024-01-01", "18:00:00", "20:00:00", "Lugar", "Direccion", "Ciudad", "Estado", 100, 80, "Estado Boleteria", 200, 1, "CORTESIA")
    assert evento.nombre == "Evento Bar"
    assert evento.artista.nombre == "Nombre Artista"
