from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from trade.forms import BasicForm
#from .models import Basic
#from .forms import BasicForm
from trade.models import Basic


def basic(request):
    basic = Basic.objects.all()
    return render(request, 'trade/home.html', {'basic': basic})


def create_view(request):
    if request.method == 'POST':
        form = BasicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = BasicForm
            context = {
                'form': form
            }
            return render(request, 'trade/test.html', context)
    return render(request, 'trade/test.html')


def update(request,id):
    bas = get_object_or_404(Basic, id=id)
    form = BasicForm(request.POST or None, request.FILES or None, instance=bas)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'trade/update.html', {'form': form})

class Update(UpdateView):
    model = Basic
    form_class = BasicForm
    template_name = 'trade/update.html'
    reverse_lazy = '/'

    def get_absolute_url(self):
        return reverse('/')





def delete_view(request, id):
    bas = Basic.objects.get(id=id)
    bas.delete()
    return redirect('/')








