import streamlit as st

def mostrar_pagina_nosotros():
    st.title("Nosotros")
    st.subheader("Bienvenido a Phoenix Eventos")
    
    st.write("""
    En Phoenix Eventos, nos dedicamos a crear experiencias inolvidables. Somos una empresa líder en la organización y 
    gestión de eventos, ofreciendo una amplia gama de servicios para satisfacer todas las necesidades de nuestros clientes. 
    Con años de experiencia en el sector, nos hemos ganado una reputación de excelencia y profesionalismo.
    """)

    st.subheader("Nuestra Misión")
    st.write("""
    Nuestra misión es transformar cada evento en un momento mágico y memorable. Nos esforzamos por ofrecer un servicio 
    personalizado y de alta calidad, asegurando que cada detalle sea perfecto y que cada cliente quede completamente satisfecho.
    """)

    st.subheader("Nuestros Servicios")
    st.write("""
    Ofrecemos una variedad de servicios para cualquier tipo de evento, incluyendo:
    - **Eventos Corporativos:** Conferencias, seminarios, lanzamientos de productos y más.
    - **Bodas y Celebraciones:** Desde bodas íntimas hasta grandes recepciones.
    - **Conciertos y Festivales:** Organización de conciertos y festivales con artistas de renombre.
    - **Eventos Filantrópicos:** Galas benéficas, subastas y eventos para recaudar fondos.

    Contamos con un equipo de expertos en planificación y ejecución de eventos, equipados con las herramientas y la creatividad 
    necesarias para superar todas las expectativas.
    """)

    st.subheader("Nuestro Equipo")
    st.write("""
    En Phoenix Eventos, creemos que nuestro equipo es nuestro mayor activo. Nuestro equipo está compuesto por profesionales 
    apasionados y dedicados que trabajan incansablemente para garantizar el éxito de cada evento. Desde nuestros planificadores 
    de eventos hasta nuestro personal de soporte, todos están comprometidos a brindar un servicio excepcional.
    """)

    st.subheader("Contáctanos")
    st.write("""
    ¿Interesado en trabajar con nosotros? ¡Nos encantaría saber de ti! Puedes contactarnos a través de nuestro formulario de 
    contacto en la página web o llamarnos al (123) 456-7890. También puedes seguirnos en nuestras redes sociales para mantenerte 
    al tanto de nuestras últimas noticias y eventos.
    """)

    st.subheader("Únete a la Experiencia Phoenix")
    st.write("""
    En Phoenix Eventos, cada evento es una oportunidad para crear algo especial. Únete a nosotros y descubre por qué somos la 
    opción número uno para la organización de eventos. ¡Hagamos de tu próximo evento un éxito rotundo!
    """)

mostrar_pagina_nosotros()
