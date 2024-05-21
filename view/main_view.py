import streamlit as st
from controllers.gui_controller import configurar_pagina, mostrar_imagenes
from pages.Evento import mostrar_pagina_evento
from pages.Boleteria import mostrar_pagina_boleteria
from pages.Dashboard import mostrar_pagina_dashboard
from pages.Reportes import mostrar_pagina_reportes

configurar_pagina("Inicio", "🏠")

paginas = {
    "Inicio": mostrar_pagina_evento,
    "Boletería": mostrar_pagina_boleteria,
    "Dashboard": mostrar_pagina_dashboard,
    "Reportes": mostrar_pagina_reportes,
}

st.sidebar.title("Navegación")
seleccion = st.sidebar.radio("Ir a", list(paginas.keys()))

# Mostrar la página seleccionada
paginas[seleccion]()
