from django import forms

from app.models import Visitor

class UpdateVisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = [
            'first_name',
            'last_name',
            'cpf',
            'birth_date',
            'ticket_date',
            'ticket_type'
        ]