# django rest framework file upload


### [download source](https://github.com/seungjinhan/django_rest_framework-_file_upload/archive/master.zip)

### install packages
1. pip install django
2. pip install djangorestframework
3. pip install pygments
4. pip install --upgrade git+git://github.com/seungjinhan/python_pytilhan_package.git

### setting fileuploadapp
1. change file save path : **uploadapp/__init__.py**
 --> <u>MEDIA_ROOT = os.path.join( 'E:\\document\\dev\\fileupload', 'media')</u>
2. upload
- url: http://localhost:8000/upload/
- method: post
![upload](/img/20190806_193206.png)

3. result
![result](/img/20190806_193351.png)
![result](/img/20190806_193509.png)
![result](/img/20190806_195527.png)
