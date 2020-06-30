from urllib import request
import json
from datetime import datetime, timedelta,date
# typing
from typing import Dict,List

def filter_tmcs(amount_uf:int,term_day:int) ->List:
	"""
	Filter data by type of operation that corresponds to the user request.

	The types of operations can be:
	
	#Operaciones reajustable moneda nacional
	type = 21 # Menores a 1 año
	type = 22 # Igual o mayor a 1 año y superior a 2000 Uf
	type = 24 # Igual o mayor a 1 año e inferior o igual a 2000 Uf

	#Operaciones no reajustable moneda nacional
	type = 25 # Menos de 90 dias y superior a 5000 Uf
	type = 26 # Menos de 90 días e inferior o igual a 5000 Uf
	type = 34 # 90 dias o mas y superior a 5000uf
	type = 35 # 90 dias o mas e inferior o igual a 5000 Uf y superior a 200 Uf
	type = 44 # 90 dias o mas e inferior o igual a 200 Uf y superior a 50 Uf
	type = 45 # 90 dias o mas inferior o igual a 50 Uf

	:param amount_uf: the amount in uf.
	:param term_day: term in days.
	:return: List with the type of operations corresponding to the days and amount.
	"""
	type_operation = list()
	# Reajustable moneda nacional
	if term_day < 365:
		type_operation.append('21')
	else:
		if amount_uf > 2000:
			type_operation.append('22')
		else:
			type_operation.append('24')
			
	# No Reajustable moneda nacional
	if term_day < 90:
		if amount_uf > 5000:
			type_operation.append('25')
		else:
			type_operation.append('26')
	else:
		if amount_uf > 5000:
			type_operation.append('34')
		elif amount_uf <= 5000 and amount_uf > 200:
			type_operation.append('35')
		elif amount_uf <= 200 and amount_uf > 50:
			type_operation.append('44')
		else:
			type_operation.append('45')
	
	# Operaciones Expresadas en moneda extranjera
	if amount_uf <= 2000:
		type_operation.append('41')
	else:
		type_operation.append('42')

	return type_operation

def get_tmcs(result:Dict,amount_uf:int,term_day:int) -> List:
	"""
	Returns TMCs that corresponds to the user's request.

	:param result: data obtained from the API
	:param amount_uf: the amount in uf
	:param term_day: term in days
	:return: List with the data of TMCs
	"""
	tmcs = list()
	type_operation = filter_tmcs(amount_uf,term_day)
	for i in type_operation:
		for data in result['TMCs']:
			if i == data['Tipo']:
				tmcs.append(data)
		
	return tmcs
	

def check_date(year:str,month:str,day:str)->str:
	"""
	Check date that sent user.

	:param year: year of TMC
	:para mont: month of TMC
	:para day: day of TMC
	:return: the year and month as string
	"""
	now = datetime.now().date()
	y = int(year)
	m = int(month)
	d = int(day)
	user_date = date(y, m, d)
	if user_date > now:
		y,m = now.strftime('%Y'),now.strftime('%m')
	else:
		base_url = f'https://api.sbif.cl/api-sbifv3/recursos_api/tmc/{year}/{month}?apikey=9c84db4d447c80c74961a72245371245cb7ac15f&formato=json'
		try:
			response = request.Request(base_url,method='GET')
			with request.urlopen(response) as f:
				response_code = f.getcode()
				if response_code == 200:
					response_data = f.read()
					data = json.loads(response_data)
					date_data = datetime.strptime(data['TMCs'][0]['Fecha'],"%Y-%m-%d")
					if date_data.day > d:
						new_date = user_date - timedelta(days=14)
						y,m = new_date.strftime('%Y'),new_date.strftime('%m')
						return [y,m]
					else:

						return [year,month]

		except Exception as er:
			return False
	return [y,m]
		

def get_data(year:str,month:str,day:str) -> Dict:
	"""
	Get data of the TMCs.

	:param year: year of TMC
	:para mont: month of TMC
	:para day: day of TMC
	:return: Dictionary with the response data.
	"""
	result_check_date = check_date(year=year,month=month,day=day)
	if result_check_date:
		year,month = result_check_date
		try:
			base_url = f'https://api.sbif.cl/api-sbifv3/recursos_api/tmc/{year}/{month}?apikey=9c84db4d447c80c74961a72245371245cb7ac15f&formato=json'
			response = request.Request(base_url,method='GET')
			with request.urlopen(response) as f:
				response_code = f.getcode()
				if response_code == 200:
					response_data = f.read()
					data = json.loads(response_data)
					return data
				else:
					return False
		except Exception as er:
			#if er.code:
			#    error_message = f' HTTP status: {er.code}'    
			return False
