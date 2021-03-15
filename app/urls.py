from django.urls import path
from .views import  *


urlpatterns = [
    path('',home,name='home'),
    path('login/',loginView,name='loginView'),
    path('login-auth/',loginAuth,name='loginauth'),
    path('is-authenticated/',isLoggedIn,name='isLoggedIn'),
    path('register/',registerView,name='registerView'),
    path('register-auth/',registerAuth,name='registerAuth'),
    path('profile/',userProfileView,name='userProfileView'),
    path('user-details/',userDetails,name='userDetails'),
    path('logout/',logoutUser,name='logoutView'),
    path('singledetector/',singledetector,name='singledetector'),
    path('show-output/',showimage,name='showimage'),
    path('process-image/',single_image_processor,name='process'),
    path('multidetector/',multi_detector,name='multi_detector'),
    path('multidetector/detector/',multi_detector_processor,name='multi_detector_processor'),
    path('multi-image-processor/',multi_image_processor,name='multi-image-processor'),
    path('draganddrop/',drag_and_drop,name='dragndrop')
]