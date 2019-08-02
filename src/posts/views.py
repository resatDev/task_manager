from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from .models  import Post
from .form import PostForm

#def post_create(request):
#def post_details(request):
def post_list(request):
    form = PostForm(request.POST or None)
    queryset = Post.objects.all()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #messages.success(request, "Successfully Created!")
        return HttpResponseRedirect("/posts/")
    context = {
        "post_list": queryset,
        "form": form
    }
    return render(request, "post_list.html", context)
#def post_update(request):
def post_delete(request,id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    #messages.success(request, "Successfully Deleted!")
    #return HttpResponseRedirect("/projects/" + str(pid))
    return HttpResponseRedirect("/posts/")
