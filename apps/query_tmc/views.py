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
		form = TmcForm(request.POST)
		context = dict()
		if form.is_valid():
			now = datetime.now().date()
			amount_uf = form.cleaned_data['amount_uf']
			term_day = form.cleaned_data['term_day']
			date_tmc = form.cleaned_data['date_tmc']
			context['date_request'] = date_tmc
			if date_tmc > now:
				date_tmc = now
			date_tmc_month = date_tmc.strftime('%m')
			date_tmc_day = date_tmc.strftime('%d')
			date_tmc_year = date_tmc.strftime('%Y')
			response = get_data(year=date_tmc_year,month=date_tmc_month,day=date_tmc_day)
			if response:
				tmcs = get_tmcs(response,amount_uf=amount_uf,term_day=term_day)
				if tmcs:
					context['tmcs'] = tmcs
					context['tmcs_fecha'] = datetime.strptime(tmcs[0]['Fecha'],"%Y-%m-%d")
					try:
						context['tmcs_hasta'] = datetime.strptime(tmcs[0]['Hasta'],"%Y-%m-%d")
					except KeyError:
						context['tmcs_hasta'] = False
					return render(request,"query_tmc/index.html",{'form':form,'data':context})
			
			context['error_response'] = True
		
		return render(request,"query_tmc/index.html",{'form':form,'data':context})