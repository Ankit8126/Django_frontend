from django.contrib.auth.models import Group

def user_role_context(request):
    role = None
    if request.user.is_authenticated:
        groups = request.user.groups.values_list('name', flat=True)
        if groups:
            role = groups[0]  # Assuming one role per user
            print("User Role:", role)  # Debug statement
    return {'role': role}