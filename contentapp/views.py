from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Content
from .serializers import ContentSerializer
from django.http import Http404


class ContentListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        search_terms = request.query_params.get('search', '')
        contents = Content.objects.filter(title__icontains=search_terms) | \
                   Content.objects.filter(body__icontains=search_terms) | \
                   Content.objects.filter(summary__icontains=search_terms) | \
                   Content.objects.filter(categories__icontains=search_terms)
        serializer = ContentSerializer(contents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContentDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            content = Content.objects.get(pk=pk)
            return content
        except:
            pass

    def get(self, request, pk):
            content = self.get_object(pk)
            if request.user == content.created_by or request.user.is_staff:
                serializer = ContentSerializer(content)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'detail': 'You do not have permission to view this content'}, status=status.HTTP_403_FORBIDDEN)

    def put(self, request, pk):
        content = self.get_object(pk)
        if request.user == content.created_by or request.user.is_staff:
            serializer = ContentSerializer(content, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail': 'You do not have permission to edit this content'}, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, pk):
        content = self.get_object(pk)
        if request.user == content.created_by or request.user.is_staff:
            content.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'detail': 'You do not have permission to delete this content'}, status=status.HTTP_403_FORBIDDEN)