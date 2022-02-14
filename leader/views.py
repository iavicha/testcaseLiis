from django.shortcuts import render
# from forms import RegisterForm
# from django.http import HttpResponseRedirect
# from django.contrib.auth.models import User
# from django.contrib.auth import password_validation


# Create your views here.

# def register(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         if RegisterForm.is_valid():
#             email = RegisterForm.cleaned_data['username']
#             password_ = RegisterForm.cleaned_data['password']
#             User.objects.create(username=email, password=password_)
#             return HttpResponseRedirect('login')
#
#         # if a GET (or any other method) we'll create a blank form
#     else:
#         form = RegisterForm()
#
#     return render(request, 'register.html', {'form': RegisterForm})
