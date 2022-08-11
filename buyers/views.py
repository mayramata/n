from django.shortcuts import render

# Create your views here.

# Create your views here.
def buyers(request): #tiene que ir el nombre de la a´ñicacion aqui para pasarla como variable en url por medio de view.sewingcourse
    return render(request, 'pages/buyers.html')