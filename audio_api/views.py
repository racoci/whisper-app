from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView


class AudioUploadView(APIView):
    parser_classes = [FileUploadParser]

    def dispatch(self, request, *args, **kwargs):
        # Log the request method and path
        print(f"Request: {request.method} {request.path}")

        # Log request headers
        try:
            print("Request headers:")
            for header, value in request.headers.items():
                print(f"  {header}: {value}")
        except:
            print("No headers in the current request")
        # Log request parameters
        try:
            print("Request query parameters:")
            for key, value in request.query_params.items():
                print(f"  {key}: {value}")
        except:
            print("No request parameters in the current request")

        # Log request body (only a sample)
        try:
            body_sample = request.body[:100]  # Log only first 100 characters
            print(f"Request body (sample): {body_sample}")
        except:
            print("No body in the current request")

        # Log request files
        try:
            print("Request files:")
            for field_name, file_obj in request.FILES.items():
                print(f"  {field_name}: {file_obj.name} ({file_obj.content_type})")
        except:
            print("No files in the current request!")

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
