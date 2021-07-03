import requests
from pprint import pprint

def add_test():

	params = {
		'id':5,
		'status':'False',
		'taskname':'bajariladigan ish',
		'description':'nimalar qilish kerak'
	}

	data = requests.get('http://127.0.0.1:8000/add',params=params)

	pprint(data.json())


def get_all_test():


	data = requests.get('http://127.0.0.1:8000/get_all')

	pprint(data.json())

def remove(ID):
	params = {
		'id':ID
	}
	data = requests.get(f'http://127.0.0.1:8000/remove',params=params)
	print(data.json())

def update(idx):

	params = {
		'id':idx,
		'status':'False',
		'taskname':'update taskname',
		'description':'update description'
	}

	data = requests.get('http://127.0.0.1:8000/update',params=params)

	pprint(data.json())

# update(5)
get_all_test()
# add_test()
# remove(12)