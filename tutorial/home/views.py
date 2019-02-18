from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView
from home.forms import HomeForm
from django.contrib.auth.models import User
from home.models import Post, Friend

# Create your views here.
class HomeView(TemplateView):

    template_name = 'home/home.html'
    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all().order_by('-post_date')
        users = User.objects.exclude(pk=request.user.id)
        length = len(users)
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.user.all()
        args = {'form': form, 'posts': posts, 'users': users, 'friends': friends, 'length': length}
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        data = ''
        if form.is_valid():
            post = form.save(commit=False)
            post.post_user = request.user
            post.save()
            data = form.cleaned_data['post']
            form = HomeForm()
            return redirect('home:home')
        return render(request, self.template_name, {'data': data, 'form': form})

def change_friend(request, action, f_id):

    new_friend = User.objects.get(pk=f_id)
    current_user = request.user
    if action == 'add':
        Friend.make_friend(current_user, new_friend)
    elif action == 'remove':
        Friend.lose_friend(current_user, new_friend)

    return redirect('home:home')