import streamlit as game
import datetime
from models.EventoBar import EventoBar
from models.EventoFilantropico import EventoFilantropico
from models.EventoTeatro import EventoTeatro
from models.Patrocinador import Patrocinador
from models.Artista import Artista


game.set_page_config(
    page_title="Eventos",
    page_icon="😂"
)
eventosbar = []
eventoteatro = []
eventofilantropico = []

artistaslist = []


game.title("Aqui estan nuestros eventos")

col1, col2, col3 =  game.columns(3)
with col1:
     game.image(r"static\img1.png", caption="Evento Bar", use_column_width="auto")

with col2:
     game.image(r"static\img2.png", caption="Evento Teatro", use_column_width="auto")

with col3:
     game.image(r"static\img3.png", caption="Evento Filantropico",use_column_width="auto")


game.header("Crear evento")
game.subheader("¿Que se hace aca?")
game.markdown("Como su nombre indica, esta seccion esta destinada a la creacion de evetos de tres tipos, cada uno con sus caracteristicas distintas.")

option =  game.selectbox(
    "Selecciona el tipo de evento",
    ("Bar", "Teatro", "Filantropico")
)



game.title("Datos del evento")

col5, col6=  game.columns(2)
with col5:
    nombre =  game.text_input("Nombre del show", "Ingrese nombre del show")
with col6:
    fecha =  game.date_input("Fecha del show", datetime.date(2006, 9, 16))

col7, col8, col9 =  game.columns(3)

with col7:
    horaApertura =  game.time_input("Hora de apertura de puertas", value=None)
with col8:
    horaShow =  game.time_input("Hora del show", value=None)
with col9:
    lugarShow =  game.text_input("Nombre del lugar del evento", "Javeriana Cali")

col10, col11 =  game.columns(2)

with col10:
    direccion =  game. text_input("Direccion del evento", "Calle 20 # 11-30")
with col11:
    ciudad =  game.text_input("Ciudad del evento", "Yumbo")

estado =  game.selectbox(
    "Selecciona el estado del evento",
    ("realizado", "por realizar", "cancelado", "aplazado", "cerrado")

)

col13, col14, col15 =  game.columns(3)

with col13:
    precioVentaRegular =  game.number_input("Precio regular", value=None)
with col14:
    precioPreVenta =  game.number_input("Precio de preventa", value=None)
with col15:
    aforoTotal =  game.number_input("Aforo total", value=None)

estadoBoleteria = "vacio"

game.title("Datos del artista ")

col31, col32, col33 =  game.columns(3)
with col31:
    nombreartista =  game.text_input("Nombre Artista", "Daniel")
with col32:
    dniArtista =  game.text_input("Documento de identidad", "1001316869")
with col33:
    emailartista =  game.text_input("Email", "ejemplo@gmail.com")

col34, col35 =  game.columns(2)
with col34:
    celularartista =  game.text_input("Celular", "301257069")
with col35:
    artista =  game.text_input("Nombre artistico", "Rels B")


if  game.button("Añadir artista al evento"):
    artistaslist.append(Artista(nombreartista, dniArtista, emailartista, celularartista, artista, nombre))

if option == "Bar":
    numPresentaciones =  game.number_input("Numero de presentaciones del artista", value=None)

    if  game.button("Creae Evento Bar"):

        eventosbar.append(EventoBar(artista, nombre, fecha, horaApertura, horaShow, lugarShow, direccion, ciudad, estado, precioVentaRegular, precioPreVenta, estadoBoleteria, aforoTotal, numPresentaciones))
        artistaslist = []


#creacion de evento Teatro
if option == "Teatro":
    alquiler =  game.number_input("Alquiler del lugar", value=None)

    if  game.button("Creae Evento Teatro"):
        eventoteatro.append(EventoTeatro(artista, nombre, fecha, horaApertura, horaShow, lugarShow, direccion, ciudad, estado, precioVentaRegular, precioPreVenta, estadoBoleteria, aforoTotal, alquiler))
        artistaslist = []


#Creacion de evento filantropico
if option == "Filantropico":
    patrocinadorlist = []
    game.title("Datos patrocinador del evento")
    col16, col17 =  game.columns(2)
    with col16:
        nombrePatrocinadores =  game.text_input("Nombre del patrocinador", "Olive Biscuit")
    with col17:
        dni =  game.text_input("Documento de identidad", "1034304796")

    col18, col19, col20 =  game.columns(3)
    with col18:
        email =  game.text_input("Email", "mafalda_0_qgmail.com")
    with col19:
        celular =  game.text_input("celular", "321968481")
    with col20:
        valorAportado =  game.number_input("Aporte del patrocinador", value=None)

    col21, col22 =  game.columns(2)
    with col21:
        if  game.button("Añadir Patrocinador"):
            patrocinadorlist.append(Patrocinador(nombrePatrocinadores, dni, email, celular, valorAportado))
    with col22:
        if  game.button("Crear evento Filantropico"):
            eventofilantropico.append(EventoFilantropico(artista, nombre, fecha, horaApertura, horaShow, lugarShow, direccion, ciudad, estado, precioVentaRegular, precioPreVenta, estadoBoleteria, aforoTotal, patrocinadorlist))
            patrocinadorlist = []
            artistaslist = []

