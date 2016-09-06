from django.conf.urls import include, url
from django.contrib import admin
import newsletter.views

urlpatterns = [
    # Examples:
    url(r'^$', newsletter.views.home, name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
