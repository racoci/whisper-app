from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView


class AudioUploadView(APIView):
    parser_classes = [FileUploadParser]

    def post(self, request, *args, **kwargs):
        file_obj = request.FILES['file']
        # Process the uploaded file as needed
        return Response({'status': 'File uploaded successfully'}, status=status.HTTP_200_OK)
