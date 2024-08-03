import toml

def get_version_from_file():
    try:
        with open('version.txt', 'r') as file:
            version = file.read().strip()
            print(version)
            return version
    except FileNotFoundError:
        return None

def update_pyproject_version(version):
    pyproject_file = 'pyproject.toml'
    with open(pyproject_file, 'r') as file:
        pyproject_data = toml.load(file)

    pyproject_data['tool']['poetry']['version'] = version.lstrip('v')

    with open(pyproject_file, 'w') as file:
        toml.dump(pyproject_data, file)

if __name__ == "__main__":
    version = get_version_from_file()
    if version:
        update_pyproject_version(version)
    else:
        print("version.txt file not found.")
