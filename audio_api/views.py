from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView


class AudioUploadView(APIView):
    parser_classes = [FileUploadParser]

    def dispatch(self, request, *args, **kwargs):
        print("Request:", request)
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            file_obj = request.FILES.get('file')
            print("File object:", file_obj)
            if file_obj:
                # Process the file
                print("File name:", file_obj.name)
                print("Content type:", file_obj.content_type)
                # Save the file, if required

                return Response({'status': 'File uploaded successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print("Error:", e)
            return Response({'error': 'An error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
