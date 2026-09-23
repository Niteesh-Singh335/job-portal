from rest_framework.decorators import api_view
from user_app.api.serializer import register_serializer
from rest_framework.response import Response
from user_app import models
from rest_framework.authtoken.models import Token
from rest_framework import status


@api_view(['POST'])
def logout_view(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def register_view(request):
    
    serializer=register_serializer(data=request.data)
    data={}
    if serializer.is_valid():
        account=serializer.save()
        data['username']=account.username
        data['email']=account.email
        token=Token.objects.get(user=account).key
        data['token']=token
    else:
        data=serializer.errors
    return Response(data,status=status.HTTP_201_CREATED)
    # return Response(serializer.errors, status=400)