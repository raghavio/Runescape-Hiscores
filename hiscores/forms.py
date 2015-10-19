from django import forms
from .models import Skills


class SearchForm(forms.Form):
    search = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'required': ''}),
        max_length=30, label=False)

    def clean_search(self):
        search = self.cleaned_data['search']
        try:
            Skills.objects.get(user_name=search)
        except Skills.DoesNotExist:
            raise forms.ValidationError("Player does not exist.")


class CompareForm(forms.Form):
    player1 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'required': ''}),
        max_length=30, label=False)
    player2 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'required': ''}),
        max_length=30, label=False)

    def clean_player1(self):
        player1 = self.cleaned_data['player1']
        try:
            Skills.objects.get(user_name=player1)
        except Skills.DoesNotExist:
            raise forms.ValidationError("Player does not exist.")
        return player1

    def clean_player2(self):
        player2 = self.cleaned_data['player2']
        try:
            Skills.objects.get(user_name=player2)
        except Skills.DoesNotExist:
            raise forms.ValidationError("Player does not exist.")
        return player2
