import streamlit as st

def pagina_inicio_sesion():
    st.title("Inicio de Sesión")
    username = st.text_input("Nombre de usuario")
    password = st.text_input("Contraseña", type="password")

    if username == "admin" and password == "adminpass":
        st.success("¡Bienvenido Admin!")
        return "admin"
    elif username == "usuario" and password == "userpass":
        st.success("¡Bienvenido Usuario!")
        return "usuario"
    else:
        st.error("Nombre de usuario o contraseña incorrectos.")
        return None

def pagina_admin():
    st.title("Página de Admin")
    st.write("Esta es la página de Admin. Aquí puedes realizar acciones de administración.")

def pagina_usuario():
    st.title("Página de Usuario")
    st.write("Esta es la página de Usuario. Aquí puedes ver información relevante para usuarios.")

if __name__ == "__main__":
    rol = pagina_inicio_sesion()

    if rol == "admin":
        pagina_admin()
    elif rol == "usuario":
        pagina_usuario()
