from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_api_view = [
            "Uses HTTP methods as functions (get, post, patch, put, delete)",
            "Is similiar to a traditional Django View",
            "Gives you the most control over your application logic",
            "Is mapped manually to URLs",
        ]

        return Response({"message": "Hello!", "an_api_view": an_api_view})


class ShalomApiView(APIView):
    """Test API View of my own"""

    def get(self, request, format=None):
        """Returns a list of APIView features in Hebrew"""

        an_api_view = [
            "משתמש בשיטות רשת כאל פונקציות",
            "דומה מאוד למראה מסורתי במערכת דגנגו",
        ]

        return Response({"message": "Shalom!", "an_api_view": an_api_view})
