from django.urls import path
from game import viv

urlpatterns = [
    path('zeros/',viv.oo),
    path('one/',viv.start),
    path('one/1',viv.start_),
    path('one/2',viv.开始说明),
    path('two/',viv.单个查询),
    path('two/1',viv.查找),
    path('three/',viv.批量),
    path('three/1',viv.批量1),
    path('three/2',viv.批量2),
    path('three/3',viv.批量3),
    path('three/d', viv.d),
]
