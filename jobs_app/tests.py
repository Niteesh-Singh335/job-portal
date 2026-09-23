from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from jobs_app.api import serializer
from jobs_app import models


class platfornTestcase(APITestCase):
    def setUp(self):
        self.user=User.objects.create_user(username="example1",password="password@123")
        self.token=Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)
        self.site=models.platform.objects.create(name="indeed",
                                platform_link="http://indeed.com",hr="nitesh")
    def test_platform_create(self):
        data={
            "name":"indeed",
            "platform_link":"https://indeed.com",
            "hr":"nitesh"
        }
        response=self.client.post(reverse("platfrom-sites-list"),data)
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)
    def test_platform_list(self):
        response=self.client.get(reverse('platfrom-sites-list'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    def test_plaform_detail(self):
        response=self.client.get(reverse("platfrom-sites-detail",args=(self.site.id,)))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
        
class jobTestcase(APITestCase):
    
    def setUp(self):
        self.user=User.objects.create_user(username="example",password="password@123")
        self.token=Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)
        self.site=models.platform.objects.create(name="indeed",
                                platform_link="http://indeed.com",hr="nitesh")
        self.job=models.job.objects.create(job_platform=self.site,salary="20000")
        
    def test_job_create(self):
        data={
            "salary":"20000"
        }
        response=self.client.post(reverse("job-list"),data)
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)
    def test_job_list(self):
        response=self.client.get(reverse('job-list'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    def test_job_detail(self):
        response=self.client.get(reverse("job-details",args=(self.job.id,)))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
class reviewTestcase(APITestCase):
    def setUp(self):
        self.user=User.objects.create_user(username="example",password="password@123")
        self.token=Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)
        self.site=models.platform.objects.create(name="indeed",
                                        platform_link="http://indeed.com",hr="nitesh")
        self.job=models.job.objects.create(job_platform=self.site,salary="20000")
        self.job1=models.job.objects.create(job_platform=self.site,salary="20000")
        self.review=models.company_review.objects.create(review_user=self.user,hiring_rate=350,
                        about_company="best hiring",job=self.job1)

        
        
        
    def test_review_create(self):
        data={
            "review_user":self.user,
            "hiring_rate":300,
            "about_company":"best hiring",
            "job":self.job.id
        }
        response=self.client.post(reverse("review-create",args=(self.job.id,)),data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        response=self.client.post(reverse("review-create",args=(self.job.id,)),data)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        
    def test_review_unauth(self):
        data={
                    "review_user":self.user,
                    "hiring_rate":300,
                    "about_company":"best hiring",
                    "job":self.job.id
                }
        self.client.force_authenticate(user=None)
        response=self.client.post(reverse("review-create",args=(self.job.id,)),data)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)
                
        
    def test_review_update(self):
        data={
            "review_user":self.user,
            "hiring_rate":350,
            "about_company":"best hiring",
            "job":self.job.id
        }
        response=self.client.put(reverse('review_detail',args=(self.review.id,)),data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    def test_review_list(self):
        response=self.client.get(reverse('review-list',args=(self.job.id,)))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    def test_review_detail(self):
        response=self.client.get(reverse('review-list',args=(self.review.id,)))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    def test_review_user(self):
        response=self.client.get('/jobs/review/?username'+self.user.username)
        self.assertEqual(response.status_code,status.HTTP_200_OK)