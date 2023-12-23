"""
URL configuration for itd105 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('/register/', views.register, name='register'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('/signout/', views.signout, name='signout'),
    path('/index/', views.index, name='index'),

    path('add_view/', views.add_view, name='add_view'),
    path('add_med/', views.add_med, name='add_med'),
    path('view/', views.view, name='view'),
    path('edit/<int:id>',views.edit, name='edit'),
    path('update/<int:id>',views.update, name='update'),
    path('delete/<int:id>',views.destroy, name='destroy'),
]

