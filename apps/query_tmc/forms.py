from django import forms
import datetime

def get_date():
        now = datetime.date.today()
        return now.strftime("%d-%m-%Y")

def get_year():
    now = datetime.datetime.now()
    years = [i for i in range(now.year,1980,-1)]
    return years

MONTHS = {
    1:('Enero'), 2:('Febrero'), 3:('Marzo'), 4:('Abril'),
    5:('Mayo'), 6:('Junio'), 7:('Julio'), 8:('Agosto'),
    9:('Septiembre'), 10:('Octubre'), 11:('Noviembre'), 12:('Diciembre')
}

class TmcForm(forms.Form):
    amount_uf = forms.IntegerField(label='Monto en uf:',min_value=1, widget=forms.NumberInput(attrs={'class': 'form-control', 'style': 'color:black', 'id': 'amount_uf', 'required': True,'placeholder':'UF'}))
    term_day = forms.IntegerField(label='Plazo en dias:',min_value=1, widget=forms.NumberInput(attrs={'class': 'form-control', 'style': 'color:black', 'id': 'term_day', 'required': True,'placeholder':'30'}))
    date_tmc = forms.DateField(error_messages={'invalid': 'Ingresa una fecha valida'},label='Fecha del TMC:',initial=datetime.date.today(), widget=forms.SelectDateWidget(months=MONTHS,years=get_year(),attrs={'class': 'form-control', 'style': 'color:black;', 'id': 'date_tmc', 'required': True}))