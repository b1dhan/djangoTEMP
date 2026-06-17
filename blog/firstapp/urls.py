from django.urls import path
from . import views

# same as routing in React 
urlpatterns=[
    path('home/', views.first_view, name='first_view'),
    path('profile/<int:id>', views.profile_view, name='profile_view'),
    path('html/', views.html_view, name='html_view'),
    path('intro/', views.intro_view, name='intro_view'),
    path('createpost/', views.create_post, name="create_post")
]