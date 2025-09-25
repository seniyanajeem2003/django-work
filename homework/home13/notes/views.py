from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from notes.forms import home13
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from notes.models import home13
from .serializers import NotesSerializer


@api_view(['POST'])
@permission_classes((AllowAny,))
def sign_in(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password: 
        return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists(): 
        return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

    User.objects.create_user(username=username, password=password) 
    return Response({"message": "Account created successfully"}, status=status.HTTP_201_CREATED)



@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},status=HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_note(request):
    title = request.data.get("title")
    message = request.data.get("message")
    if not title or not message:
        return Response({"error": "Title and message are required"}, status=status.HTTP_400_BAD_REQUEST)
    note = home13.objects.create(username=request.user.username, password="", title=title, message=message)
    return Response({"id": note.id, "title": note.title, "message": note.message},
        status=status.HTTP_201_CREATED
    )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_notes(request):
    notes = home13.objects.filter(username=request.user.username)
    serializer= NotesSerializer(notes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)