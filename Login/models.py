from django.db import models
from django import forms

class Country(models.Model):
    Name = models.CharField(max_length=100, null=True)
    IsoCode = models.CharField(max_length=2, null=True)
    IsActive = models.BooleanField(default=False)

    class Meta:
        db_table = 'Country'

class CountryForm(forms.ModelForm):
    CountryName = forms.CharField(max_length=100)
    CountryID = forms.CharField(max_length=100)
    class Meta:
        model = Country
        fields = ['Name']