from django import forms



class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=150, required=True)
    city = forms.CharField(max_length=50, required=True)
    zip_code = forms.CharField(max_length=10, required=True)
    address = forms.CharField(widget=forms.Textarea, required=True)




