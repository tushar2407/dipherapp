from django.urls import path, include
from .views import  (
    home, 
    UserLogin, 
    UploadFile,
    signup,
    delete,
    profile,
    Encrypt,
    Decrypt,
    logout_view,
    download
)

urlpatterns=[
    #path('upload/', upload,name="upload" ),
    path('',home, name="home"),
    path('login/', UserLogin.as_view(), name="login"),
    path('upload/',UploadFile.as_view(),name="uploadFile"),
    path('register/',signup,name="signup"),
    path('delete/<int:pk>/',delete, name='delete'),
    path('profile/', profile, name="profile"),
    path('encrypt/', Encrypt.as_view(), name="encrypt"),
    path('decrypt/', Decrypt.as_view(), name="decrypt"),
    path('logout/',logout_view, name="logout"),
    path('download/<int:pk>',download,name="download"),
]