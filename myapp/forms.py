from django import forms
from .models import Student, Lib
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput
                             (attrs={'class':'form-control'}),
                             max_length=30,
                             required=True)

    email=forms.CharField(widget=forms.EmailInput
                             (attrs={'class':'form-control'}),
                             max_length=30,
                             required=True)

    password=forms.CharField(widget=forms.PasswordInput
                             (attrs={'class':'form-control'}),
                             max_length=30,
                             required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput
                            (attrs={'class': 'form-control'}),
                            label="Confirm your password",
                            max_length=30,
                            required=True)

    class Meta:
        model = User
        fields = ['username','email','password','confirm_password']						

	


class StudentForm(forms.ModelForm):
	age = forms.IntegerField() 
	class Meta: 
		model = Student
		fields = "__all__"
	
	def clean_age(self):
		a = self.cleaned_data['age']
		if not a<0 and a>100:
			raise forms.ValidationError("Invalid Age")
		return a	

class LibForm(forms.ModelForm):
	class Meta:
		model = Lib
		fields  = "__all__"