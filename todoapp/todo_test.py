import requests
params = {
	'status':'False',
	'taskname':'TEST'
}
data = requests.get('http://127.0.0.1:8000/add',params=params)
print(data.json())