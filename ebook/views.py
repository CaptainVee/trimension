from django.shortcuts import render, redirect
from .forms import BookForm, PageForm
from .models import Book, Page
from .utills import get_site_id, upload_model, my_random_string
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    books = Book.objects.all()
    return render(request, "ebook/home.html", {'books':books})

@login_required
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = request.user
            book.save()
            messages.success(request, "Successfully created book")
            return redirect('book-detail', pk=book.pk)
    form = BookForm()
    return render(request, "ebook/book_create.html", {'form':form})


def read(request, pk):
    book = Book.objects.get(pk=pk)
    pages = Page.objects.filter(book=book)
    return render(request, "ebook/read_book.html", {'book':book, "pages":pages})


# def book_list(request):
#     books = Book.objects.all()
#     return render(request, "ebook/book_list.html", {'books':books})

@login_required
def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            model = form.cleaned_data['model']
            json_obj = get_site_id(f'{book.title}-{my_random_string()}')
            swiftxr_link =json_obj['site']['site_url']
            page = Page.objects.create(
                site_name=json_obj['site']['site_name'], 
                site_id=json_obj['site']['site_id'], 
                site_url=swiftxr_link,
                book=book,
                text = request.POST.get("text"),
                model = model,
                image = request.POST.get("image"),
                )
            # Call the API with the uploaded file
            # breakpoint()
            file = page.model
            upload_data = upload_model(file, json_obj['site']['site_id'])
            if upload_data["success"] == 'Successfully deployed site':
                messages.success(request, f"Successfully created page, preview here {swiftxr_link}")

            else:
                messages.error(request, "something went wrong")
    else:
        form = PageForm()
    context = {'form':form, "book":book}
    return render(request, "ebook/book_detail.html", context)



"SWF.8OEDftHHfg4jPA.szwPDnyEjnHFf8KcOurylnRuFUHbMOQ0nx7rpAFwwG0"
{"success":"successfully created site","site":{"site_id":"prj_6van8svtqJfSSAbBa31dw9gzpyie","site_name":"cowmilk","created":1682385737187,"updated":1682385737187,"site_url":"https://cowmilk.swiftxr.app"}}