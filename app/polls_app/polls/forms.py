from django import forms


class PollsDetailForm(forms.Form):
    pk = forms.IntegerField()


class PollsVoteForm(forms.Form):
    choice = forms.IntegerField()
