from django import forms
from .models import CasinoPaymentMethod, PaymentMethod, CasinoTag, Tag, Casino


class CasinoForm(forms.ModelForm):
    class Meta:
        model = Casino
        fields = '__all__'
        
        
class CasinoPaymentMethodForm(forms.ModelForm):
    class Meta:
        model = CasinoPaymentMethod
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'method' in self.fields:
            self.fields['method'].queryset = \
                 PaymentMethod.objects.all().order_by('method_type', 'name')


class CasinoTagForm(forms.ModelForm):
    class Meta:
        model = CasinoTag
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'tag' in self.fields:
            self.fields['tag'].queryset = Tag.objects.all().order_by('name')