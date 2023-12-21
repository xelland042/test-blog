from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DeleteView, DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy

from post.models import Post, Tag, Comment
from post.forms import CommentForm


def home(request):
    return render(request, 'post/home.html')


class PostListView(ListView):
    template_name = 'post/home.html'
    model = Post
    context_object_name = 'posts'


class PostDetailView(DetailView):
    template_name = 'post/post-detail.html'
    model = Post
    context_object_name = 'post'

    def get_success_url(self):
        return reverse_lazy('post:detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CommentForm()
        context['form'] = form
        context['comments'] = Comment.objects.filter(post=self.object)
        return context

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if request.method == 'POST':
            form = CommentForm(request.POST)
        if form.is_valid():
            reply_obj = None
            try:
                reply_id = int(request.POST.get('reply_id'))
            except:
                reply_id = None
            if reply_id:
                reply_obj = Comment.objects.get(id=reply_id)

            print(form.data)
            author = request.user
            comment_text = form.data.get('comment_field')
            if reply_obj:
                comment = form.save(commit=False)
                comment.author = author
                comment.reply = reply_obj
                comment.comment_field = comment_text
                comment.post_id = pk
                comment.is_reply = True
                comment.save()
            else:
                Comment(author=author, comment_field=comment_text, post_id=pk).save()
            return redirect('post:detail', pk)
