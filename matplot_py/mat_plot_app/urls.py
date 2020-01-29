from django.conf.urls import url
from . import views
 
urlpatterns = [
    # url(r'^$', views.HomePageView.as_view()),
    # url(r'^links/$' , views.LinksPageView.as_view()),
    url(r'^getcust/$',views.Customers.getCust),
    url(r'^getnum/$',views.Customers.getNums),
    url(r'getimg.png', views.Customers.getimage),
    url(r'^getdata/$', views.Customers.getData),
    url(r'^getsbdata/$', views.Customers.getSBData),
    url(r'^getavg/$', views.Customers.getAvg),
    # url(r'mplimage.png', views.mplimage)
 
]