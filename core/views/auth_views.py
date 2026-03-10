from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models.auth_models import User
from rest_framework.exceptions import AuthenticationFailed

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        fullname = request.data.get("fullname", None)
        username = request.data.get("username", None)
        age = request.data.get('age', None)
        gender = request.data.get("gender", None)
        role = request.data.get("role", None)
        password = request.data.get("password", None)

        if None in [fullname, username, age, gender, role, password]:
            return Response({
                "error": "kerakli, polyalar to'lliq emas"
            }, status=403)

        user = User.objects.filter(username=username).first()

        if user:
            raise AuthenticationFailed("user already exist")

        if 3 > len(password):
            return Response({
                "message": "parol judayam kichkina"
            })

        elif len(password) >= 14:
            return Response({
                "message": "parol judayam katta"
            })

        kerak = {
            "son": 0,
            "harf": 0
        }

        for i in password:
            if i.isdigit():
                kerak['son'] +=1
            if i.isalpha():
                kerak['harf'] +=1

        if 0 in [kerak['son'], kerak['harf']]:
            return Response({
                "message": "parolda harf bilan son qatnalishi shart"
            })

        clear_data = {
            "fullname": fullname,
            "username": username,
            "age": age,
            "gender": gender,
            "role": role,
            "password": password
        }
        user = User.objects.create_user(**clear_data)

        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "user": user.response(),
            "access_token": token.key
        })







