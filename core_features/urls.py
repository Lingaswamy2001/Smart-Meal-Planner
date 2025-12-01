from django.urls import path
from .views import UsersView,PreferenceView,IngredientsView,LoginView,WeeklyMealPlanView

urlpatterns = [
    path('', LoginView.as_view()),
    path('register/', UsersView.as_view()),
    path('preferences/', PreferenceView.as_view()),
    path('preferences/<int:id>/', PreferenceView.as_view()),
    path("ingredients/", IngredientsView.as_view()),         
    path("ingredients/user/<int:user_id>/", IngredientsView.as_view()), 
    path("ingredients/<int:id>/", IngredientsView.as_view()), 
    path("mealplan/", WeeklyMealPlanView.as_view()),
    path("mealplan/<int:user_id>/", WeeklyMealPlanView.as_view()),
    path("mealplan/<int:id>/", WeeklyMealPlanView.as_view()),
]