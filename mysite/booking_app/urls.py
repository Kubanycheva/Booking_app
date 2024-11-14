from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'hotels', HotelListViewSet, basename='hotel-list')
router.register(r'hotel-detail', HotelDetailViewSet, basename='hotel-detail')
router.register(r'users', UserProfileViewSet, basename='user-detail')
router.register(r'room', RoomListViewSet, basename='room-list')
router.register(r'room-detail', RoomDetailViewSet, basename='room-detail')
router.register(r'booking', BookingViewSet, basename='book-list')
router.register(r'review', ReviewViewSet, basename='review-list')
router.register(r'review-detail', ReviewViewSet, basename='review-detail')
router.register(r'hotel_image', HotelImageViewSet, basename='hotel_image-detail')
router.register(r'room_image', RoomImageViewSet, basename='room_image-detail')


urlpatterns = [
    path('', include(router.urls))
]




#
# urlpatterns = [
#
#     path('', HotelListViewSet.as_view({'get': 'list', 'post': 'create'}), name='hotel_list'),
#     path('<int:pk>/', HotelDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
#                                                'delete': 'destroy'}), name='hotel_detail'),
#
#
#     path('users', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='users_list'),
#     path('users/<int:pk>/', UserProfileSimpleViewSet.as_view({'get': 'retrieve', 'put': 'update',
#                                                  'delete': 'destroy'}), name='users_detail'),
#
#
#     path('hotel_image', HotelImageViewSet.as_view({'get': 'list', 'post': 'create'}), name='hotel_list'),
#     path('hotel_image/<int:pk>/', HotelImageViewSet.as_view({'get': 'retrieve', 'put': 'update',
#                                                  'delete': 'destroy'}), name='hotel_detail'),
#
#
#     path('room', RoomListViewSet.as_view({'get': 'list', 'post': 'create'}), name='room_list'),
#     path('room/<int:pk>/', RoomDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
#                                                              'delete': 'destroy'}), name='room_detail'),
#
#     path('room_image', RoomImageViewSet.as_view({'get': 'list', 'post': 'create'}), name='room_image_list'),
#     path('room_image/<int:pk>/', RoomImageViewSet.as_view({'get': 'retrieve', 'put': 'update',
#                                                              'delete': 'destroy'}), name='room_image_detail'),
#
#     path('review', ReviewViewSet.as_view({'get': 'list', 'post': 'create'}), name='review_list'),
#     path('review/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve', 'put': 'update',
#                                                              'delete': 'destroy'}), name='review_detail'),
#
#     path('booking', BookingViewSet.as_view({'get': 'list', 'post': 'create'}), name='booking_list'),
#     path('booking/<int:pk>/', BookingViewSet.as_view({'get': 'retrieve', 'put': 'update',
#                                                     'delete': 'destroy'}), name='booking_detail')
#
# ]















