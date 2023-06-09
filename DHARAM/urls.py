"""
URL configuration for DHARAM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# """
from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
from django.urls import include, path
from rest_framework import routers
from dharam_api.views import SignupView,otpView,LoginView, resetpasswordView,forgotpassword,otpverify,feedback,Invoice,History
from dharam_api import views

router = routers.DefaultRouter() 
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
router.register(r'user_details', views.User_detailsViewSet)
router.register(r'feedback', views.feedbackViewSet)
router.register(r'invoices', views.InvoiceViewSet)
router.register(r'history', views.HistoryViewSet)


# router.register(r'login_user', views.CustomerLoginViewSet)
Invoice
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', LoginView.as_view(), name="login"),
    path('signup/', SignupView.as_view(), name="login"),
    path('otp/', otpView.as_view(), name="otp"),
    path('reset/', resetpasswordView.as_view(), name="reset"),
    path('forgotpassword/', forgotpassword.as_view(), name="forgotpassword"),
    path('otpverify/', otpverify.as_view(), name="otpverify"),
    path('updatefeedback/', feedback.as_view(), name="feedback"),
    path('invoices_data/', Invoice.as_view(), name="Invoice"),
    path('history_data/', History.as_view(), name="History"),

    




    


]