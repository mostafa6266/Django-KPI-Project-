from django import forms
from .models import Data
from .models import Comments

class AddKPIForm(forms.Form):
    user = forms.ModelChoiceField(queryset=Data.objects.all(), label="User")
    points = forms.IntegerField(label="Points to Add")
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']