from django.shortcuts import render
from django.views import View
from .forms import TmcForm
from .utils import get_data,get_tmcs
from datetime import datetime,date

class Index(View):


	def get(self,request):
		form = TmcForm()
		return render(request,"query_tmc/index.html",{'form':form})
		
	def post(self,request):
		context = dict()
		form = TmcForm(request.POST)
		if form.is_valid():
			amount_uf = form.cleaned_data['amount_uf']
			term_day = form.cleaned_data['term_day']
			date_tmc = form.cleaned_data['date_tmc']
			date_tmc_month = date_tmc.strftime('%m')
			date_tmc_day = date_tmc.strftime('%d')
			date_tmc_year = date_tmc.strftime('%Y')
			response = get_data(year=date_tmc_year,month=date_tmc_month,day=date_tmc_day)
			tmcs = get_tmcs(response,amount_uf=amount_uf,term_day=term_day)
			context['tmcs'] = tmcs
			context['date_request'] = date_tmc
			context['tmcs_fecha'] = datetime.strptime(tmcs[0]['Fecha'],"%Y-%m-%d")
			try:
				context['tmcs_hasta'] = datetime.strptime(tmcs[0]['Hasta'],"%Y-%m-%d")
			except KeyError:
				context['tmcs_hasta'] = False
			return render(request,"query_tmc/index.html",{'form':form,'data':context})
		else:
			return render(request,"query_tmc/index.html",{'form':form})
			
			