import toml
from version import NEW_VERSION

def update_pyproject_version(tag):
    pyproject_file = 'pyproject.toml'
    with open(pyproject_file, 'r') as file:
        pyproject_data = toml.load(file)

    pyproject_data['tool']['poetry']['version'] = tag.lstrip('v')

    with open(pyproject_file, 'w') as file:
        toml.dump(pyproject_data, file)
        
if __name__ == "__main__":
    update_pyproject_version(NEW_VERSION)
   
