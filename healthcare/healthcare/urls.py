"""
URL configuration for healthcare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from diseases import views
app_name='diseases'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('diagnose',views.diagnose,name='diagnose'),
    path('consultation/<d>', views.consultation, name='consultation'),
    path('checkup',views.checkup,name='checkup'),
    path('adddata', views.adddata, name='adddata'),
    path('suggestion <int:p>', views.suggestion, name='suggestion'),
    # path('suggested', views.suggested, name='suggested'),
    path('patient_register',views.patient_register,name='patient_register'),
    path('doctor_register',views.doctor_register,name='doctor_register'),
    path('user_login', views.user_login, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('delete,<int:p>', views.delete, name='delete'),
]


if settings.DEBUG:urlpatterns +=static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)




