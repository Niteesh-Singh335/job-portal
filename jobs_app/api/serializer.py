from rest_framework import serializers
from django.contrib.auth.models import User
from jobs_app.models import job,platform,company_review

# ----------------------serializers.ModelSerializer----------------------------


class reviewSerializer(serializers.ModelSerializer):
    review_user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=company_review
        fields='__all__'



class jobSerializer(serializers.ModelSerializer):
    # reviews=reviewSerializer(many=True,read_only=True)
    platform=serializers.CharField(source='job_platform.name',allow_null=True,read_only=True)
    posted_by=serializers.StringRelatedField(read_only=True)
    class  Meta:
        model=job
        fields='__all__'
        # fields=['id','job_title','salary']
        # exclude=['location']


class platformSerializer(serializers.ModelSerializer):
    job=jobSerializer(many=True,read_only=True)
    class Meta:
        model=platform
        fields='__all__'
        
        





# ----------------serializers.Serializer-------------------------------
# class jobSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     job_title=serializers.CharField()
#     salary=serializers.IntegerField()
#     company=serializers.CharField()
#     location=serializers.CharField()
#     description=serializers.CharField()
#     date_and_time=serializers.DateTimeField(read_only=True)
#     posted_by=serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
#     job_type=serializers.CharField()
#     current_working=serializers.BooleanField()
    
#     def create(self,validated_data):
#         return job.objects.create(**validated_data)
#     def update(self,instance,validated_data):
#         instance.job_title=validated_data.get('job_title',instance.job_title)
#         instance.salary=validated_data.get('salary',instance.salary)
#         instance.company=validated_data.get('company',instance.company)
#         instance.location=validated_data.get('location',instance.location)
#         instance.description=validated_data.get('description',instance.description)
#         instance.description=validated_data.get('description',instance.description)
#         instance.date_and_time=validated_data.get('date_and_time',instance.date_and_time)
#         instance.posted_by=validated_data.get('posted_by',instance.posted_by)
#         instance.job_type=validated_data.get('job_type',instance.job_type)
#         instance.current_working=validated_data.get('current_working',instance.current_working)
#         instance.save()
#         return instance