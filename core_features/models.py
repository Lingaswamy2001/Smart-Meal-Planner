from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(null=False,max_length=50,unique=True)
    email = models.EmailField(null=False,max_length=70,unique=True)
    password = models.CharField(max_length=250,null=False)


class Preferences(models.Model):
    class Diet(models.TextChoices):
        VEGAN = 'VEGAN', 'vegan'
        VEG = 'VEG' , 'veg'
        NON_VEG = 'NON_VEG', 'non_veg'
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    diet_type = models.CharField(max_length=7,choices=Diet.choices,default=Diet.VEG)   


class Ingredients(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50) 


class WeeklyMealPlan(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    monday_breakfast = models.CharField(max_length=255, null=True, blank=True)
    monday_lunch = models.CharField(max_length=255, null=True, blank=True)
    monday_dinner = models.CharField(max_length=255, null=True, blank=True)

    tuesday_breakfast = models.CharField(max_length=255, null=True, blank=True)
    tuesday_lunch = models.CharField(max_length=255, null=True, blank=True)
    tuesday_dinner = models.CharField(max_length=255, null=True, blank=True)

    wednesday_breakfast = models.CharField(max_length=255, null=True, blank=True)
    wednesday_lunch = models.CharField(max_length=255, null=True, blank=True)
    wednesday_dinner = models.CharField(max_length=255, null=True, blank=True)

    thursday_breakfast = models.CharField(max_length=255, null=True, blank=True)
    thursday_lunch = models.CharField(max_length=255, null=True, blank=True)
    thursday_dinner = models.CharField(max_length=255, null=True, blank=True)

    friday_breakfast = models.CharField(max_length=255, null=True, blank=True)
    friday_lunch = models.CharField(max_length=255, null=True, blank=True)
    friday_dinner = models.CharField(max_length=255, null=True, blank=True)

    saturday_breakfast = models.CharField(max_length=255, null=True, blank=True)
    saturday_lunch = models.CharField(max_length=255, null=True, blank=True)
    saturday_dinner = models.CharField(max_length=255, null=True, blank=True)

    sunday_breakfast = models.CharField(max_length=255, null=True, blank=True)
    sunday_lunch = models.CharField(max_length=255, null=True, blank=True)
    sunday_dinner = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Recipe(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="recipes")
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    ingredients = models.TextField() 
    steps = models.TextField()      
    cooking_time = models.IntegerField(help_text="time in minutes", default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
