from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .utils import hash_password,check_password
from .serializers import UsersSerializers,PreferencesSerializers,IngredientsSerializer,WeeklyMealPlanSerializer
from .models import Users,Preferences,Ingredients,WeeklyMealPlan

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



