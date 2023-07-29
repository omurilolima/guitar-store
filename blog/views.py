from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from .models import Post
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class PostList(generic.ListView):
    """
    Displays the latest blog posts on the home page,
    including filter by approved and order by created_on descending
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/index.html'
    paginate_by = 6
