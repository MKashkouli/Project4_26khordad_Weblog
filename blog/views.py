from django.shortcuts import render , redirect , reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy

from .forms import NewPostForm
from .models import Post

#  -----> Class Based View :
class PostListView(generic.ListView):
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts_list'
    def get_queryset(self):
        return Post.objects.filter(status='Pub').order_by('-datetime_modified')

    #----> Functional View :
# def post_list_view(request):
#     # posts_list = Post.objects.all()
#     posts_list = Post.objects.filter(status='Pub').order_by('-datetime_modified')
#     return render(request, 'blog/posts_list.html', {'posts_list' : posts_list})
#

#  -----> Class Based View :
class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


#     ----> Functional View
# def post_detail_view(request, pk):
#     # post = Post.objects.get(pk= pk)
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html',{'post':post})

class PostCreateView(generic.CreateView):
    template_name = 'blog/post_create.html'
    form_class =NewPostForm
    success_url = reverse_lazy('postlist')


#     ----> Functional View
# def post_create_view(request) :
#     if request.method == 'POST':
#         form = NewPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # form= NewPostForm()
#             return redirect('postlist')
#
#     else: #GET REQUEST
#          form=NewPostForm()
#     return render(request,'blog/post_create.html',context={'form':form})


    # if request.method == 'POST':                   raveshe aval ke tosie nemishavad
    #     post_title=request.POST.get('title')
    #     post_text=request.POST.get('text')
    #
    #     user= User.objects.all()[0]
    #     Post.objects.create(title=post_title,text=post_text, author=user, status='Pub')
    # else:
    #     print("GET REQUEST")
    # return render(request,'blog/post_create.html')

    # class PostUpdateView(generic.UpdateView):
    #     model = Post
    #     fields = ['title', 'text', 'author' , 'status']
    #     template_name =  'blog/post_create.html'


#  -----> Class Based View :
class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = NewPostForm      #or     ( # fields = ['title', 'text', 'author' ] or fields = __all__)
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('postlist')
# agar success_url neveshte nashavad bad az update varede safheye post detail mishavad


#     ----> Functional View
# def post_update_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = NewPostForm(request.POST or None, instance=post)
#
#     if form.is_valid():
#         form.save()
#         return redirect('postlist')
#
#     return render(request, 'blog/post_create.html', context={'form': form})


#  -----> Class Based View :
class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('postlist')

#     ----> Functional View
# def post_delete_view(request,pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('postlist')
#
#     return render(request,'blog/post_delete.html', context={'post': post})





