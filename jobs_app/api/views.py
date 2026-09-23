from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from jobs_app.models import job,platform,company_review
from jobs_app.api.serializer import jobSerializer,platformSerializer,reviewSerializer
from rest_framework import generics
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from jobs_app.api.permission import AdminOrReadOnly,ReviewUserOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle,ScopedRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from jobs_app.api.pagination import job_list1_pagination,job_list1_cpagination

# ---------------------------generic api-----------------------------

class User_review(generics.ListAPIView):            #filltering
    serializer_class=reviewSerializer
    # def get_queryset(self):
    #     username=self.kwargs['username']
    #     return company_review.objects.filter(review_user__username=username)
    def get_queryset(self):
        username=self.request.query_params.get('username',None)
        return company_review.objects.filter(review_user__username=username)




class review_create(generics.CreateAPIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    serializer_class=reviewSerializer
    # throttle_classes=[UserRateThrottle,AnonRateThrottle]
    
    
    def get_queryset(self):
        return company_review.objects.all()
    
    
    def perform_create(self, serializer):
        pk=self.kwargs.get('pk')
        job_review=job.objects.get(pk=pk)
        review_user=self.request.user
        review_queryset=company_review.objects.filter(job=job_review,review_user=review_user)
        if review_queryset.exists():
            raise ValidationError("you have already review this job")
        
        serializer.save(job=job_review,review_user=review_user)
    
    
    
class review_list(generics.ListAPIView):
    # queryset=company_review.objects.all()
    serializer_class=reviewSerializer
    # permission_classes=[AdminOrReadOnly]
    
    def get_queryset(self):
        pk=self.kwargs['pk']
        return company_review.objects.filter(job=pk)

class review_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=company_review.objects.all()
    serializer_class=reviewSerializer
    permission_classes=[ReviewUserOrReadOnly]
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='review-detail'
    
    


# class platform_vs(viewsets.ViewSet):
#     def list(self,request):
#         queryset=platform.objects.all()
#         serializer=platformSerializer(queryset,many=True)
#         return Response(serializer.data)
    
#     def retrieve(self,request,pk=None):
#         queryset=platform.objects.all()
#         job_list=get_object_or_404(queryset,pk=pk)
#         serializer=platformSerializer(job_list)
#         return Response(serializer.data)
    
class platform_vs(viewsets.ModelViewSet):
    queryset=platform.objects.all()
    serializer_class=platformSerializer
    permission_classes=[AdminOrReadOnly]
    
    


class show_platform(APIView):
    permission_classes=[AdminOrReadOnly]
    def get(self,request):
        site=platform.objects.all()
        serializer=platformSerializer(site,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=platformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class platform_list(APIView):
    permission_classes=[AdminOrReadOnly]
    def get(self,request,pk):
        try:
            site=platform.objects.get(pk=pk)
        except platform.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer=platformSerializer(site)
        return Response(serializer.data)
    def put(self,request,pk):
        site=platform.objects.get(pk=pk)
        serializer=platformSerializer(site,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
           return Response(serializer.errors) 
    def delete(self,request,pk):
        site=platform.objects.get(pk=pk)
        site.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
    

class job_list1(generics.ListAPIView):
    queryset=job.objects.all()
    serializer_class=jobSerializer
    pagination_class=job_list1_cpagination
    # filter_backends=[filters.SearchFilter]
    # search_fields=['job_title','location']
    # filter_backends=[filters.OrderingFilter]
    # ordering_fields=['salary']
    

class job_list(APIView):
    permission_classes=[AdminOrReadOnly]
    # authentication_classes=[TokenAuthentication]
    def get(self,request):
        jobs=job.objects.all()
        serializer=jobSerializer(jobs,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=jobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class job_details(APIView):
    permission_classes=[AdminOrReadOnly]
    # authentication_classes=[TokenAuthentication]
    def get(self,request,pk):
        try:
            detail=job.objects.get(pk=pk)
        except job.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=jobSerializer(detail)
        return Response(serializer.data)
    def put(self,request,pk):
        detail=job.objects.get(pk=pk)
        serializer=jobSerializer(detail,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,pk):
        detail=job.objects.get(pk=pk)
        detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







# @api_view(['GET','POST'])             ---------api based function------------
# def job_list(request):
#     if request.method == 'GET':
#         jobs=job.objects.all()
#         serializer=jobSerializer(jobs,many=True)
#         return Response(serializer.data)
#     if request.method =='POST':
#         serializer=jobSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
# @api_view(['GET','PUT','DELETE'])
# def job_details(request,pk):
#     if request.method=='GET':
#         try:
#             detail=job.objects.get(pk=pk)
#         except job.DoesNotExist:
#             return Response("error job not found",status=status.HTTP_404_NOT_FOUND)
#         serializer=jobSerializer(detail)
#         return Response(serializer.data)
#     if request.method=='PUT':
#         detail=job.objects.get(pk=pk)
#         serializer=jobSerializer(detail,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
#     if request.method=='DELETE':
#         detail=job.objects.get(pk=pk)
#         detail.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
