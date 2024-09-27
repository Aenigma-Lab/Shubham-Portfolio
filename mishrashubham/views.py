from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import ContactForm
from django.middleware.csrf import CsrfViewMiddleware


def home_page(request):
    context = {
        'page_title': 'Welcome to My Portfolio',
        
    }
    return render(request, "index.html", context)

def homePage_2(request):
    context = {
        'page_title': 'Alternate Home Page',
         
    }
    return render(request, "index-2.html", context)

def custom_404_view(request):
    return render(request, '404.html')

def contact_us(request):
    context = {
        'page_title': 'Contact Us',
    }
    return render(request, "contacts.html", context)
def portfolio(request):
    context = {
        'page_title': 'Portfolio',
    }
    return render(request,"portfolio.html", context)

def portfolio_single(request):
    context = {
        'page_title': 'Portfolio Item',
    }
    return render(request, "portfolio-single.html", context)

def portfolio_single_2(request):
    context = {
        'page_title': 'Portfolio Item 2',
    }
    return render(request, "portfolio-single2.html", context)

def my_blog(request):
    context = {
        'page_title': 'My Blogs',
    }
    return render(request, "blog.html", context)

def blog_single(request):
    context = {
        'page_title': 'Single Blog',
    }
    return render(request, "blog-single.html", context)

def resume(request):
    context = {
        'page_title': 'My Resume',
    }
    return render(request, "resume.html", context)


def contact_us_submit(request):
    if request.method == 'POST':
        csrf_token = request.POST.get('csrfmiddlewaretoken')
        print(f"CSRF Token: {csrf_token}")  # Debugging line
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success-page')
    else:
        form = ContactForm()

    context = {
        'form': form,
        'page_title': 'Contact Us',
    }
    return render(request, "contacts.html", context)

def success_page(request):
    context = {
        'page_title': 'Success!',
    }
    return render(request, 'success.html', context)