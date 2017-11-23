from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
from forms import MyRegistrationForm, Customers_form
from .models import Customers
from products.models import product


# Create your views here.
def index(request):
    language = 'en-gb'
    session_language = 'en-gb'
    info = Customers.objects.all()
    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']
    if 'lang' in request.session:
        session_language = request.session['lang']
    c={}
    c.update(csrf(request))
    c['language'] = language
    c['session_language'] = session_language
    c['info'] = Customers.objects.all()
    c['full_name'] = request.user.username
        # user1 = request.session['user']

    return render_to_response('header/index.html',
                              c)
    # template = loader.get_template('htmls/index.html')
    # return HttpResponse(template.render(request))


'''def login(request):
      template = loader.get_template('header/login.html')
      return HttpResponse(template.render(request)) '''


def language(request, language='en-gb'):
    response = HttpResponse("setting language to %s" % language)
    response.set_cookie('lang', language)
    request.session['lang'] = language
    return response


def login(request):
    c = {}
    c.update(csrf(request))

    return render_to_response('header/form.html', c)
    # template = loader.get_template('header/form.html')
    # return HttpResponse(template.render(request))


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/index/accounts/loggedin')
    else:
        return HttpResponseRedirect('/index/accounts/invalid')


def loggedin(request):
    c={}
    c.update(csrf(request))
    c['full_name'] = request.user.username
    return render_to_response('header/index.html',c)


def invalid_login(request):
    return render_to_response('header/invalid_login.html')


def logout(request):
    auth.logout(request)
    return render_to_response('header/form.html')


def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index/accounts/register_success')
    args = {}
    args.update(csrf(request))
    args['form'] = MyRegistrationForm()
    return render_to_response('header/form.html', args)


def register_success(request):
    return render_to_response('header/register_success.html')


def create(request):
    if request.POST:
        form = Customers_form(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect('/index')

    else:
        form = Customers_form()
        args = {}
        args.update(csrf(request))
        args['form'] = form
        return render_to_response('header/create_customer.html', args)


def contact(request):
    return render_to_response('header/contact-us.html', {'full_name': request.user.username})


def search(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''

    p1 = product.objects.filter(productname__contains=search_text)

    return render_to_response('header/ajax_search.html', {'p1': p1,'search_text':search_text})
