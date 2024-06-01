import streamlit as st

def mostrar_pagina_contacto():
    st.title("Contacto")
    st.subheader("¡Hablemos!")
    
    st.write("""
    En Phoenix Eventos, estamos aquí para ayudarte a crear momentos inolvidables. Ya sea que estés planeando una boda, un 
    concierto, un evento corporativo, o cualquier otra celebración, queremos saber de ti. ¡Contáctanos hoy mismo y hagamos 
    realidad tus ideas!
    """)

    st.subheader("Información de Contacto")
    
    st.markdown("""
    **Teléfono:**  
    📞 (123) 456-7890
    
    **Correo Electrónico:**  
    📧 info@phoenixeventos.com
    
    **Dirección:**  
    📍 Calle Falsa 123, Ciudad, País
    """)

    st.subheader("Síguenos en Redes Sociales")
    
    st.markdown("""
    **Instagram:**  
    📷 [@PhoenixEventos](https://www.instagram.com/phoenixeventos)
    
    **Facebook:**  
    👍 [Phoenix Eventos](https://www.facebook.com/phoenixeventos)
    
    **Twitter:**  
    🐦 [@Phoenix_Eventos](https://twitter.com/phoenix_eventos)
    """)

    st.subheader("Formulario de Contacto")
    st.write("""
    Completa el siguiente formulario y uno de nuestros representantes se pondrá en contacto contigo lo antes posible.
    """)
    
    with st.form("contact_form"):
        nombre = st.text_input("Nombre")
        email = st.text_input("Correo Electrónico")
        mensaje = st.text_area("Mensaje")
        submit_button = st.form_submit_button("Enviar")
        
        if submit_button:
            st.success("¡Gracias por contactarnos! Nos pondremos en contacto contigo pronto.")

    st.subheader("¡Hagamos de tu próximo evento un éxito!")
    st.write("""
    En Phoenix Eventos, cada evento es una oportunidad para crear algo extraordinario. Estamos emocionados de colaborar 
    contigo y hacer de tu próximo evento una experiencia inolvidable. ¡No dudes en ponerte en contacto con nosotros!
    """)

mostrar_pagina_contacto()
