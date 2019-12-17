from django import forms

class ContactForm(forms.Form):
    contact_name=forms.CharField(label='Enter your name',required=True)
    contact_email=forms.EmailField(label='Enter your email-id',required=True)
    content=forms.CharField(label='Enter your Message',required=True,widget=forms.Textarea)
