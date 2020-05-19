from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('articles/', views.ArticleView.as_view(), name = 'all_article'),
    path('articles/<int:year>/', views.year_archive, name = 'year'),
    path('articles/<int:year>/<int:month>/', views.month_archive , name = 'month' ),
    path('articles/<int:year>/<int:month>/<int:pk>/', views.DetailView.as_view(), name = 'detail'),
] 

"""urlpatterns =[
    path('articles/', views.article_archive),
    path('articles/<int:year>/', views.YearView.as_view()), name = 'year_archive'),
    path('articles/<int:year>/<int:month>/', views.MonthView.as_view(), name = 'month_archive' ),
    path('articles/<int:year>/<int:month>/<int:pk>/', views.DetailView.as_view(), name = 'article_detail'),
    path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),
]"""