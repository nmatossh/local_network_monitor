Set WshShell = CreateObject("WScript.Shell")

' 1. Cierra cualquier proceso previo para evitar duplicados
WshShell.Run "taskkill /f /im streamlit.exe", 0, True

' 2. Inicia servidor de forma invisible
WshShell.Run "cmd /c streamlit run Dashboard.py --server.headless true", 0, False

' 3. Espera que el servidor esté listo
WScript.Sleep 100

' 4. Lanza  Chrome en modo APP con perfil aislado
strChrome = "chrome.exe --app=http://localhost:8501 --user-data-dir=%TEMP%\dash_monitor"
WshShell.Run strChrome, 1