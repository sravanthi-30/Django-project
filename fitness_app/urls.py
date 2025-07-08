# # fitness_app/urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('generate/', views.generate_fitness_plan_view, name='generate_plan'),
#     path('plan/<int:plan_id>/', views.view_fitness_plan_view, name='view_plan'),
# ]

# fitness_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.generate_fitness_plan_view, name='generate_plan'),
    path('plan/<int:plan_id>/', views.view_fitness_plan_view, name='view_plan'),
    # Add this line to make the root of 'fitness/' (or the project root)
    # direct to the generate view
    path('', views.generate_fitness_plan_view, name='home'), # <--- THIS IS ALSO A GOOD IDEA
]