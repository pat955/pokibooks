import toml
import re
import argparse

def update_pyproject_version(tag):
    pyproject_file = 'pyproject.toml'
    with open(pyproject_file, 'r') as file:
        pyproject_data = toml.load(file)

    pyproject_data['tool']['poetry']['version'] = tag.lstrip('v')

    with open(pyproject_file, 'w') as file:
        toml.dump(pyproject_data, file)


def main():
    parser = argparse.ArgumentParser(description="Update version in pyproject.toml and setup.py.")
    parser.add_argument('version', type=str, help='The version to set, e.g., v0.1.4')
    
    args = parser.parse_args()
    version_tag = args.version

    # You might want to validate the version format here if needed
    update_pyproject_version(version_tag)

if __name__ == "__main__":
    main()
