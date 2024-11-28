from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from portfolio import views
from todo import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('blog/', include('blog.urls')),
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('create/', views.createtodo, name='createtodo'),
    path('current/', views.currenttodos, name='currenttodos'),
    path('completed/', views.completedtodos, name='completedtodos'),
    path('todo/<int:todo_pk>', views.viewtodo, name='viewtodo'),
    path('todo/<int:todo_pk>/complete', views.completetodo, name='completetodo'),
    path('todo/<int:todo_pk>/delete', views.deletetodo, name='deletetodo'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)