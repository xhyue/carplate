from django.conf.urls import url
from charge import views
urlpatterns = [
    url('carinport/', views.Carinprot, name="carinport"),
    url('caroutport/', views.Caroutprot, name="caroutport"),
    url('carin/', views.car_in, name="carin"),
    url('carout/', views.car_out, name="carout"),

]