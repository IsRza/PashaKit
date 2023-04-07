# from typing import Any
# import requests as req

# # response: req.Response = req.get('https://raw.githubusercontent.com/PB-Digital/PashaKit/main/Config.json')
# response: req.Response = req.get('https://raw.githubusercontent.com/RzaIs/Svelte-TS-Project/main/package.json', verify=False)

# if response.status_code == 200:
#     print('\n\033[1;31m' + 'Fetching latest version failed!\n')
#     exit(1)

# body: dict[str, Any] = response.json()

# body['version'] = '12.34.5' # Delete

# master_version: list[int] = [ int(i) for i in body['version'].split('.') ]

# print(master_version)


from sys import argv

argv.pop(0)

print(argv)
