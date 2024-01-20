from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo", max_length=100, widget=forms.TextInput(attrs={'class': 'input'}))
    description = forms.CharField(label="Descripcion", widget=forms.Textarea(attrs={'class': 'input'}))

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Project name", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))