from django import forms

class IssueForm(forms.Form):
    name = forms.CharField(label='Seu nome', initial='',max_length=50)
    localization = forms.CharField(label='AP/vaga (ex.: 315/F)', initial='', max_length=5)
    iniciativa = forms.ChoiceField(label='iniciativa (ex.: RedeCasd)', choices= (('1','RedeCasd'),('2','DOO'),('3','Casd')))
    description = forms.CharField(label='Descrição do problema', initial='',max_length=200)