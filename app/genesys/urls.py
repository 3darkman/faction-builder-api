from django.urls import path

from genesys import views


app_name = 'genesys'

urlpatterns = [
    path('traits/', views.TraitListView.as_view(), name='traits'),
    path('abilities/', views.AbilityViewSet.as_view({'get': 'list'})),
    path('abilities/<int:pk>', views.AbilityViewSet.as_view({
        'get': 'retrieve'})),
]
