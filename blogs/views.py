from django.shortcuts import redirect, render, get_object_or_404
from .models import Blog, Category

def posts_by_category(request, category_id):
    #category = get_object_or_404(Category, id=category_id)
    posts = Blog.objects.filter(status__iexact='Published', category_id=category_id)
    # try:
    #     category = Category.objects.get(pk=category_id)   
    # except:
    #     return redirect('/')
    category = get_object_or_404(Category, pk=category_id)

    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'posts_by_category.html', context)



