from django import forms

class RegisterForm(forms.Form):
	username = forms.CharField(
		required=True, 
		min_length=4, 
		max_length=50,
		widget=forms.TextInput(
			attrs={
				'class'			: 'form-control',
				'id'   			: 'username',
			}
		)
	)
	email		= forms.EmailField(
		required=True, 
		widget=forms.TextInput(
			attrs={
				'class'			: 'form-control',
				'id'   			: 'email',
				'placeholder'  : 'email@dominio.com'
			}
		)
	)
	password = forms.CharField(
		required=True, 
		widget=forms.PasswordInput(
			attrs={
				'class'			: 'form-control',
				'id'   			: 'password'
			}
		)
	)