import os
import sys
from pathlib import Path

class AutoImporter:
    def __init__(self, base_dir=None):
        # Establece el directorio base
        self.base_dir = Path(base_dir) if base_dir else Path.cwd()
        self.add_to_sys_path()

    def add_to_sys_path(self):
        # Recorre todos los subdirectorios del base_dir
        for dirpath, dirnames, filenames in os.walk(self.base_dir):
            # Añade cada subdirectorio a sys.path
            sys.path.append(dirpath)
            # Puedes imprimir cada directorio añadido si deseas
            print(f"Added to sys.path: {dirpath}")

# Ejemplo de uso
if __name__ == "__main__":
    # Al instanciar la clase, se añadirán los subdirectorios al sys.path
    importer = AutoImporter()
