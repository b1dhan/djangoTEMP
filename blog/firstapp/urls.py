from django.urls import path
from . import views

# same as routing in React 
urlpatterns=[
    path('home/', views.first_view, name='first_view'),
    path('pfp/<int:id>', views.pfp_view, name='pfp_view'),
    path('', views.html_view, name='html_view'),
    path('intro/', views.intro_view, name='intro_view'),
    path('createpost/', views.create_post, name="create_post"),
    path('allpost/', views.get_post_view, name="get_post"),
    path('post/<int:post_id>', views.post_detail_view, name="post_detail"),
    path('signup/', views.signup_view, name="signup_view"),
    path('login/', views.login_view, name="login_view"),
    path('logout/', views.logout_view, name="logout_view"),
    path('post/<int:id>/edit_post/', views.edit_post, name="edit_post"),
    path('post/<int:id>/delete_post/', views.delete_post, name="delete_post"),
    path('search/', views.search, name="search"),
    path('password_change/', views.change_password, name='password_change'),
    path('password_change/done/', views.change_password_done, name='password_change_done'),
    path('profile/', views.profile_view, name='profile_view')
]