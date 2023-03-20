from django.shortcuts import render

# Create your views here.
def specificstatic_folder(request):
    return render(request,'specificstatic_folder.html')