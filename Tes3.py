import requests

headers = {
    'Accept': 'application/json',
    'Authorization': 'Basic U1NWdXNlcjpSZXN0QDIwMTg=',
    'Content-type': 'application/vnd.vmware.vmw.rest-v1+json'
}
#RP7S41VI8V2FB70Q3BU8N90TBGJUKQL8

data = '{ \\ \n shutdown}'
response = requests.put('https://10.46.205.75:8697/api/vms/RP7S41VI8V2FB70Q3BU8N90TBGJUKQL8/power', headers=headers, data=data, verify=False)
print(response.json())
