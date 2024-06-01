import streamlit as st
import json
import bcrypt
import pandas as pd  

hashed_password = b'$2b$12$bPDofRXQDO4o79sPH2yzEujdSnVkNJLo.VSUqBKLTmTNeP7127ZGK'  

def mostrar_pagina_inicio():
    st.title("Bienvenido a Phoenix Eventos")

    st.header("Cambio de Tipo de Usuario")
    tipo_usuario_actual = st.session_state.get('tipo_usuario', 'usuario')
    st.write(f"Tipo de usuario actual: {tipo_usuario_actual}")

    if tipo_usuario_actual == 'usuario':
        contrasena = st.text_input("Ingrese la contraseña de administrador:", type="password")
        if st.button("Cambiar a Administrador"):
            if contrasena:
                # Verificar la contraseña
                if bcrypt.checkpw(contrasena.encode('utf-8'), hashed_password):
                    st.session_state['tipo_usuario'] = 'administrador'
                    st.success("Cambio a administrador exitoso.")
                    st.experimental_rerun()
                else:
                    st.error("Contraseña incorrecta")
    else:
        if st.button("Cambiar a Usuario"):
            st.session_state['tipo_usuario'] = 'usuario'
            st.success("Cambio a usuario exitoso.")
            st.experimental_rerun()

    st.header("Ingreso al Evento")

    def cargar_datos(filename):
        datos = []
        try:
            with open(filename, 'r') as f:
                for line in f:
                    datos.append(json.loads(line))
        except FileNotFoundError:
            st.error(f"No se encontraron datos en {filename}.")
        return datos

    boletos = cargar_datos('boletos.json')

    if boletos:
        df_boletos = pd.DataFrame(boletos)
        
        eventos_disponibles = df_boletos['evento'].unique()
        evento_seleccionado = st.selectbox("Selecciona un evento", eventos_disponibles)
        
        if evento_seleccionado:
            df_boletos_evento = df_boletos[df_boletos['evento'] == evento_seleccionado]
            
            compradores_disponibles = df_boletos_evento['comprador'].apply(lambda x: x['nombre']).unique()
            comprador_seleccionado = st.selectbox("Selecciona un comprador", compradores_disponibles)
            
            if comprador_seleccionado:
                df_boletos_comprador = df_boletos_evento[df_boletos_evento['comprador'].apply(lambda x: x['nombre']) == comprador_seleccionado]
                st.write(f"Boletas compradas por {comprador_seleccionado}:")
                st.write(df_boletos_comprador[['cantidad', 'fecha_compra']])
                
                cantidad_boletos = df_boletos_comprador['cantidad'].sum()
                st.write(f"Total de boletas compradas: {cantidad_boletos}")
                
                personas_llegadas = st.number_input("Número de personas que llegaron", min_value=0, max_value=int(cantidad_boletos))
                
                if st.button("Verificar Ingreso"):
                    if personas_llegadas <= cantidad_boletos:
                        st.success(f"Ingreso verificado para {personas_llegadas} personas de {cantidad_boletos} boletas compradas.")
                    else:
                        st.error("El número de personas que llegaron excede el número de boletas compradas.")

    st.write("© 2024 Juan Canchala y Samuel Troncoso. All Rights Reserved.")
