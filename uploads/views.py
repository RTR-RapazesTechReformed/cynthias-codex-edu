import boto3
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import UploadLog
from django.http import JsonResponse
import json

# Create your views here.

s3_client = boto3.client('s3', aws_access_key_id="ASIAUWEMPCBHHLWHRHCF", aws_secret_access_key="xxTrjrro1QcKue0ALZBTf0xEzudXIjocZaBVy8uW", region_name="us-east-1")


def index(request):
    return render(request, 'uploads/index.html')


@staff_member_required
def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES.get('file')
        

        # Verifica se o arquivo foi enviado com sucesso
        try:
            s3_client.upload_fileobj(file, settings.AWS_STORAGE_BUCKET_NAME, file.name)
            s3_client.head_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=file.name)
            UploadLog.objects.create(filename=file.name, uploaded_by=request.user.username)
            return JsonResponse({'message': 'Upload bem-sucedido', 'filename': file.name})
        except s3_client.exceptions.ClientError as e:
            return JsonResponse({'message': f'Erro ao verificar o upload no S3 error: {str(e)}', 'error': str(e)}, status=500)

    return render(request, 'uploads/upload.html')
