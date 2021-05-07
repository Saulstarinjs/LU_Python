from django.views.generic import (
    FormView,
    ListView,
    DetailView,
    View
)
from django.shortcuts import render, HttpResponse
from users.models import User
from users.forms import UserForm


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'


class UserDetailView(DetailView):

    model = User
    template_name = 'user_detail.html'


class AddUserView(FormView):

    form_class = UserForm
    template_name = 'form.html'
    success_url = "/"

    def form_valid(self, form):
        form.save()

        response = super().form_valid(form)

        return response


class UserEditView(View):

    def get(self, request, pk):

        form = UserForm()

        context = {
            'form': form
        }

        return render(
            template_name='form.html',
            context=context,
            request=request,
        )

    def post(self, request, pk):

        user = User.objects.get(pk=pk)

        username = request.POST['username']
        email = request.POST['email']

        if len(username) != 0:
            user.username = username

        if len(email) != 0:
            user.email = email

        user.save()

        context = {
            'user': user
        }

        return render(
            template_name='user_detail.html',
            context=context,
            request=request,
        )


class UserDeleteView(View):

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()

        return HttpResponse(f'Deleted {user.username}')
