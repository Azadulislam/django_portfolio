from django import forms


class ContactForm(forms.Form):
    clases = 'form-control form-input'
    name = forms.CharField(
        label= "Name",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class':clases,
            'placeholder':'Name *'
            })
    )
    email = forms.EmailField(
        label= "Email",
        max_length=100,
        required=True,
        widget=forms.EmailInput(attrs={
            'class':clases,
            'placeholder':'Email *'
            })
    )
    subject = forms.CharField(
        label= "Subject",
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={
            'class':clases,
            'placeholder':'Subject *'
            })
    )
    message = forms.CharField(
        label= "Message",
        required=True,
        widget=forms.Textarea(attrs={
            'class':clases,
            'placeholder':'Message *'
            })
    )
