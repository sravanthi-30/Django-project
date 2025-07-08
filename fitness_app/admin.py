# fitness_app/admin.py
from django.contrib import admin
from .models import FitnessGoal, Exercise, FitnessPlan # Import your models

# Register your models here.
admin.site.register(FitnessGoal)
admin.site.register(Exercise)
admin.site.register(FitnessPlan) # Also register FitnessPlan if you want to view generated plans

