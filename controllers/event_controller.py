import json
from models.EventoBar import EventoBar
from models.EventoFilantropico import EventoFilantropico
from models.EventoTeatro import EventoTeatro

def cargar_datos(filename):
    datos = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                datos.append(json.loads(line))
    except FileNotFoundError:
        pass
    return datos

def guardar_datos(filename, datos):
    with open(filename, 'w') as f:
        for dato in datos:
            json.dump(dato, f)
            f.write('\n')

def crear_evento_bar(artista, nombre, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, estado, precio_regular, precio_preventa, estado_boleteria, aforo, num_presentaciones, codigo_cortesia):
    return EventoBar(artista, nombre, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, estado, precio_regular, precio_preventa, estado_boleteria, aforo, num_presentaciones, codigo_cortesia)

def crear_evento_teatro(artista, nombre, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, estado, precio_regular, precio_preventa, estado_boleteria, aforo, alquiler, codigo_cortesia):
    return EventoTeatro(artista, nombre, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, estado, precio_regular, precio_preventa, estado_boleteria, aforo, alquiler, codigo_cortesia)

def crear_evento_filantropico(artista, nombre, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, estado, precio_regular, precio_preventa, estado_boleteria, aforo, patrocinadores, codigo_cortesia):
    return EventoFilantropico(artista, nombre, fecha, hora_apertura, hora_show, lugar, direccion, ciudad, estado, precio_regular, precio_preventa, estado_boleteria, aforo, patrocinadores, codigo_cortesia)

def actualizar_evento(eventos, evento_actualizado):
    for i, evento in enumerate(eventos):
        if evento['nombre'] == evento_actualizado['nombre']:
            eventos[i] = evento_actualizado
            break
    guardar_datos('eventos.json', eventos)
