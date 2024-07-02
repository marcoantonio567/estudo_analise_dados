import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

# Substitua o caminho abaixo pelo caminho do arquivo que você quer monitorar
arquivo = "desafio2.py"

class MeuHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print(f"Arquivo {event.src_path} modificado. Reiniciando o script...")
            subprocess.run(["python", arquivo])

if __name__ == "__main__":
    observer = Observer()
    observer.schedule(MeuHandler(), path=".")
    observer.start()
    print("Monitorando alterações no arquivo. Pressione Ctrl + C para sair.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
