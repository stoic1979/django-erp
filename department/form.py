from django import forms

# class will use to create the form
class ComputerForm(forms.Form):
	c_id = forms.IntegerField(label = 'ID')
	name = forms.CharField(label = 'Name', max_length = 100)
	designation = forms.CharField(label = 'Designation', max_length = 100)
	profile = forms.CharField(label = 'Work Profile', max_length = 10)
	salary = forms.CharField(label = 'Salary', max_length = 50)
