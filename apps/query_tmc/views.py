from django.shortcuts import render
from django.views import View
from .forms import TmcForm

class Index(View):
	def get(self,request):
		form = TmcForm()
		return render(request,"query_tmc/index.html",{'form':form})
		