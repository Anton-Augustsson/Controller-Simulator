import requests

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

#data = '{ \\ \n   "Id": 0, \\ \n   "Command": "s", \\ \n   "MessageNumber": "19", \\ \n   "Interval": 10, \\ \n   "Repetitions": 30 \\ \n }'
data = {'Id': 0, 'command': 's', 'MessageNumber': '19', 'Interval': 10, 'Repetitions': 30}

response = requests.put('http://10.46.205.67:8500/Api/Simulator/SendCommand', headers=headers, data=data)
print(response)

