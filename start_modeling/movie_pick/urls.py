from django.urls import path
from . import views

app_name = "products"
# 여러 app을 만들었을 때 겹치는 것을 방지하기 위해 namespace를 설정.
urlpatterns = [
    path('', views.name, name ="name"),
    path('main/', views.main, name = "main"),
    path('interesting/', views.interesting, name = "interesting"),
    path('list/', views.list, name = "list"),
    path('<int:id>/', views.show, name="show"),
    path('edit/<int:id>/', views.edit, name="edit"),
    path('update/<int:id>/', views.update, name="update"),
    path('delete/<int:id>/', views.delete, name="delete"),
#id 라는 이름으로, 그 타입은 integer로 주소로 보낼 것이다.
#그럼 저 id를 int type인 id를 views에서 받을 수 있어야겠구나.
]