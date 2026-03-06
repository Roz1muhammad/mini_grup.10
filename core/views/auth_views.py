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

        if None in [fullname, username, age, gender, role]:
            return Response({
                "error": "kerakli, polyalar to'lliq emas"
            }, status=403)

        user = User.objects.filter(username=username).first()
        if user:
            raise AuthenticationFailed("user already exist")

        return Response({
            'message': "hozircha hammasi cho'tki"
        })







