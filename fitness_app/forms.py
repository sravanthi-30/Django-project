# fitness_app/forms.py
from django import forms
from .models import FitnessGoal, Exercise # Import models if needed for choices

class PlanGenerationForm(forms.Form):
    goal = forms.ModelChoiceField(queryset=FitnessGoal.objects.all(), label="Your Fitness Goal")
    experience_level = forms.ChoiceField(
        choices=[
            ('beginner', 'Beginner'),
            ('intermediate', 'Intermediate'),
            ('advanced', 'Advanced'),
        ],
        label="Your Experience Level"
    )
    # You could add more fields here like 'days per week', 'available equipment', etc.