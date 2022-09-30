from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    # Uprawnienie niestandardowe, aby tylko właściciele obiektu mogli go edytować
    def has_object_permission(self, request, view, obj):
        # Uprawnienia do odczytu są dozwolone dla każdego żądania, więc zawsze zezwalamy na żądania GET, HEAD lub OPTIONS.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Uprawnienia do zapisu są dozwolone tylko dla właściciela fragmentu
        return obj.owner == request.user
