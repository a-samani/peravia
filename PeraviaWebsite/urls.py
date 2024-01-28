from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path, include
from django.views.generic import RedirectView
from .views import (homepage,
                    checkEmail,
                    about_us,
                    AjaxCategories,
                    frequently_asked_questions,
                    AjaxSiteSetting)
from PeraviaWebsite import settings
from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns
# ----------------------------------------------------------
urlpatterns = i18n_patterns(

    path('', homepage, name='home'),
    path('about-us', about_us, name='about'),
    path('FAQ', frequently_asked_questions, name='faq'),
    path('ajax/validate_email/', checkEmail, name='validate_email_url'),
    path('ajax/GetCategories', AjaxCategories, name='get_categories'),
    path('ajax/GetSiteSetting', AjaxSiteSetting, name='get_site_setting'),
    # path('user/', include('peravia_accounts.urls', namespace='accounts')),
    path('', include('peravia_contact.urls', namespace='contact')),
    path('p/', include('peravia_products.urls', namespace='product')),
    path('blog/', include('peravia_blog.urls', namespace='blog')),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url("images/favicon/favicon.ico")), ),
    path(_('peravia_admin/'), admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('rosetta/', include('rosetta.urls')),
)
# ------------------------------------------------------------------------
handler404 = 'PeraviaWebsite.views.handle_404_error'
# ----------------------------------------------------------
if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
