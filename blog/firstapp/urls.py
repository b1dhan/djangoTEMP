from django.urls import path
from . import views

# same as routing in React 
urlpatterns=[
    path('home/', views.first_view, name='first_view'),
    path('profile/<int:id>', views.profile_view, name='profile_view'),
    path('', views.html_view, name='html_view'),
    path('intro/', views.intro_view, name='intro_view'),
    path('createpost/', views.create_post, name="create_post"),
    path('allpost/', views.get_post_view, name="get_post"),
    path('post/<int:post_id>', views.post_detail_view, name="post_detail"),
    path('signup/', views.signup_view, name="signup_view"),
    path('login/', views.login_view, name="login_view"),
    path('logout/', views.logout_view, name="logout_view"),
    path('post/<int:id>/edit_post/', views.edit_post, name="edit_post"),
    path('search/', views.search, name="search")
]