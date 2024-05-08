from django.shortcuts import render,redirect
from . models import Recipe

# Create your views here.
def recipes(request):
    recipes=Recipe.objects.all()
    if request.GET.get("search"):
        recipes=Recipe.objects.filter(recipe_name__icontains=request.GET.get("search"))
    return render(request,'recipe.html',{'recipes':recipes})

def addRecipe(request):
    if request.method=="POST":
        recipe_name=request.POST.get("recipe_name")
        recipe_description=request.POST.get("recipe_description")
        recipe_image=request.FILES.get('recipe_image')
        print(recipe_name,recipe_description,recipe_image,sep="\n")
        Recipe.objects.create(recipe_name=recipe_name,recipe_description=recipe_description,recipe_image=recipe_image)
        return redirect("/")
    return render(request,'addrecipes.html')


def removeRecipe(request,pk):
    query=Recipe.objects.get(id=pk)
    print(query)
    query.delete()

    return redirect("/")

def updateRecipe(request,pk):
    recipe=Recipe.objects.get(id=pk)
    
    if request.method=='POST':
        recipe_name=request.POST.get("recipe_name")
        recipe_description=request.POST.get("recipe_description")
        recipe_image=request.FILES.get('recipe_image')
        
        recipe.recipe_name=recipe_name
        recipe.recipe_description=recipe_description
        if recipe_image:
            recipe.recipe_image=recipe_image
        
        recipe.save()

        return redirect("/")
    return render(request,'updaterecipe.html',{'recipe':recipe})
