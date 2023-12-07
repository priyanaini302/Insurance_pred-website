from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import joblib
from .models import insurance
model=joblib.load('./Insurance_pred_finalmodel.sav')

def index(request):
    return render(request,'index.html')
# Create your views here.
def result(request):
    if request.method=='POST':
        
        age =request.POST.get('age')
        #print(age)
        sex=request.POST.get('sex')
        #print(sex)
        bmi=request.POST.get('bmi')
        #print(bmi)
        children=request.POST.get('children')
        #print(children)
        smoker=request.POST.get('smoker')
        #print(smoker)
    result=model.predict([[age,bmi,children,sex,smoker]]) 
    #print(result)  
    pred={'predition':int(result)}
    inu=insurance(age=age,sex=sex,bmi=bmi,children=children,smoker=smoker)
    inu.save()
    return render(request,'result.html',pred)
