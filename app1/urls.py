from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name='app1'
urlpatterns = [
    path("",views.home, name="h"),
    path("about",views.about, name="about"),
    path("contact",views.contact, name="contact"),
    path("services",views.service, name="service"),
    path("Project/",views.project, name="project"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

# postgres://hallotech_user:LsV1eCHQdWB6i7tJJwUe43DRdbxHNGTG@dpg-cnq8hmen7f5s73f8pvo0-a.oregon-postgres.render.com/hallotech