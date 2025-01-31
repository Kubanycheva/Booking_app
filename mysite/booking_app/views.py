from rest_framework import viewsets, permissions
from .serializers import *
from .models import *
from .filters import HotelFilter, RoomFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework. filters import SearchFilter, OrderingFilter
from .permissions import (CheckOwner, CheckCRUD, CheckHotelOwner, CheckRoom, CheckBooking, CheckReview,
                          CheckRoomOwner, CheckUpdateBooking, CheckImage)

from .paginations import RoomPagination


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileSimpleViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSimpleSerializer


class HotelImageViewSet(viewsets.ModelViewSet):
    queryset = HotelImage.objects.all()
    serializer_class = HotelImageSerializer
    permission_classes = [CheckImage]


class RoomListViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['room_number']
    ordering_fields = ['room_price']
    filterset_class = RoomFilter
    permission_classes = [CheckRoomOwner]
    # pagination_class = RoomPagination


class RoomDetailViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer
    permission_classes = [CheckRoom, CheckRoomOwner]


class RoomImageViewSet(viewsets.ModelViewSet):
    queryset = RoomImage.objects.all()
    serializer_class = RoomImageSerializer
    permission_classes = [CheckImage]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated, CheckOwner, CheckReview]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [CheckBooking, CheckUpdateBooking]


class HotelListViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = HotelFilter
    search_fields = ['hotel_name']
    ordering_fields = ['hotel_stars']
    permission_classes = [CheckCRUD]


class HotelDetailViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializer
    permission_classes = [CheckCRUD, CheckHotelOwner]

