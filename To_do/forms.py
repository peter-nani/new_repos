from .models import To_Do
from django.forms import ModelForm

class do_it_f(ModelForm):
    #throw the model to replicate the form
    class Meta():
        model = To_Do
        fields = '__all__'