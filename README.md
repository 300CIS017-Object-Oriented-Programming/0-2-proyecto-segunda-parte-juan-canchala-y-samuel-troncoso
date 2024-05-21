[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/6rk6xNey)
# Proyecto Segunda parte
## Instalacion
Instalar el proyecto en su computador local. Escriba desde la línea de comandos y ubicado en la carpeta raíz del proyecto pip install -r requirements.txt.
Ejecutar el juego localmente. Escriba en consola streamlit run  Su navegador debería abrir el juego


# Diagrama de Clases

```mermaid
classDiagram
    class Evento {
        +artista: Artista[]
        +nombre: String
        +fecha: Date
        +hora_apertura: Time
        +hora_show: Time
        +lugar_show: String
        +direccion: String
        +ciudad: String
        +estado: String
        +precioVentaRegular: Float
        +precioPreVenta: Float
        +estado_boleteria: String
        +aforoTotal: Int
        +codigo_cortesia: String
        +calcular_ingresos(precio_final: Float, cantidad_boletos: Int)
    }

    class EventoBar {
        +num_presentaciones: Int
    }

    class EventoTeatro {
        +alquiler: Float
    }

    class EventoFilantropico {
        +patrocinadores: Patrocinador[]
    }

    class Artista {
        +nombre: String
        +dni: String
        +email: String
        +celular: String
        +nombre_artistico: String
        +evento_nombre: String
    }

    class Patrocinador {
        +nombre: String
        +dni: String
        +email: String
        +celular: String
        +valor_aportado: Float
    }

    class Boleto {
        +evento: String
        +comprador: Comprador
        +como_se_entero: String
        +fase_venta: String
        +descuento: Int
        +precio_final: Float
        +cantidad: Int
        +fecha_compra: Date
    }

    class Comprador {
        +nombre: String
        +email: String
        +celular: String
    }

    Evento <|-- EventoBar
    Evento <|-- EventoTeatro
    Evento <|-- EventoFilantropico
    Evento "1" --> "*" Artista
    EventoFilantropico "1" --> "*" Patrocinador
    Boleto "1" --> "1" Comprador
    Boleto "*" --> "1" Evento

```