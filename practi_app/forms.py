from django import forms





class my_form(forms.Form):
    name = forms.CharField(max_length= 10)
    surname = forms.CharField(max_length = 12 )



    def __str__(self):
        return self.name
