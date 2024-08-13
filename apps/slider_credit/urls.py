from os import path

from .views import (
    slider_list, slider_detail, slider_create, slider_update, slider_delete,
    credit_list, credit_create, credit_update, credit_delete
)

urlpatterns = [
    path('sliders/', slider_list, name='slider_list'),
    path('sliders/<int:pk>/', slider_detail, name='slider_detail'),
    path('sliders/new/', slider_create, name='slider_create'),
    path('sliders/<int:pk>/edit/', slider_update, name='slider_update'),
    path('sliders/<int:pk>/delete/', slider_delete, name='slider_delete'),
    path('credits/', credit_list, name='credit_list'),
    path('credits/new/', credit_create, name='credit_create'),
    path('credits/<int:pk>/edit/', credit_update, name='credit_update'),
    path('credits/<int:pk>/delete/', credit_delete, name='credit_delete'),
]
