from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from uploadapp.serializers import FileSerializer
import os
from uploadapp.utils import is_image
from uploadapp import  file_upload_path
from django.http.request import QueryDict
from pytilhan.utils import log_util


class FileView( APIView):
    
    parser_classes = (MultiPartParser, FormParser)
    
    def post(self, req, *args, **kwargs):

        # 요청된 데이터를 꺼냄( QueryDict)         
        new_data = req.data.dict()
        
        # 요청된 파일 객체
        file_name = req.data['file_name']
        
        # 저장될 파일의 풀path를 생성        
        new_file_full_name = file_upload_path( file_name.name)
        
        # 새롭게 생성된 파일의 경로
        file_path = '\\'.join(new_file_full_name.split('\\')[0:-1])        
        
        # 파일 확장자
        file_ext = os.path.splitext(file_name.name)[1]
        
        # QueryDict에 새로운 데이터 추가( DB와 매핑을 위해서)
        new_data['file_ext'] = file_ext
        new_data['is_img'] = is_image( file_ext)
        new_data['file_path'] = file_path
        new_data['file_origin_name'] = req.data['file_name'].name
        new_data['file_save_name'] = req.data['file_name']
        
        new_query_dict = QueryDict('', mutable=True)
        new_query_dict.update( new_data)
        
        file_serializer = FileSerializer(data = new_query_dict)
        if file_serializer.is_valid():
            
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            file_serializer.save()       
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!2")
            
            print( file_serializer.data)
                 
            return Response( status=status.HTTP_201_CREATED)
        else:
            
            log_util.error(__name__ , file_serializer.errors)
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
