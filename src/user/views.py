from django.utils.http import is_safe_url
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, RedirectView

from .forms import LoginForm, RegisterForm

# Create your views here.

class RegisterView(CreateView):
	form_class = RegisterForm
	template_name = "form.html"
	success_url = '/login'

class LoginView(FormView):
	form_class = LoginForm
	template_name = 'form.html'
	success_url = '/'

	def form_valid(self, form):
	    request = self.request

	    next_ = request.GET.get('next')
	    next_post = request.POST.get('next')
	    redirect_path = next_ or next_post or None

	    email = form.cleaned_data.get("email")
	    password = form.cleaned_data.get("password")
	    user = authenticate(request, email=email, password=password)

	    if user is not None:
	        login(request, user)
	        if is_safe_url(redirect_path, request.get_host()):
	            return redirect(redirect_path)
	        else:
	            return redirect("/")
	    return super(LoginView, self).form_invalid(form)

class LogoutView(RedirectView):
	url = '/login'

	def get(self, request, *args, **kwargs):
		logout(request)
		return super(LogoutView, self).get(request, *args, **kwargs)

