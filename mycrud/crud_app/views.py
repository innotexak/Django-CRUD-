from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import BlogForm
from django.contrib import messages 
# Create your views here.
def home(request):

    return render(request, 'base.html')

def postView(request):
    qs = Post.objects.all()
    
    return render(request, 'blog.html', {
                                        'post':qs})


def blog_form(request):
    my_form = BlogForm()
    
    if request.method == 'POST':
        my_form = BlogForm(request.POST, request.FILES)
        if my_form.is_valid():
            my_form.save()
            messages.success(request, "Your information was posted successfully!")
            return redirect("blog")
        else:
            messages.danger(request, "Your form is not valid!")
            return render(request, 'form_sub.html')
    else:
        my_form = BlogForm()
    return render(request,'form_sub.html', {"forms":my_form})

def edit_view(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Post.objects.get(id=book_id)
    except Post.DoesNotExist:
        return redirect('index')
    upload_form = BlogForm(request.POST or None, instance=book_sel)
    print(upload_form)
    if upload_form.is_valid():
        upload_form.save()
        
        messages.warning(request, "Your information has been successfully edited")
        return redirect('blog')
    return render(request, 'form_sub.html', {'forms':upload_form})
    
    
    
    
def delete_view(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Post.objects.get(id=book_id)
    except book_sel.DoesNotExist:
        messages.danger(request, "Invalid selection!")
        return redirect('blog')
    else:
        book_sel.delete()
        messages.success(request, "Your post was deleted successfully!")
    return redirect('blog')


    
    
        
    