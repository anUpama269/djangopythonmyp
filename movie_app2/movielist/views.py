from django.shortcuts import render,redirect
from django.template.defaultfilters import title
from django.templatetags.i18n import language
from django.urls import reverse_lazy
from movielist.models import Movies
from django.views.generic import ListView
# def movie_list(request):
#     m=Movies.objects.all()
#     return render(request,'movielist.html',{'movies':m})

class MovieListView(ListView):
    model=Movies
    template_name = 'movielist.html'
    context_object_name = 'movies'






from movielist.forms import AddmovieForm
# def add_movie(request):
#     if request.method=="POST":
#         form_instance = AddmovieForm(request.POST,request.FILES)
#         if form_instance.is_valid():
#             # data = form_instance.cleaned_data
#             # print(data)
#             # m=Movies.objects.create(name=form_instance.cleaned_data['Movie_Name'],
#             #                         director_name=form_instance.cleaned_data['Director_Name'],
#             #                         description=form_instance.cleaned_data['Description'],
#             #                         language=form_instance.cleaned_data['Language'],
#             #                         Year=form_instance.cleaned_data['Year'],
#             #                         image=form_instance.cleaned_data['Image'])
#             # m.save()
#             form_instance.save()
#
#
#             return redirect('movie_list',)
#
#     form_instance=AddmovieForm()
#     return render(request, 'addmovie.html',{'form':form_instance})

from django.views.generic import CreateView
class AddMovie(CreateView):
    form_class = AddmovieForm
    template_name = 'addmovie.html'
    model=Movies
    success_url = reverse_lazy('movie_list')



# def detail_view(request,i):
#     m=Movies.objects.get(id=i)
#     return render(request,'detailview.html',{'Movies':m})


from django.views.generic import DetailView
class MovieDetail(DetailView):
    model = Movies
    template_name = 'detailview.html'
    context_object_name = 'Movies'







# def edit_view(request,i):
#     m=Movies.objects.get(id=i)
#     if request.method == "POST":
#         form_instance = AddmovieForm(request.POST, request.FILES,instance=m)
#
#         if form_instance.is_valid():
#             form_instance.save()
#             return redirect('movie_list',)
#
#     form_instance = AddmovieForm(instance=m)
#
#
#     return render(request,'editview.html',{'form': form_instance})


from django.views.generic import UpdateView
class EditView(UpdateView):
    form_class = AddmovieForm
    template_name ='editview.html'
    model = Movies
    success_url = reverse_lazy('movie_list')


# def deletemovie(request,i):
#     m=Movies.objects.get(id=i)
#     m.delete()
#     return redirect('movie_list')

from django.views.generic import DeleteView
class DeleteMovie(DeleteView):
    model=Movies
    template_name = 'delete.html'
    success_url = reverse_lazy('movie_list')