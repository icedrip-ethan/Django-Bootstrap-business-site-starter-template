from django import forms
from captcha.fields import ReCaptchaField


class ContactForm(forms.Form):
	full_name = forms.CharField(required=True)
	from_email = forms.EmailField(required = True)
	subject = forms.CharField(required=True)
	message = forms.CharField(widget=forms.Textarea, required=True)
	captcha = ReCaptchaField(required=False)