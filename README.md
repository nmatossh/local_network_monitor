# 🚀 Real-Time Network Monitor

Un panel de control dinámico y liviano para monitorear la latencia de red de múltiples dispositivos simultáneamente. Diseñado para funcionar como una aplicación de escritorio independiente en Windows.

## 🇪🇸 Características (Spanish)
- **Monitoreo en tiempo real**: Actualización constante de latencia (ping) con precisión de decimales.
- **Interfaz Visual**: 8 monitores organizados en una cuadrícula con gráficos de área históricos.
- **Personalización**: Diccionario de IPs para asignar nombres amigables (ej: "Router Cisco", "JOTUNHEIM").
- **Alertas por color**: Sistema de semáforo (Verde: OK, Amarillo: +100ms, Rojo: Timeout).
- **Modo App**: Script VBScript incluido para ejecutarlo sin ventanas de consola y sin barras de navegador.

- ## 🇺🇸 Features (English)
- **Real-time Monitoring**: Constant latency (ping) updates with decimal precision.
- **Visual Interface**: 8 monitors arranged in a grid with historical area charts.
- **Customizable**: IP dictionary to assign friendly names (e.g., "Main Server").
- **Color Alerts**: Traffic light system (Green: OK, Yellow: +100ms, Red: Timeout).
- **App Mode**: VBScript included to run as a standalone window without console or browser bars.

---

## 🛠️ Instalación / Installation

1. **Clonar/Descargar** este repositorio.
2. **Instalar dependencias** de Python:
   pip install streamlit pandas
3. **Configurar IPs**: Edita el diccionario `monitors` en `Dashboard.py` con tus direcciones locales o remotas.

## 🚀 Ejecución / Execution

### Windows (Modo App - Recomendado)
Simplemente haz doble clic en `Monitor.vbs`. Esto hará lo siguiente:
1. Inicia el servidor de Streamlit de forma invisible.
2. Abre una ventana dedicada de Chrome/Edge en modo aplicación.

### Manual
streamlit run Dashboard.py

---

## 📂 Estructura del Proyecto / Project Structure
* `Dashboard.py`: El núcleo de la aplicación en Python.
* `Monitor.vbs`: Script para lanzamiento silencioso en modo aplicación.
* `Kill_Monitor.bat`: Script para cerrar todos los procesos de fondo.
