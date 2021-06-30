import requests
def add_test():
	params = {
		'status':'False',
		'taskname':'TEST'
	}

	data = requests.get('http://127.0.0.1:8000/add',params=params)

	print(data.json())


def get_all_test():


	data = requests.get('http://127.0.0.1:8000/get_all')

	print(data.json())


get_all_test()