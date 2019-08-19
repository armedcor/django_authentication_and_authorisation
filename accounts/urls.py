from django.urls.conf import url
from accounts.views import index, logout, login, registration, user_profile
import url_reset

urlpatterns = [
    url(r'^accounts/logout/$', logout, name="logout"),
    url(r'^accounts/login/$', login, name="login"),
    url(r'^accounts/register/$', registration, name="registration"),
    url(r'^accounts/profile/$', user_profile, name="profile")
]
