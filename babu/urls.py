from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('', views.display, name='index'),
    path('as', views.addShow, name='addShow'),
    path('display', views.display, name='display'),
    path('delete/<int:id>', views.delete, name='deletedata'),
    path('update/<int:id>', views.update, name='updatebaba'),
    path('search', views.search, name='search'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='sinout'),

]
