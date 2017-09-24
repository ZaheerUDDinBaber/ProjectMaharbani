from django.conf.urls import url,include
from frontend import views

urlpatterns = [
    #www.projectmaharbani.org#
    url(r'^$',views.home, name="homepage"), #default

    #
    # url(r'^login.html/$', views.login, name="login"),
    # url(r'^login.html/signup.html/$', views.signup, name="signup"),
    # url(r'^login.html/signup.html/save/$', views.saveaccount, name="save-account"),



    #www.projectmaharbani.org/signin/#



]