# fitness_app/views.py
from django.shortcuts import render, redirect
from .forms import PlanGenerationForm
from .models import FitnessPlan, FitnessGoal, Exercise
import random

def generate_fitness_plan_view(request):
    if request.method == 'POST':
        form = PlanGenerationForm(request.POST)
        if form.is_valid():
            goal = form.cleaned_data['goal']
            experience_level = form.cleaned_data['experience_level']

            # --- Simple Plan Generation Logic (Customize this extensively!) ---
            # This is a very basic example. In a real app, you'd have more sophisticated logic.
            # You might fetch exercises based on difficulty, type, and goal.

            # Example: Fetch some exercises based on experience level
            suitable_exercises = Exercise.objects.filter(difficulty=experience_level)
            if not suitable_exercises.exists():
                suitable_exercises = Exercise.objects.all() # Fallback

            selected_exercises = random.sample(list(suitable_exercises), min(5, suitable_exercises.count())) # Pick 5 random exercises

            plan_text = f"<h1>Your {goal.name} Fitness Plan ({experience_level.capitalize()})</h1>"
            plan_text += "<p>Here's a sample plan to get you started:</p>"
            plan_text += "<ul>"
            for i, exercise in enumerate(selected_exercises):
                plan_text += f"<li><strong>Day {i+1}:</strong> {exercise.name} - {exercise.description} (Type: {exercise.get_exercise_type_display()})</li>"
            plan_text += "</ul>"
            plan_text += "<p>Remember to consult a professional before starting any new fitness program.</p>"
            # --- End of Simple Plan Generation Logic ---

            fitness_plan = FitnessPlan.objects.create(
                user_goal=goal,
                experience_level=experience_level,
                generated_plan_text=plan_text
            )
            return redirect('view_plan', plan_id=fitness_plan.id)
    else:
        form = PlanGenerationForm()
    return render(request, 'fitness_app/generate_plan.html', {'form': form})

def view_fitness_plan_view(request, plan_id):
    fitness_plan = FitnessPlan.objects.get(id=plan_id)
    return render(request, 'fitness_app/view_plan.html', {'plan': fitness_plan})

# Create your views here.
