from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='/sv/', permanent=False)),
    
    path('ofv/', views.orderFormView, name='order_url'),
    path('sv/', views.showView, name='show_url'),
    path('up/<int:f_oid>', views.updateView, name= 'update_url'),
    path('del/<int:f_oid>', views.deleteView, name= 'delete_url'),
]