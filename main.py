import os
import sys
from PIL import Image
from datetime import datetime



def listar_arquivos(l:list, path:str)-> list[str]:
    for i in os.listdir(path):
        if os.path.isdir(path + '/'+ i): l = listar_arquivos(l, path+'/'+i)
        else: l.append(path + '/' +i)
    return l

def find_date(path) -> None | datetime:
    try:
        img = Image.open(path)
    except Exception as e: print(e); return None

    exif_data = img.getexif()

    date_tags = {36867: 'DateTimeOriginal', 36868: 'DateTimeDigitized', 306: 'DateTime'}
    for tag_id, tag_name in date_tags.items():
        if tag_id in exif_data:
            date_string = exif_data[tag_id]
            dt = datetime.strptime(date_string, '%Y:%m:%d %H:%M:%S')# Passa para datetime
            print(f"{tag_name}: {dt}")
            return dt

def main(path_pasta):
    l = []
    l = listar_arquivos(l, path_pasta)                              # Procura recursivamente todos os arquivos na pasta

    datas =  [find_date(i) for i in l if find_date(i) is not None]  # Acha a data de cada um deles
    dt = str(min(datas).strftime('%Y-%m-%d'))                       # Passa o menor datetime para a formatação que gosto 

    PATH = path_pasta.split('/')                                    # Separa os elementos do path até a pasta (em linux apenas)
    PATH.append(dt + ' ' + PATH.pop())                              # Adiciona a data ao nome da pasta
    path_pasta_novo = '/'.join(PATH)

    os.rename(path_pasta, path_pasta_novo)
    print(f'pasta renomeada para: {path_pasta_novo}')

if __name__ == '__main__':

    path_pasta = sys.argv[1]
    try: #confere
        datetime.strptime(path_pasta.split('/').pop()[:10], '%Y-%m-%d')
        print('A sua pasta já tem data, essa execução não terá efeito')
    except ValueError:
        main(path_pasta)
