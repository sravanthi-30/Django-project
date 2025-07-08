# fitness_app/models.py
from django.db import models

class FitnessGoal(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    exercise_type_choices = [
        ('strength', 'Strength Training'),
        ('cardio', 'Cardio'),
        ('flexibility', 'Flexibility'),
    ]
    exercise_type = models.CharField(max_length=20, choices=exercise_type_choices)
    difficulty_choices = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    difficulty = models.CharField(max_length=20, choices=difficulty_choices)

    def __str__(self):
        return self.name

class FitnessPlan(models.Model):
    user_goal = models.ForeignKey(FitnessGoal, on_delete=models.CASCADE)
    experience_level_choices = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    experience_level = models.CharField(max_length=20, choices=experience_level_choices)
    generated_plan_text = models.TextField() # To store the actual plan generated

    def __str__(self):
        return f"Plan for {self.user_goal.name} ({self.experience_level})"

# Create your models here.
