from rest_framework.permissions import BasePermission
from rest_framework import permissions


class CheckOwner(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'ownerUser':
            return False
        return True


class CheckCRUD(BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.user_role == 'ownerUser'


class CheckHotelOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class CheckRoom(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.room_status == 'cвободен':
            return True
        return False


class CheckBooking(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'simpleUser':
            return True
        return False


class CheckReview(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.user_name


class CheckRoomOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.hotel_room.owner


class CheckUpdateBooking(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.user_book


# class CheckUpdateBooking(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.user == obj.user_book:
#             return True
#         return False


class CheckImage(BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

