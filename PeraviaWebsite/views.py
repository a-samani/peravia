from django.http import JsonResponse
from django.shortcuts import render
from peravia_accounts.models import CustomUser
from peravia_products.models import Category, MainCategory
from peravia_setting.models import SiteSetting, SocialMedia, Client, Certificate
from django.core import serializers
from peravia_team.models import Team
from peravia_blog.models import News


# ------------------------------------------------------------------------
def homepage(request):
    team = Team.objects.all()
    return render(request, 'main/Home_Page.html', {'title': 'Peravia | Home',
                                                   'main_categories': MainCategory.objects.all(),
                                                   'clients': Client.objects.all(),
                                                   'members': Team.objects.all(),
                                                   'certificates': Certificate.objects.all(), 
                                                   'newslist': News.objects.all()[:3]})


# ------------------------------------------------------------------------
def about_us(request):
    return render(request, 'main/About_Us.html', {'title': 'Peravia | About Us',
                                                  'page_name': 'About Us',
                                                  'members': Team.objects.all()})
                                                  
# ------------------------------------------------------------------------
def frequently_asked_questions(request):
    return render(request, 'main/FAQ.html', {'title': 'Peravia | FAQ',
                                             'page_name': 'FAQ'})


# ------------------------------------------------------------------------
def checkEmail(request):
    email = request.GET.get('email', None).lower()
    data = {
        'is_taken': CustomUser.objects.filter(email__iexact=email).exists()
    }
    return JsonResponse(data)


# ------------------------------------------------------------------------
def AjaxCategories(request):
    data = {
        'categories': serializers.serialize('json', MainCategory.objects.all())
    }
    return JsonResponse(data)


# ------------------------------------------------------------------------
def AjaxSiteSetting(request):
    site_setting = serializers.serialize('json', SiteSetting.objects.all()[:1])
    data = {
        'site_setting': site_setting,
        'social_media': serializers.serialize('json', SocialMedia.objects.all()),
        'main_categories': serializers.serialize('json', MainCategory.objects.all())
    }
    return JsonResponse(data)


# ------------------------------------------------------------------------
def handle_404_error(request, exception):
    return render(request, '404.html', {})
