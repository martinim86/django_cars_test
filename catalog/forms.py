from django import forms
from .models import Cars
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.
from functools import partial


DateInput = partial(forms.DateInput, {'class': 'datepicker'})
    
class CarsForm(forms.ModelForm):
    # date_on = forms.DateTimeField(
    #     input_formats=['%Y/%m/%d'],
    #     widget=forms.DateInput(attrs={
    #         # 'data-target': '#datetimepicker1'
    #     })
    # )
    # date_off = forms.DateTimeField(
    #     input_formats=['%d/%m/%Y %H:%M'],
    #     widget=forms.DateTimeInput(attrs={
    #         'class': 'form-control datetimepicker-input',
    #         'data-target': '#datetimepicker2'
    #     })
    # )

    # date_on = forms.DateField(input_formats=['%d/%m/%Y'])
    class Meta:
        model = Cars
        fields = ('name', 'date_on','date_off')
    # renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']
        
        #Проверка того, что дата не выходит за "нижнюю" границу (не в прошлом). 
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        #Проверка того, то дата не выходит за "верхнюю" границу (+4 недели).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Помните, что всегда надо возвращать "очищенные" данные.
        return data