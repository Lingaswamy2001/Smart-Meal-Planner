from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .utils import hash_password,check_password
from .serializers import UsersSerializers,PreferencesSerializers,IngredientsSerializer,WeeklyMealPlanSerializer,RecipeSerializer
from .models import Users,Preferences,Ingredients,WeeklyMealPlan,Recipe

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class LoginView(View):
    def post(self,request):
        data = json.loads(request.body)
        if data.get('username') or data.get('password'):
            try:
                user = Users.objects.get(username = data['username'])
            except:
                return JsonResponse({"status":"invalid username"})
        else:
            return JsonResponse({"status":"invalid credentials"})
        if check_password(data['password'],user.password):
            return JsonResponse({"status":f"user {user.username} login successfully"})
        return JsonResponse({"status":"login failed"})


@method_decorator(csrf_exempt,name='dispatch')
class UsersView(View):
    def post(self,request):
        data = json.loads(request.body)
        print(data)
        if data.get('password'):
            data['password'] = hash_password(data['password'])
        print(data)
        sr = UsersSerializers(data = data)
        if sr.is_valid():
            sr.save()
            return JsonResponse({"status":"users registered successfully"})

        return JsonResponse({"status":"user registaration failed"})
    

@method_decorator(csrf_exempt,name='dispatch')
class PreferenceView(View):
    def get(self,request,id):
        try:
            preference = Preferences.objects.get(id = id)
        except:
            return JsonResponse({"status":"invalid user"})
        return JsonResponse({"status":200,"preference":preference.diet_type})
    
    def post(self,request):
        data = json.loads(request.body)
        sr = PreferencesSerializers(data = data)
        if sr.is_valid():
            sr.save()
            return JsonResponse({"status":"preference saved"})
        return JsonResponse({"status":"invalid preference"})

    def patch(self, request, id):
        try:
            preference = Preferences.objects.get(id=id)
        except Preferences.DoesNotExist:
            return JsonResponse({"status": "invalid user"})

        data = json.loads(request.body)
        sr = PreferencesSerializers(preference, data=data, partial=True)

        if sr.is_valid():
            sr.save()
            return JsonResponse({"status": "preference updated"})

        return JsonResponse({"status": "invalid preference update"})
    
    def delete(self, request, id):
        try:
            preference = Preferences.objects.get(id=id)
        except Preferences.DoesNotExist:
            return JsonResponse({"status": "invalid user"})

        preference.delete()
        return JsonResponse({"status": "preference deleted"})


@method_decorator(csrf_exempt, name='dispatch')
class IngredientsView(View):

    def get(self, request, user_id):
        ingredients = Ingredients.objects.filter(user_id=user_id)
        sr = IngredientsSerializer(ingredients, many=True)
        return JsonResponse({"status": 200, "ingredients": sr.data})

    def post(self, request):
        data = json.loads(request.body)
        sr = IngredientsSerializer(data=data)

        if sr.is_valid():
            sr.save()
            return JsonResponse({"status": "ingredient added"})

        return JsonResponse({"status": "invalid data", "errors": sr.errors})

    def patch(self, request, id):
        try:
            ingredient = Ingredients.objects.get(id=id)
        except Ingredients.DoesNotExist:
            return JsonResponse({"status": "ingredient not found"})

        data = json.loads(request.body)
        sr = IngredientsSerializer(ingredient, data=data, partial=True)

        if sr.is_valid():
            sr.save()
            return JsonResponse({"status": "ingredient updated"})

        return JsonResponse({"status": "update failed", "errors": sr.errors})

    def delete(self, request, id):
        try:
            ingredient = Ingredients.objects.get(id=id)
        except Ingredients.DoesNotExist:
            return JsonResponse({"status": "ingredient not found"})

        ingredient.delete()
        return JsonResponse({"status": "ingredient deleted"})
    

@method_decorator(csrf_exempt, name='dispatch')
class WeeklyMealPlanView(View):

    def post(self, request):
        data = json.loads(request.body)
        sr = WeeklyMealPlanSerializer(data=data)

        if sr.is_valid():
            sr.save()
            return JsonResponse({"status": "meal plan created"})
        
        return JsonResponse({"status": "invalid data", "errors": sr.errors})

    def get(self, request, user_id):
        try:
            plan = WeeklyMealPlan.objects.get(user_id=user_id)
        except WeeklyMealPlan.DoesNotExist:
            return JsonResponse({"status": "meal plan not found"})
        
        sr = WeeklyMealPlanSerializer(plan)
        return JsonResponse({"status": 200, "plan": sr.data})

    def patch(self, request, id):
        try:
            plan = WeeklyMealPlan.objects.get(id=id)
        except WeeklyMealPlan.DoesNotExist:
            return JsonResponse({"status": "meal plan not found"})

        data = json.loads(request.body)
        sr = WeeklyMealPlanSerializer(plan, data=data, partial=True)

        if sr.is_valid():
            sr.save()
            return JsonResponse({"status": "meal plan updated"})
        
        return JsonResponse({"status": "update failed", "errors": sr.errors})

    def delete(self, request, id):
        try:
            plan = WeeklyMealPlan.objects.get(id=id)
        except WeeklyMealPlan.DoesNotExist:
            return JsonResponse({"status": "meal plan not found"})

        plan.delete()
        return JsonResponse({"status": "meal plan deleted"})


@method_decorator(csrf_exempt, name="dispatch")
class RecipeView(View):

    def get(self, request, user_id=None, id=None):
        if id:
            try:
                recipe = Recipe.objects.get(id=id)
                sr = RecipeSerializer(recipe)
                return JsonResponse({"status": 200, "recipe": sr.data})
            except Recipe.DoesNotExist:
                return JsonResponse({"status": 404, "error": "Recipe not found"})

        if user_id:
            recipes = Recipe.objects.filter(user_id=user_id)
            sr = RecipeSerializer(recipes, many=True)
            return JsonResponse({"status": 200, "recipes": sr.data})

        return JsonResponse({"status": 400, "error": "Invalid request"})

    def post(self, request):
        data = json.loads(request.body)
        sr = RecipeSerializer(data=data)
        if sr.is_valid():
            sr.save()
            return JsonResponse({"status": 201, "message": "Recipe created successfully"})
        return JsonResponse({"status": 400, "errors": sr.errors})

    def patch(self, request, id):
        try:
            recipe = Recipe.objects.get(id=id)
        except Recipe.DoesNotExist:
            return JsonResponse({"status": 404, "error": "Recipe not found"})

        data = json.loads(request.body)
        sr = RecipeSerializer(recipe, data=data, partial=True)
        if sr.is_valid():
            sr.save()
            return JsonResponse({"status": 200, "message": "Recipe updated"})
        return JsonResponse({"status": 400, "errors": sr.errors})

    def delete(self, request, id):
        try:
            recipe = Recipe.objects.get(id=id)
        except Recipe.DoesNotExist:
            return JsonResponse({"status": 404, "error": "Recipe not found"})

        recipe.delete()
        return JsonResponse({"status": 200, "message": "Recipe deleted"})



