from django import forms
class NewDepartamentoForm(forms.Form):
    nomDepa = forms.CharField(max_length=50)
    areaDepa = forms.CharField(max_length=30)

    nomEmp = forms.CharField(max_length=50)