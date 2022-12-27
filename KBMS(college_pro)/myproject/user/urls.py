from django.urls import path
from .import views

app_name='user'

urlpatterns = [

    path('',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('articlelist/',views.ArticleList,name='articlelist'),
    path('<int:pk>/articleview/',views.AriticleView.as_view(),name='articledetail'),
    path('articlecreate/',views.ArticleCreate.as_view(),name='articlecreate'),
    path('dashboard/',views.dashboarddetail.as_view(),name='dashboard'),
    path('<int:pk>/articleupdate/',views.Articleupdate.as_view(),name='articleupdate'),
    path('<int:pk>/articledelete/',views.Articledelete.as_view(),name='articledelete'),
    path('questionform/',views.QuestionForm.as_view(),name='questionform'),
    path('questionlist/',views.QuestionList.as_view(),name='questionlist'),
    path('questionform/thankyou/',views.Thankyou,name='thankyou'),
    path('service/',views.service,name='service'),

]