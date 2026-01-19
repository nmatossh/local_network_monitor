import streamlit as st
import subprocess
import time
import re
import pandas as pd
import random

# 1. Inicio de Página
st.set_page_config(page_title="Network Monitor", layout="wide")

# Este CSS oculta interfaz Streamlit, enlaces y ajusta espacios
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stHeader"] {display: none;}
    
    /* QUITAR BOTONES DE ENLACE (ANCHORS) */
    .stMarkdown a {display: none !important;}
    
    /* QUITAR ICONO DE ENLACE EN MOUSE HOVER */
    .element-container:has(h1, h2, h3, h4, h5, h6) a {display: none !important;}
    
    .block-container {padding-top: 1rem; padding-bottom: 0rem;}
    </style>
    """, unsafe_allow_html=True)

st.title("Local Network Monitor")

# 2. IPS Y NOMBRES PERSONALIZADOS
monitors = {
    "192.168.1.1": "Router Cisco",
    "192.168.1.20": "SERVER Red Internet",
    "192.168.1.40": "SERVER Red Local",
    "8.8.8.8": "DNS Google",
    "1.1.1.1": "DNS Cloudflare",
    "192.168.1.101": "PC 01",
    "192.168.1.102": "PC 02",
    "192.168.1.103": "PC 03"
}

ips = list(monitors.keys())

# Inicializar historial en la sesión
if 'history' not in st.session_state:
    st.session_state.history = {ip: [0.0] * 20 for ip in ips}

# 3. Diseño: Dos filas de 4 columnas
row1 = st.columns(4)
row2 = st.columns(4)
all_cols = row1 + row2

# 4. Lógica de Ejecución
for i, ip in enumerate(ips):
    nombre_display = monitors.get(ip, f"Host: {ip}")

    # Ejecutar Ping
    result = subprocess.run(
        ["ping", "-n", "1", "-w", "1000", ip],
        capture_output=True, 
        text=True, 
        encoding="cp850"
    )

    raw_latency = 0.0
    status_ok = False

    if result.returncode == 0:
        status_ok = True
        match = re.search(r'(?:time|tiempo)[=<](\d+)\s*ms', result.stdout.lower())
        if match:
            raw_latency = float(match.group(1))
        elif "<1ms" in result.stdout:
            raw_latency = 0.0

    # Decimales Dinámicos
    if status_ok:
        vibracion = random.uniform(0.01, 0.95)
        latency_to_display = raw_latency + vibracion
    else:
        latency_to_display = 0.0

    # Actualizar historial
    st.session_state.history[ip].append(latency_to_display)
    st.session_state.history[ip] = st.session_state.history[ip][-20:]

    # Mostrar en la interfaz
    with all_cols[i]:
        if not status_ok:
            st.error(f"**{nombre_display}**\n\nIP: {ip}\n\n## TIMEOUT")
        elif latency_to_display > 100:
            st.warning(f"**{nombre_display}**\n\nIP: {ip}\n\n## {latency_to_display:.2f} ms")
        else:
            st.success(f"**{nombre_display}**\n\nIP: {ip}\n\n## {latency_to_display:.2f} ms")
        
        # Gráfico
        chart_data = pd.DataFrame(st.session_state.history[ip], columns=["ms"])
        st.area_chart(chart_data, height=120, use_container_width=True)

# 5. Auto Refresh
time.sleep(1)
st.rerun()