[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/6rk6xNey)
# Proyecto Segunda parte
## Instalacion
Instalar el proyecto en su computador local. Escriba desde la línea de comandos y ubicado en la carpeta raíz del proyecto pip install -r requirements.txt.
Ejecutar el juego localmente. Escriba en consola streamlit run  Su navegador debería abrir el juego


# Diagrama de Clases

```mermaid
classDiagram
    class Evento {
        +String nombre
        +String fecha
        +String hora_apertura
        +String hora_show
        +String lugar_show
        +String direccion
        +String ciudad
        +String estado
        +float precioVentaRegular
        +float precioPreVenta
        +int aforoTotal
        +String codigo_cortesia
        +List~Artista~ artistas
    }

    class Artista {
        +String nombre
        +String dni
        +String email
        +String celular
        +String nombre_artistico
        +String evento_nombre
    }

    class EventoBar {
        +int num_presentaciones
    }

    class EventoTeatro {
        +float alquiler
    }

    class EventoFilantropico {
        +List~Patrocinador~ patrocinadores
    }

    class Patrocinador {
        +String nombre
        +String dni
        +String email
        +String celular
        +float valor_aportado
    }

    class Persona {
        +String nombre
        +String dni
        +String email
        +String celular
    }

    class Cliente {
        +String nombre
        +String email
        +String celular
    }

    class Boleteria {
        +String evento
        +Cliente comprador
        +String como_se_entero
        +String fase_venta
        +float descuento
        +int cantidad
        +float precio_final
        +String fecha_compra
    }

    class controllers~event_controller~ {
        +cargar_datos(filename: String)
        +guardar_datos(filename: String, datos: List)
        +crear_evento_bar(artista: List~Artista~, nombre: String, fecha: String, hora_apertura: String, hora_show: String, lugar: String, direccion: String, ciudad: String, estado: String, precio_regular: float, precio_preventa: float, estado_boleteria: String, aforo: int, num_presentaciones: int, codigo_cortesia: String)
        +crear_evento_teatro(artista: List~Artista~, nombre: String, fecha: String, hora_apertura: String, hora_show: String, lugar: String, direccion: String, ciudad: String, estado: String, precio_regular: float, precio_preventa: float, estado_boleteria: String, aforo: int, alquiler: float, codigo_cortesia: String)
        +crear_evento_filantropico(artista: List~Artista~, nombre: String, fecha: String, hora_apertura: String, hora_show: String, lugar: String, direccion: String, ciudad: String, estado: String, precio_regular: float, precio_preventa: float, estado_boleteria: String, aforo: int, patrocinadores: List~Patrocinador~, codigo_cortesia: String)
        +actualizar_evento(eventos: List, evento_actualizado: Evento)
    }

    class controllers~game_controller~ {
        +iniciar_juego()
        +procesar_movimiento(jugador: String, movimiento: String)
        +verificar_ganador()
    }

    class controllers~gui_controller~ {
        +configurar_pagina(titulo: String, icono: String)
        +mostrar_imagenes()
    }

    class controllers~pdf_controller~ {
        +generar_pdf(evento: Evento, tipo_evento: String)
    }

    class pages~Autenticador~ {
        +mostrar_pagina_autenticador()
    }

    class pages~Boleteria~ {
        +mostrar_pagina_boleteria()
    }

    class pages~Dashboard~ {
        +mostrar_pagina_dashboard()
    }

    class pages~Evento~ {
        +mostrar_pagina_evento()
    }

    class pages~Reportes~ {
        +mostrar_pagina_reportes()
    }

    class view~main_view~ {
        +main()
    }

    Evento <|-- EventoBar
    Evento <|-- EventoTeatro
    Evento <|-- EventoFilantropico
    Evento "1" *-- "0..*" Artista
    EventoFilantropico "1" *-- "0..*" Patrocinador
    Persona <|-- Artista
    Persona <|-- Cliente
    Boleteria "1" *-- "1" Cliente
    controllers~event_controller~ --> Evento
    controllers~pdf_controller~ --> Evento
    pages~Evento~ --> controllers~event_controller~
    pages~Boleteria~ --> controllers~event_controller~
    pages~Dashboard~ --> controllers~event_controller~
    pages~Reportes~ --> controllers~event_controller~
    pages~Evento~ --> controllers~pdf_controller~
    pages~Boleteria~ --> controllers~pdf_controller~
    view~main_view~ --> pages~Evento~
    view~main_view~ --> pages~Boleteria~
    view~main_view~ --> pages~Dashboard~
    view~main_view~ --> pages~Reportes~
    view~main_view~ --> pages~Autenticador~
    pages~Evento~ --> controllers~gui_controller~

```