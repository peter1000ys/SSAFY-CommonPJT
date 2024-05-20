from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    ReviewListSerializer,
    ReviewSerializer,
    ReviewDetailSerializer,
    CommentListSerializer,
    CommentSerializer,
)
from .models import Review, Comment
from accounts.models import User
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.views import APIView
from rest_framework import status

from django.http import HttpResponse, JsonResponse


# 리뷰 조회, 리뷰 작성 기능
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def review_list(request):
    if request.method == "GET":
        reviews = Review.objects.all()
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(["GET",])
@permission_classes([IsAuthenticated])
def review_detail(request, review_pk):
    if request.method == "GET":
        review = Review.objects.get(pk=review_pk)
        serializer = ReviewDetailSerializer(review)
        return Response(serializer.data)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def review_like(request, review_pk, user_pk):
    review = Review.objects.get(pk=review_pk)
    user = User.objects.get(pk=user_pk)
    if request.method == "POST":
        if review.like_users.filter(pk=user.pk).exists():
            review.like_users.remove(user)
            like = False
        else:
            review.like_users.add(user)
            like = True
        like_status = {
            "liked": like,
            "count": review.like_users.count(),
        }
        return JsonResponse(like_status)
    elif request.method == "GET":
        if review.like_users.filter(pk=user.pk).exists():
            like = True
        else:
            like = False
        like_status = {
            "liked": like,
            "count": review.like_users.count(),
        }
        return JsonResponse(like_status)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def review_hate(request, review_pk, user_pk):
    review = Review.objects.get(pk=review_pk)
    user = User.objects.get(pk=user_pk)
    if request.method == "POST":
        if review.hate_users.filter(pk=user.pk).exists():
            review.hate_users.remove(user)
            hate = False
        else:
            review.hate_users.add(user)
            hate = True
        hate_status = {
            "hated": hate,
            "count": review.hate_users.count(),
        }
        return JsonResponse(hate_status)
    elif request.method == "GET":
        if review.hate_users.filter(pk=user.pk).exists():
            hate = True
        else:
            hate = False
        hate_status = {
            "hated": hate,
            "count": review.hate_users.count(),
        }
        return JsonResponse(hate_status)

# 리뷰 < - 댓글 조회, 작성 기능
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def review_comment(request, review_pk):
    if request.method == "GET":
        comments = Comment.objects.filter(review=review_pk)
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def review_comment_like(request, review_pk, comment_pk, user_pk):
    comment = Comment.objects.get(pk=comment_pk)
    user = User.objects.get(pk=user_pk)
    if request.method == "POST":
        if comment.like_users.filter(pk=user.pk).exists():
            comment.like_users.remove(user)
            like = False
        else:
            comment.like_users.add(user)
            like = True
        like_status = {
            "liked": like,
            "count": comment.like_users.count(),
        }
        return JsonResponse(like_status)
    elif request.method == "GET":
        if comment.like_users.filter(pk=user.pk).exists():
            like = True
        else:
            like = False
        like_status = {
            "liked": like,
            "count": comment.like_users.count(),
        }
        return JsonResponse(like_status)

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def review_comment_hate(request, review_pk, comment_pk, user_pk):
    comment = Comment.objects.get(pk=comment_pk)
    user = User.objects.get(pk=user_pk)
    if request.method == "POST":
        if comment.hate_users.filter(pk=user.pk).exists():
            comment.hate_users.remove(user)
            hate = False
        else:
            comment.hate_users.add(user)
            hate = True
        hate_status = {
            "hated": hate,
            "count": comment.hate_users.count(),
        }
        return JsonResponse(hate_status)
    elif request.method == "GET":
        if comment.hate_users.filter(pk=user.pk).exists():
            hate = True
        else:
            hate = False
        hate_status = {
            "hated": hate,
            "count": comment.hate_users.count(),
        }
        return JsonResponse(hate_status)
