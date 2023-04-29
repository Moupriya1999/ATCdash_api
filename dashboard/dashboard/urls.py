from django.contrib import admin
from django.urls import path, include
from ATCdash import views
from django.contrib.auth import views as auth_views
from ATCdash.views import UserList, UserDetail
from ATCdash.views import ObtainTokenView

urlpatterns = [
    path('admin/', admin.site.urls, name='djangoadmin'),
    path('', views.home, name='login'),
    path('main/', views.dashboard, name='dashboard'),
    path('logout/', views.log_out, name='logout'),
    path('accounts/', include('allauth.urls')),
    path('profile_image/', views.generate_profile_image, name='generate_profile_image'),

    # Reset Password #
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),

    # url for API view
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    #Token view url
    path('api/token/', ObtainTokenView.as_view(), name='token_obtain'),
]
