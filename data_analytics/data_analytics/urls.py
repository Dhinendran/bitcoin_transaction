from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from home.api import last100transaction,Transactions_count_per_minute,High_value_addr
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register('users', ListUsers, base_name="")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('transactions_count_per_minute/<int:min_value>', Transactions_count_per_minute.as_view()),
    path('show_transactions/', last100transaction.as_view()),
    path('high_value_addr', High_value_addr.as_view()),
    path('api-auth/', include('rest_framework.urls')),

]
