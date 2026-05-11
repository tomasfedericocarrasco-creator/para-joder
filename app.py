import streamlit as st
import random

# Configuración de la página
st.set_page_config(page_title="Pregunta importante", page_icon="❤️")

# Inicializar el estado de la posición del botón 'No' si no existe
if 'pos_no' not in st.session_state:
    st.session_state.pos_no = 1  # Columna por defecto
if 'pos_y' not in st.session_state:
    st.session_state.pos_y = 0  # Líneas de espacio vertical por defecto

# Si el usuario hace clic en "Sí"
if 'enamorado' not in st.session_state:
    st.session_state.enamorado = False

# --- LÓGICA DE PANTALLAS ---

if st.session_state.enamorado:
    st.balloons()
    st.title("❤️ ¡Lo sabía!")
    st.subheader("Ya sé que me amas y que te parezco guapísimo 😍")
    if st.button("Volver a empezar"):
        st.session_state.enamorado = False
        st.rerun()

else:
    st.title("¿Me amas? ❤️")

    # Creamos múltiples columnas para mover el botón de "No"
    cols = st.columns(5)

    # Botón SI (siempre en la columna 0)
    with cols[0]:
        if st.button("Sí", type="primary"):
            st.session_state.enamorado = True
            st.rerun()

    # Botón NO (se mueve de columna según el estado)
    with cols[st.session_state.pos_no]:
        st.write("\n" * st.session_state.pos_y)
        if st.button("No"):
            # Al hacer clic en No, cambia a una posición aleatoria (1 a 4)
            # para que nunca se solape con el "Sí" que está en la 0
            nueva_pos = random.randint(1, 4)
            st.session_state.pos_no = nueva_pos
            nueva_y = random.randint(0, 10)
            st.session_state.pos_y = nueva_y
            st.rerun()
