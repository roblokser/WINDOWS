Локально (Windows, Python 3.12):
  pip install pyinstaller pillow
  pyinstaller --onefile --noconsole --name screamer --add-data "screen.png;." --add-data "scream.mp3;." --add-data "music.mp3;." main.py
  -> dist\screamer.exe

Через GitHub: залей папку в репозиторий -> вкладка Actions -> build-exe -> Artifacts -> screamer-exe.
Порядок: картинка + крик один раз, потом музыка по кругу. Esc закрывает программу.
