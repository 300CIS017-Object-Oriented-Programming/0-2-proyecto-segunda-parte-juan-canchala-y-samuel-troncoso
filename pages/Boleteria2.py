import streamlit as game

game.set_page_config(
    page_title="Boleteria",
    page_icon="😂"
)

col1, col2, col3 = game.columns(3)

game.title("Tipos de evento")

with col1:
    if game.button("Crear evento"):
        game.switch_page("your_app.py")
game.header("Esta es una prueba")
game.subheader("Esta es  prueba")
game.markdown("Este es un texto con **pruba** *Markdown*. de prueba")
