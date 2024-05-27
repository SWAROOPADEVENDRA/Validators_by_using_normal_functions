from typing import Any
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
    reemail=forms.EmailField()

    #botchatcher are two types.they are
    #-->human code -->it is insert the data into front end
    #-->automated software-->it is insert the data into source code.
    botchatcher=forms.CharField(widget=forms.HiddenInput,required=False)


    #form class object method
    #clean (it takes all input object)
    def clean(self):
        email=self.cleaned_data['email']
        reemail=self.cleaned_data['reemail']
        if email!=reemail:
            raise forms.ValidationError('email not matched')
    
    #clean_element(it takes only one input element)
    def clean_url(self):
        url=self.cleaned_data['url']
        if url[-1]=='n':
            raise forms.ValidationError('url started with')
    
    #clean_element for botchatcher 
    def clean_botchatcher(self):
        botchatcher=self.cleaned_data['botchatcher']
        if len(botchatcher)>0:
            raise forms.ValidationError('botchatcher length is > 0')
        
        
class Accessrecordforms(forms.Form):
    name=forms.ModelChoiceField(queryset=Webpage.objects.all())
    date=forms.DateField()
    author=forms.CharField()