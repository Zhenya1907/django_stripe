from django.urls import path
from .views import (
    IndexPageView,
    DetailPageView,
    CreateCheckoutSessionView,
    SuccessView,
    CancelView
)



urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('item/<int:item_id>/', DetailPageView.as_view(), name='item'),
    path('buy/<int:item_id>/', CreateCheckoutSessionView.as_view(), name='buy'),
    path('success/', SuccessView.as_view(), name='success'),
    path('cancel', CancelView.as_view(), name='cancel'),
    ]