from typing import Any
import json

def get_current_version() -> list[int]:
    config: dict[str, Any]
    with open('Config.json', 'r') as file:
        config = json.load(file)
    return config['version']

def main():
    print(f'version={get_current_version()}')

if __name__ == '__main__':
    main()