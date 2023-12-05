from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Request URLs 
    path('create_request/<int:id>', views.create_request, name='create_request'),
    path('show_all_request/', views.show_all_request, name='show_all_request'),
    path('update_request/<int:id>/', views.update_request, name='update_request'),
    path('delete_request/<int:id>/', views.delete_request, name='delete_request'),
    path('delete_all_request/', views.delete_all_request, name='delete_all_request'),
    path('create_request_pdf/', views.create_request_pdf, name='create_request_pdf'),
    path('add_favorite_request/', views.add_favorite_request,
         name='add_favorite_request'),


    # Review URLs
    path('create_custom_review/', views.create_custom_review,name='create_custom_review'), 
    path('create_master_review/', views.create_master_review,name='create_master_review'), 
    path('show_all_review/', views.show_all_review,name='show_all_review'), 
    path('update_review/<int:review_id>/', views.update_review, name='update_review'),
    path('getCustomRequestForReview/<int:id>', views.getCustomRequestForReview,name='getCustomRequestForReview'), 
    path('save_review_report/', views.save_review_report,name='save_review_report'), 
    path('delete_review/<int:id>/', views.delete_review, name='delete_review'),
    path('delete_all_review/', views.delete_all_review, name='delete_all_review'),
    path('create_review_pdf/', views.create_review_pdf, name='create_review_pdf'),
    path('add_favorite_review/', views.add_favorite_review,
         name='add_favorite_review'),
]



