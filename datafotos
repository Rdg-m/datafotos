import os
import re
import argparse
from PIL import Image
from datetime import datetime



def listar_arquivos(l:list, path:str)-> list[str]:
    for i in os.listdir(path):
        if os.path.isdir(path + '/'+ i): 
            l = listar_arquivos(l, path+'/'+i)
        else: l.append(path + '/' +i)
    return l

def find_date(path, verbose=False) -> None | datetime:
    try:
        img = Image.open(path)
    except Exception as e: print(e); return None

    exif_data = img.getexif()

    date_tags = {36867: 'DateTimeOriginal', 36868: 'DateTimeDigitized', 306: 'DateTime'}
    for tag_id, _ in date_tags.items():
        if tag_id in exif_data:
            date_string = exif_data[tag_id]
            dt = datetime.strptime(date_string, '%Y:%m:%d %H:%M:%S')# Passa para datetime
            if verbose: print(dt)
            return dt

def main(path_pasta, v_flag):
    l = []
    l = listar_arquivos(l, path_pasta)                              # Procura recursivamente todos os arquivos na pasta
    if v_flag: print(l)

    datas =  [find_date(i, verbose=v_flag) for i in l if find_date(i) is not None]  # Acha a data de cada um deles
    dt = str(min(datas).strftime('%Y-%m-%d'))                       # Passa o menor datetime para a formatação que gosto 
    if v_flag: print(dt)

    PATH = path_pasta.split('/')                                    # Separa os elementos do path até a pasta (em linux apenas)
    PATH.append(dt + ' ' + PATH.pop())                              # Adiciona a data ao nome da pasta
    path_pasta_novo = '/'.join(PATH)

    os.rename(path_pasta, path_pasta_novo)
    print(f'Pasta renomeada para: {path_pasta_novo}')

if __name__ == '__main__':
    # setup para CLI
    parser = argparse.ArgumentParser(description='Rename folder based on oldest photo date')
    parser.add_argument('-p', '--path', required=True, help='Path to folder to rename')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    
    if re.match(r'^\d{4}-\d{2}-\d{2}', args.path.split('/')[-1]):
        if args.verbose: print('A pasta já tem data, não executarei')
    else:
        main(args.path, args.verbose)

