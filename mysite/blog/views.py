from django.shortcuts import render,HttpResponse
from blog.models import Post
# Create your views here.
def blogHome(request):
    #fetches all the posts in form of objects from database.
    allPosts=Post.objects.all()
    # print(allPosts)
    context={'allPosts':allPosts}
    return render(request,'blog/blogHome.html',context)

def blogPost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    # print(post)
    context={'post':post}
    return render(request,'blog/blogPost.html',context)

   # return HttpResponse(f'This is blog post:{slug}')