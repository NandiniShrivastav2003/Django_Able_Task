from django.shortcuts import render,HttpResponse

# Create your views here.
def blogHome(index):
    return HttpResponse('This is Bloghome we will keep all the blogs here..')

def blogPost(request,slug):
    return HttpResponse(f'This is blog post:{slug}')