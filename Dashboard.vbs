Set WshShell = CreateObject("WScript.Shell")

' 1. Cerramos cualquier proceso previo para evitar duplicados
WshShell.Run "taskkill /f /im streamlit.exe", 0, True

' 2. Iniciamos el servidor de forma invisible
WshShell.Run "cmd /c streamlit run Dashboard.py --server.headless true", 0, False

' 3. Esperamos a que el servidor esté listo
WScript.Sleep 100

' 4. Abrimos Chrome en modo APP con un perfil aislado
' Esto evita que se abra como pestaña en tu Chrome normal
strChrome = "chrome.exe --app=http://localhost:8501 --user-data-dir=%TEMP%\dash_monitor"
WshShell.Run strChrome, 1