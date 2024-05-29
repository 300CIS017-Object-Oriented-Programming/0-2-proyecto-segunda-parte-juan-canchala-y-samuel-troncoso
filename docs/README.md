[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/6rk6xNey)
# Manual de Instrucciones para Phoenix Eventos
## Instalacion

Instalar el proyecto en su computador local. Escriba desde la línea de comandos y ubicado en la carpeta raíz del proyecto pip install -r requirements.txt.
Ejecutar el juego localmente. Escriba en consola "python run.py" esto ejecutara streamlit y en breve observara la pagina 


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

# Guia de usuario 
contraseña para cambio a administrador: admin123
## Página de Inicio
**Descripción:** 
La página principal de Phoenix Eventos, donde se puede cambiar el tipo de usuario entre "Usuario" y "Administrador".
**Uso:** 
Seleccione el tipo de usuario o registre su ingreso a un evento.

## Página de Eventos (administrador)
**Descripción:** 
Aquí puede crear, modificar y eliminar eventos.
**Uso:**
Para crear un evento, seleccione el tipo de evento y complete los campos requeridos.
Para modificar un evento, seleccione el evento existente y realice los cambios necesarios.
Si un evento ya tiene boletos vendidos, no podrá eliminarlo ni modificar su estado a "realizado".

## Página de Boletería
**Descripción:** 
Permite la compra de boletos para los eventos disponibles.
**Uso:**
Seleccione un evento y complete la información del comprador.
Aplique descuentos y códigos de cortesía si es necesario.
Finalice la compra y descargue el recibo en formato PDF.

## Página de Dashboard
**Descripción:** 
Proporciona una vista general de los eventos y sus métricas.
**Uso:**
Filtre los eventos por rango de fechas.
Visualice las gráficas de cantidad de eventos por tipo y los ingresos totales por eventos.
Revise los ingresos totales para la casa y los artistas.

## Página de Reportes
**Descripción:** 
Genera reportes detallados de ventas, financieros y datos de los compradores y artistas.
**Uso:**
Revise la cantidad de boletos vendidos por tipo y los ingresos totales por preventa y venta regular.
Desglose los ingresos por tipo de pago y boletería.
Visualice los datos de los compradores con gráficos y descargue el informe en formato Excel.
Filtre por artista para ver los datos de sus eventos y descargue el reporte correspondiente.

## Página de Nosotros
**Descripción:** 
Información sobre Phoenix Eventos.
**Uso:** 
Lea sobre nuestra misión, visión y el equipo que hace posible Phoenix Eventos.

## Página de Contacto
**Descripción:** 
Información de contacto y redes sociales de Phoenix Eventos.
**Uso:**
Encuentre nuestro número de teléfono, dirección de correo electrónico y ubicación física.
Síganos en nuestras redes sociales: Instagram, Facebook y Twitter.
Complete el formulario de contacto para comunicarse con nosotros.

# Diagrama de secuencias
La intencion de este diagrama esque el usuario pueda ver como es un flujo tipico en nuestra aplicacion.

```mermaid
sequenceDiagram
    participant U as Usuario
    participant W as Web Browser
    participant S as Streamlit App
    participant EC as EventController
    participant DB as Database

    U->>W: Accede a la página de inicio
    W->>S: Solicita la página de inicio
    S->>EC: Verifica tipo de usuario
    EC->>S: Retorna tipo de usuario
    S->>W: Muestra página de inicio

    U->>W: Navega a la página de creación de eventos
    W->>S: Solicita la página de creación de eventos
    S->>W: Muestra formulario de creación de eventos

    U->>W: Llena y envía el formulario de creación de eventos
    W->>S: Envía datos del evento
    S->>EC: Valida y procesa datos del evento
    EC->>DB: Guarda evento en la base de datos
    DB->>EC: Confirma almacenamiento del evento
    EC->>S: Notifica éxito en la creación del evento
    S->>W: Muestra confirmación de creación de evento

    U->>W: Navega a la página de reporte de ventas
    W->>S: Solicita la página de reporte de ventas
    S->>EC: Solicita datos de ventas de boletos
    EC->>DB: Recupera datos de ventas de boletos
    DB->>EC: Retorna datos de ventas de boletos
    EC->>S: Envía datos de ventas de boletos
    S->>W: Muestra reporte de ventas de boletos

    U->>W: Navega a la página de reportes financieros
    W->>S: Solicita la página de reportes financieros
    S->>EC: Solicita datos financieros
    EC->>DB: Recupera datos financieros
    DB->>EC: Retorna datos financieros
    EC->>S: Envía datos financieros
    S->>W: Muestra reportes financieros

    U->>W: Navega a la página de contacto
    W->>S: Solicita la página de contacto
    S->>W: Muestra la página de contacto con la información relevante

```

# Cumplimiento de los requerimientos tecnicos

## Eventos
1. Se deben manejar 3 tipos de eventos en el sistema: evento en Bar, evento en Teatro y evento Filantrópico (boletería sin costo).
![Texto alternativo](ruta/a/la/imagen.jpg)
2. El sistema permite ingresar detalles del evento como artista o artistas del show, nombre, fecha, hora de apertura de puertas, hora del show, lugar, dirección y ciudad.
![Texto alternativo](ruta/a/la/imagen.jpg)
3. El sistema permite definir el estado del evento (realizado, por realizar, cancelado, aplazado, cerrado). Cambios en el estado "realizado" están restringidos.
![Texto alternativo](ruta/a/la/imagen.jpg)
4. El administrador puede definir precios de boletas para diferentes categorías y fases de venta (preventa y venta regular).
![Texto alternativo](ruta/a/la/imagen.jpg)
5. Se impide la eliminación de eventos con boletería vendida.
![Texto alternativo](ruta/a/la/imagen.jpg)
6. El sistema permite definir el aforo total del evento.
![Texto alternativo](ruta/a/la/imagen.jpg)
7. Ingreso al evento

## Boleteria

1. Se requieren datos del comprador y cómo se enteró del evento al vender una boleta.
2. El sistema verifica la disponibilidad de aforo antes de completar la venta.
3. El precio de la boleta varía según la fase de venta y aplicaciones de descuentos.
4. Las boletas de cortesía se pueden emitir con un precio de cero.
5. Generación de PDF con la boleta.

## Reportes

1. Reporte de Ventas de Boletas: Detalla cantidad de boletas vendidas por tipo (incluyendo cortesías) y los ingresos totales por preventa y venta regular.
2. Reporte Financiero: Desglosa los ingresos por tipo de pago y tipo de boletería.
3. Reporte de Datos de los Compradores: Ofrece información detallada de los compradores permitiendo análisis demográficos y de comportamiento para estrategias de marketing. Debe incluir al menos dos gráficas visualizando esta información (en Plotly) y estar disponible para descargar en formato Excel.
4. Reporte de Datos por Artista: Dado un artista (que se puede filtrar desde la interfaz gráfica) será posible reportar datos generales de sus eventos gestionados en el sistema. En los datos generales de cada evento deben estar cosas como (nombre del evento, fecha, lugar, cantidad de boletas vendidas, porcentaje de aforo cubierto).

## Dashboard

1. Dashboard con su rango de fechas.
2. Graficos