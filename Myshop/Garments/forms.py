from django import forms

class ContactForm(forms.Form):
    contact_name=forms.CharField(label='Enter you Name', required=True)
    contact_email=forms.EmailField(label='Enter you Email', required=True)
    content=forms.CharField(label='Enter you message',required=True,widget=forms.Textarea)
    
