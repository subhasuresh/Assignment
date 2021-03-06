from django.conf.urls import include, url
from register.views import *
from register.models import *
urlpatterns = [
    url(r'^$', UserRegistrationView.as_view(), name='register_user'),
    url(r'^user/$', UserRegistrationView.as_view(), name='login'),
    url(r'^user/success/', TemplateView.as_view(template_name='page.html'),
        name='page'),
    url(r'^chocolate/add/',AddChocolateview.as_view(), name='add_chocolate'),
    url(r'^chocolate/success/', TemplateView.as_view(template_name='success.html'),
        name='bla'),
    url(r'^chocolate/add/', AddChocolateview.as_view(), name='add_chocolates'),
    url( r'^chocolate/info/(?P<choco_id>\d+)/$', ChocolateDetailsView.as_view(), name="chocolate_info"),
    url(r'^user/profile/edit/$', UserProfileUpdateView.as_view(), name='user_profile_update'),
    ]
