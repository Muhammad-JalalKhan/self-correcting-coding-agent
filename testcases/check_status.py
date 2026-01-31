import requests

try:
    response = requests.get('https://google.com')
    print(f'Status Code: {response.status_code}')
except ImportError:
    print('requests library is not installed. Installing now...')
    import subprocess
    subprocess.check_call(['pip', 'install', 'requests'])
    # Retry ater installations
    response = requests.get('https://google.com')
    print(f'Status Code: {response.status_code}')