from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Only include once, with namespace if needed
    path('', include(('home.urls', 'home'), namespace='home')),

    path('admissions/', include(('admissions.urls', 'admissions'), namespace='admissions')),
    path('courses/', include(('courses.urls', 'courses'), namespace='courses')),
    path('events/', include(('events.urls', 'events'), namespace='events')),
    path('contact/', include(('contact.urls', 'contact'), namespace='contact')),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path('bot/', include('institute_bot.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
