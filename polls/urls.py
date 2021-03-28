from django.urls import path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from polls.views import QuestionViewSet, PollViewSet, AttemptViewSet, AnswerViewSet

router = DefaultRouter()

router.register(r'polls', PollViewSet, basename='polls')
router.register(r'questions', QuestionViewSet, basename='question')
router.register(r'attempts', AttemptViewSet, basename='attempt')
router.register(r'answers', AnswerViewSet, basename='answer')

urlpatterns = router.urls
urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token),
]
