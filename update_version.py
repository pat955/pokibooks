import toml
import re

def get_version_from_file():
    try:
        with open('version.txt', 'r') as file:
            version = file.readline().strip()
            print(version)
            return version
    except FileNotFoundError:
        print("version.txt not found.")
        return None

def update_pyproject_version(tag):
    pyproject_file = 'pyproject.toml'
    with open(pyproject_file, 'r') as file:
        pyproject_data = toml.load(file)

    pyproject_data['tool']['poetry']['version'] = tag.lstrip('v')

    with open(pyproject_file, 'w') as file:
        toml.dump(pyproject_data, file)
        
def update_setup_py_version(tag):
    setup_py_file = 'setup.py'
    with open(setup_py_file, 'r') as file:
        setup_py_data = file.read()

    new_setup_py_data = re.sub(r'__version__ = "[^"]+"', f'__version__ = "{tag}"', setup_py_data)
    new_setup_py_data = re.sub(r'version\s*=\s*"[^"]+"', f'version = "{tag}"', new_setup_py_data)

    with open(setup_py_file, 'w') as file:
        file.write(new_setup_py_data)
        
if __name__ == "__main__":
    version_tag = get_version_from_file()
    if version_tag:
        update_pyproject_version(version_tag)
        update_setup_py_version(version_tag)
    else:
        print("No version found in version.txt.")
