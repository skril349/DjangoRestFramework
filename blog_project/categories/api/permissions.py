from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):

        # GET només per usuaris autenticats
        if request.method == "GET":
            return request.user and request.user.is_authenticated

        # Altres mètodes només per staff
        return request.user and request.user.is_staff