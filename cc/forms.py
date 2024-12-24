from django import forms
from .models import Complaint, Student, Feedback
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from .models import Complaint, Branch, Category

class Complaint_form(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control rounded-input', 'placeholder': 'Enter Title'})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': '4', 'class': 'form-control rounded-input', 'placeholder': 'Enter Description'})
    )
    priority = forms.ChoiceField(
        choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')],
        widget=forms.Select(attrs={'class': 'form-control rounded-input'})
    )
    attachment = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    branch = forms.ModelChoiceField(
        queryset=Branch.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control rounded-input'}),
        empty_label="Select Branch"  # Optional placeholder for the dropdown
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control rounded-input'}),
        empty_label="Select Category"  # Optional placeholder for the dropdown
    )

    class Meta:
        model = Complaint
        fields = ['title', 'description', 'priority', 'attachment', 'branch', 'category']

class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'input'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

class Student_form(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('birth_date', 'branch',)

class Feedback_form(forms.ModelForm):
    feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': '10', 'cols': '80', 'class': 'input'}), label=False)
    
    class Meta:
        model = Feedback
        fields = ('feedback',)
from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['feedback']  # Adjust fields based on your model

