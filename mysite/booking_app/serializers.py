from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['hotel_image']


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['room_image']


class RoomListSerializer(serializers.ModelSerializer):
    room_images = RoomImageSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['room_number', 'room_type', 'room_status', 'room_price',
                  'room_images', 'all_inclusive']


class RoomDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ['id', 'room_number', 'room_type', 'room_status',
                  'room_price', 'all_inclusive', 'room_description', 'hotel_room']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text', 'stars', 'user_name', 'hotel',
                  'parent']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['hotel_book', 'user_book', 'check_in', 'check_out']


class HotelListSerializer(serializers.ModelSerializer):
    hotel_images = HotelImageSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name', 'country',
                  'city', 'hotel_images', 'hotel_stars', 'average_rating']

    def get_average_rating(self, obj):
        return obj.get_average_rating()


class HotelDetailSerializer(serializers.ModelSerializer):
    owner = UserProfileSimpleSerializer()
    reviews = ReviewSerializer(many=True, read_only=True)
    rooms = RoomListSerializer(many=True, read_only=True)
    hotel_images = HotelImageSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = ['hotel_name', 'hotel_description', 'country', 'city', 'address', 'hotel_stars',
                  'hotel_images', 'hotel_video',  'reviews', 'created_date', 'owner', 'rooms']


