from django.views.generic import TemplateView, ListView
from Inst.models import Post;

class HelloWorld(TemplateView):
    template_name = 'test.html'

class PostsView(ListView):
     model = Post
     template_name ='index.html'