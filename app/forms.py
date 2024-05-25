from django import forms
from app.models import * 

def validate_for_a(value):
    if value[0]=='a':
        raise forms.ValidationError('started with a')
    
def validate_for_len(value):
    if len(value)<4:
        raise forms.ValidationError('Length should be max of 4')
    
def validate_for_email(value):
    if not value.endswith('@gmail.com'):
        raise forms.ValidationError('Email len shoud be max of 5')


class Topicforms(forms.Form):
    topic_name=forms.CharField(max_length=100,validators=[validate_for_a])
    
class Webpageforms(forms.Form):
    topic_name=forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField(max_length=100,validators=[validate_for_len])
    url=forms.URLField()
    email=forms.EmailField(validators=[validate_for_email])
    
class Accessrecordforms(forms.Form):
    name=forms.ModelChoiceField(queryset=Webpage.objects.all())
    date=forms.DateField()
    author=forms.CharField()