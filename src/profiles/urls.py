from django.urls import path
from .views import *

app_name = 'profiles'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', ProfileView.as_view(), name='profile_view'),
    path('update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('education/create', EducationCreateView.as_view(), name='education_create'),
    path('education/<int:pk>/update', EducationUpdateView.as_view(), name='education_update'),
    path('education/<int:pk>/delete', EducationDeleteView.as_view(), name='education_delete'),
    path('experience/create', ExperienceCreateView.as_view(), name='experience_create'),
    path('experience/<int:pk>/update', ExperienceUpdateView.as_view(), name='experience_update'),
    path('experience/<int:pk>/delete', ExperienceDeleteView.as_view(), name='experience_delete'),
    path('award/create', AwardCreateView.as_view(), name='award_create'),
    path('award/<int:pk>/update', AwardUpdateView.as_view(), name='award_update'),
    path('award/<int:pk>/delete', AwardDeleteView.as_view(), name='award_delete'),
]
