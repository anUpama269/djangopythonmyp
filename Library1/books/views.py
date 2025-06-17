from django.shortcuts import render,redirect
from django.template.defaultfilters import title
from django.templatetags.i18n import language
from django.views import View


# def home(request):
#
#     return render(request,'home.html',)
class HomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"home.html")

from books.forms import AddbookForm
# def add_book(request):
#     if request.method == "POST":
#         # print(request.POST)
#         # print(request.FILES)
#         form_instance = AddbookForm(request.POST,request.FILES)
#         if form_instance.is_valid():
#             # data = form_instance.cleaned_data
#             # title = data['Title']
#             # author = data['Author']
#             # page = data['Page']
#             # price = data['Price']
#             # language=data['Language']
#             # b = Book.objects.create(title=title, author=author, pages=page, price=price, language=language)
#             # b=Book.objects.create(title=form_instance.cleaned_data['Title'],
#             #                       author=form_instance.cleaned_data['Author'],
#             #                       pages=form_instance.cleaned_data['Page'],
#             #                       price=form_instance.cleaned_data['Price'],
#             #                       language=form_instance.cleaned_data['Language'],
#             #                       image=form_instance.cleaned_data['Image'])
#             # b.save()
#             # print(data)
#             form_instance.save()
#
#
#         return redirect('books:view_book')

    # form_instance=AddbookForm()
    # return render(request,'addbook.html',{'form':form_instance})

class AddBookView(View):
    def get(self,request,*args,**kwargs):
        form_instance = AddbookForm()
        return render(request, 'addbook.html', {'form': form_instance})
    def post(self,request):
        if request.method == "POST":
            # print(request.POST)
            # print(request.FILES)
            form_instance = AddbookForm(request.POST, request.FILES)
            if form_instance.is_valid():
                # data = form_instance.cleaned_data
                # title = data['Title']
                # author = data['Author']
                # page = data['Page']
                # price = data['Price']
                # language=data['Language']
                # b = Book.objects.create(title=title, author=author, pages=page, price=price, language=language)
                # b=Book.objects.create(title=form_instance.cleaned_data['Title'],
                #                       author=form_instance.cleaned_data['Author'],
                #                       pages=form_instance.cleaned_data['Page'],
                #                       price=form_instance.cleaned_data['Price'],
                #                       language=form_instance.cleaned_data['Language'],
                #                       image=form_instance.cleaned_data['Image'])
                # b.save()
                # print(data)
                form_instance.save()

            return redirect('books:view_book')


from books.models import Book
# def add_book1(request):
#     if request.method=="POST":
#         print(request.POST)
#         print(request.FILES)
#         t=request.POST['t']
#         a=request.POST['a']
#         pa=request.POST['pa']
#         pr=request.POST['pr']
#         l=request.POST['l']
#         i=request.FILES['i']
#
#         b=Book.objects.create(title=t,author=a,pages=pa,price=pr,language=l,image=i)
#         b.save()
#         return redirect('books:view_book')


    # return render(request, 'addbook1.html', )

class AddBook1View(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'addbook1.html', )

    def post(self,request,*args,**kwargs):
        if request.method == "POST":
            print(request.POST)
            print(request.FILES)
            t = request.POST['t']
            a = request.POST['a']
            pa = request.POST['pa']
            pr = request.POST['pr']
            l = request.POST['l']
            i = request.FILES['i']

            b = Book.objects.create(title=t, author=a, pages=pa, price=pr, language=l, image=i)
            b.save()
            return redirect('books:view_book')








# def view_book(request):
#     b=Book.objects.all()
#     print(b)
#     return render(request,'viewbook.html',{'books':b})


class ViewBookView(View):
    def get(self,request,*args,**kwargs):
            b = Book.objects.all()
            # print(b)
            return render(request, 'viewbook.html', {'books': b})




# def detail_view(request,i):
    # print(i)
    # b=Book.objects.get(id=i)
    # return render(request,'detailview.html',{'books':b})

class BookDetailView(View):
    def get(self,request,i):
        b = Book.objects.get(id=i)
        return render(request, 'detailview.html', {'books': b})


# def edit_view(request,i):
#     b = Book.objects.get(id=i)
#     if request.method == 'POST':
#         form_instance = AddbookForm(request.POST, request.FILES, instance=b)
#
#         if form_instance.is_valid():
#             form_instance.save()
#             return redirect('books:view_book')
#
#     form_instance = AddbookForm(instance=b)
#
#
#     return render(request,'editview.html',{'form': form_instance})
#


class EditBookView(View):
    def get(self,request,i):
        b = Book.objects.get(id=i)
        form_instance = AddbookForm(instance=b)
        return render(request, 'editview.html', {'form': form_instance})
    def post(self,request,i):
        b = Book.objects.get(id=i)
        if request.method == 'POST':
            form_instance = AddbookForm(request.POST, request.FILES, instance=b)

            if form_instance.is_valid():
                form_instance.save()
                return redirect('books:view_book')



# def deletebook(request,i):
#     b = Book.objects.get(id=i)
#     b.delete()
#     return redirect('books:view_book')

class DeleteBookView(View):
    def get(self,request,i):
        b = Book.objects.get(id=i)
        b.delete()
        return redirect('books:view_book')


from django.db.models import Q
# def search(request):
#     if request.method=="POST":
#         data=request.POST['q']
#         print(data)
#         b=Book.objects.filter(Q(title__icontains=data)| Q(author__icontains=data)|Q(language__icontains=data))
#         print(b)
#         context={'book':b}
#         return render(request, 'search.html',context)
#
#
#
#     return render(request,'search.html')

class BookSearchView(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'search.html')
    def post(self,request):
        data = request.POST['q']
        print(data)
        b = Book.objects.filter(Q(title__icontains=data) | Q(author__icontains=data) | Q(language__icontains=data))
        print(b)
        context = {'book': b}
        return render(request, 'search.html', context)




