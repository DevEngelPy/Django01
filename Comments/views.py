from django.shortcuts import render, redirect, get_object_or_404,get_list_or_404
from django.core.paginator import Paginator
from .forms import CommentForm
from .models import Comment
# Create your views here.

def index(request):
    all_commment = Comment.objects.all()
    #all_commment = get_list_or_404(Comment, pk__gt=10)
    paginatior = Paginator(all_commment, 2)
    page_nuber = request.GET.get('page')
    comment_page = paginatior.get_page(page_nuber)
        
    context = {
                'Comments': all_commment,
                'comment_page':comment_page,
                'title':'Listado de Comentarios',
                } 
    return render(request, 'comments/index.html', context)


def add(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Comments:index')
    else:
        form = CommentForm()
        
    return render(request, 'comments/add.html',{'page':'Add',
                                                'form': form})


def update(request, pk):
    commet = get_object_or_404(Comment,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=commet)
        if form.is_valid():
            form.save()
            return redirect('Comments:index')
    else:
        form = CommentForm(instance=commet)
    context = {
        'page':'editando',
        'form':form,
        'comment':commet
    }
    return render(request, 'comments/add.html', context)

def delete(request, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == 'POST':
        comment.delete()
    return redirect('Comments:index')