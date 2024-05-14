import streamlit as game

game.set_page_config(
    page_title="Home",
    page_icon="😂"
)

game.title("Bienvenido al Sistema de Gestión de Eventos de Comedia")

# Introducción
game.write("Este sistema está diseñado para gestionar eventos de comedia, permitiendo a los administradores crear, editar y eliminar eventos, gestionar la boletería y generar reportes.")

game.header("Tipos de Eventos")
game.write("El sistema maneja tres tipos de eventos con características propias:")
game.markdown("- **Evento en Bar:** Los comediantes son pagados por presentarse.")
game.markdown("- **Evento en Teatro:** Se alquila el teatro y se retiene un porcentaje de la boletería.")
game.markdown("- **Evento Filantrópico:** Boletas gratuitas financiadas por patrocinadores.")

game.header("Criterios de Aceptación")
game.write("El sistema cumple con los siguientes criterios:")
game.markdown("- Gestión de tres tipos de eventos: Bar, Teatro y Filantrópico.")
game.markdown("- Definición de detalles del evento, estado y precios de boletas.")
game.markdown("- Gestión de boletería con verificación de disponibilidad y generación de boletas en PDF.")
game.markdown("---")
game.write("© 2024 Juan Canchala y Samuel Troncoso. Todos los derechos reservados.")
