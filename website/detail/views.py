from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,render_to_response
from django.contrib.auth import authenticate, login, logout
# from django.core.context_processors import csrf
from django.contrib.auth.models import User



from .formsyn import PostForm
from .models import Detail

from .models import contactus
from .contactform import ContactForm

from .models import comment
from .commentform import CommentForm

from .models import stories
from .storyform import StoryForm






def index(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/home')
	else:
		return render(request,"index.html",{})




# login section start

def Login(request):
	#c={}
	#c.update(csrf(request))
	return render_to_response('login.html')

def logIn(request):
	return render(request,"invalid.html",{})

def auth_view(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username = username, password = password)
	if user is not None:
		login(request,user)
		return HttpResponseRedirect('/home')
	else:
		return HttpResponseRedirect('/logIn')

# login section finish


def logOut(request):
	logout(request)
	return HttpResponseRedirect('/')







def details(request):
	form = PostForm(request.POST or None)
	context = {
		"form" : form,
		"username":request.user.get_username(),
	}
	return render(request,"info.html",context)


def formcheck(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	return HttpResponseRedirect('/home')






def signup(request):
	# c={}
	# c.update(csrf(request))
	return render_to_response('signup.html')


def signcheck(request):
	username = request.POST['username']
	email = request.POST['email']
	password = request.POST['password']
	if User.objects.filter(email = email).exists() and User.objects.filter(username = username).exists():
		context = {
				"statement" : "You already have an account, so please login!!"
		}
		return render(request,"signup.html",context)
	elif User.objects.filter(username=username).exists():
		context = {
				"statement" : "Username already exist, change your username!!"
		}
		return render(request,"signup.html",context)
	elif User.objects.filter(email = email).exists():
		context = {
				"statement" : "Email is already registered, enter new email!!"
		}
		return render(request,"signup.html",context)
	
	else:
		user = User.objects.create_user(username, email, password)
		user.save()
		user = authenticate(username = username, password = password)
		login(request,user)
		subject = 'thank you'
		message = 'welcome https://docs.djangoproject.com/en/1.10/topics/email/'
		from_email = settings.EMAIL_HOST_USER
		to_list = (user.email, settings.EMAIL_HOST_USER)
		send_mail(subject,message,from_email,to_list, fail_silently = True)
		return HttpResponseRedirect('/details')







def home(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/login')
	else:
		context = {
			"username":request.user.get_username(),
		}
		return render(request,"home.html",context)

def gallery(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/login')
	else:
		context = {
			"username":request.user.get_username(),
		}
		return render(request,"gallery.html",context)

def member(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/login')
	else:
		queryset = Detail.objects.all()
		context = {
			"detail_list" : queryset,
			"username":request.user.get_username(),
		}
		return render(request,"member.html",context)


def feedbackmake(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/login')
	else:
		queryset = stories.objects.order_by('-id')
		form = StoryForm(request.POST or None)
		context = {
			"form" : form,
			"story_list" : queryset,
			"username":request.user.get_username(),
		}
		return render(request,"feedback.html",context)


def contact(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/login')
	else:
		form = ContactForm(request.POST or None)
		context = {
			"form" : form,
			"username":request.user.get_username(),
		}
		return render(request,"contact.html",context)


def commentmake(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/login')
	else:
		queryset = comment.objects.order_by('-id')
		form = CommentForm(request.POST or None)
		context = {
			"form" : form,
			"comment_list" : queryset,
			"username":request.user.get_username(),
		}
		return render(request,"comment.html",context)




def formcheck2(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	return HttpResponseRedirect('/feedback/')


def formcheck3(request):
	form = CommentForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	return HttpResponseRedirect('/comment/')


def formcheck4(request):
	form = StoryForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	return HttpResponseRedirect('/feedback/')
