from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from todo import views as todo_views  # Используем alias для todo.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo_views.index, name='index'),# Изменено на todo_views
    path('blog/', include('blog.urls')),
    path('signup/', todo_views.signupuser, name='signupuser'),
    path('login/', todo_views.loginuser, name='loginuser'),
    path('logout/', todo_views.logoutuser, name='logoutuser'),
    path('create/', todo_views.createtodo, name='createtodo'),
    path('current/', todo_views.currenttodos, name='currenttodos'),
    path('completed/', todo_views.completedtodos, name='completedtodos'),
    path('todo/<int:todo_pk>', todo_views.viewtodo, name='viewtodo'),
    path('todo/<int:todo_pk>/complete', todo_views.completetodo, name='completetodo'),
    path('todo/<int:todo_pk>/delete', todo_views.deletetodo, name='deletetodo'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
