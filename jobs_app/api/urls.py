from django.urls import path,include
from jobs_app.api.views import job_list,job_details,show_platform,platform_list,review_list,review_detail,review_create,platform_vs,User_review,job_list1
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'sites',platform_vs,basename='platfrom-sites')


urlpatterns = [
    path("list/",job_list.as_view(),name="job-list"),
    path("<int:pk>",job_details.as_view(),name="job-details"),
    path('list1/',job_list1.as_view(),name="job-list1"),
    # path("sites/",show_platform.as_view(),name="job-site"),
    # path("sites/<int:pk>",platform_list.as_view(),name="platform-list"),
    path("",include(router.urls)),
    path("sites/<int:pk>/review/",review_list.as_view(),name='review-list'),
    path("sites/review/<int:pk>",review_detail.as_view(),name='review_detail'),
    path("sites/review/create/<int:pk>",review_create.as_view(),name="review-create"),
    # path('review/<str:username>',User_review.as_view(),name="user-review")
    path('review/',User_review.as_view(),name="user-review")
]