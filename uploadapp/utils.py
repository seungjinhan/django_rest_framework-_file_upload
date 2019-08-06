

# 이미지 확장자 리스트
file_img_ext_list = ".AI,.BMP,.GIF,.JPG,.JPEG,.JPE,.JFIF,.JP2,.J2C,.PCX,.PNG,.PSD,.TGA,.TAGA,.TIF"

# 이미지 확장자 여부 확인
# . 포함해서 조회
def is_image( ext):   
    return ext.upper() in file_img_ext_list   