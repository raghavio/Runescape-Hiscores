from django import forms
from django.core.exceptions import FieldError
from .models import Skills


class SearchForm(forms.Form):
    search = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'required': ''}),
        max_length=12, label=False)

    def clean_search(self):
        search = self.cleaned_data['search']
        try:
            Skills.objects.get(user_name__iexact=search)
        except Skills.DoesNotExist:
            raise forms.ValidationError("Player does not exist.")


class CompareForm(forms.Form):
    player1 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'required': ''}),
        max_length=12, label=False)
    player2 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'required': ''}),
        max_length=12, label=False)

    def clean_player1(self):
        player1 = self.cleaned_data['player1']
        try:
            Skills.objects.get(user_name__iexact=player1)
        except Skills.DoesNotExist:
            raise forms.ValidationError("Player does not exist.")
        return player1

    def clean_player2(self):
        player2 = self.cleaned_data['player2']
        try:
            Skills.objects.get(user_name__iexact=player2)
        except Skills.DoesNotExist:
            raise forms.ValidationError("Player does not exist.")
        return player2


class SearchRankForm(forms.Form):
    search_rank = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rank', 'required': ''}),
        max_length=30, label=False)
    skill_exp = forms.CharField(widget=forms.HiddenInput())

    def clean_search_rank(self):
        rank = self.cleaned_data['search_rank']
        skill_exp = self.data['skill_exp']
        try:
            rank = max(int(rank), 1)  # Take to first rank if negative
            user_name = Skills.objects.order_by("-%s" % skill_exp).values("user_name")[rank - 1]['user_name']
        except IndexError:
            raise forms.ValidationError("That rank does not exist.")
        except FieldError:
            raise forms.ValidationError("Oops, please try again.")
        except ValueError:
            raise forms.ValidationError("Enter a valid number.")
        return user_name

