from django.shortcuts import render
from .forms import MoviesModelForm
from .models import class6
def page1(request):
    if request.method == 'POST':
        form = MoviesModelForm(request.POST)
        if form.is_valid():
            movies=form.save()
            form = MoviesModelForm()
            return render(request, 'forms-data.html', {'form': form, 'movies': movies})
            
    else:
        form = MoviesModelForm()
    return render(request,'page1.html',{'form':form})

