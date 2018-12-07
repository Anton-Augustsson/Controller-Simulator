import requests

r = requests.get("http://10.46.205.67:8500/swagger/ui/index#!/Simulator/Simulator_SendCommand")#http://10.46.205.67:8500/Api/Simulator/SendCommand")
print(r)