
import pathlib

def get_version():
    version_file = pathlib.Path(__file__).resolve().parent.parent / 'VERSION'
    if version_file.exists():
        with version_file.open('r') as f:
            return f.read().strip()
    else:
        return "Version file not found"
