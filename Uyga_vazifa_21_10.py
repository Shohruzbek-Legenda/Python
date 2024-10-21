import os
import shutil

def popka_yaratish():
    folder_path = 'D:/Man_bekorchiman'
    os.makedirs(folder_path, exist_ok=True)
    print(f"Popka yaratildi _ : {folder_path}")

def fayl_yaratish():
    folder_path = 'D:/Man_bekorchiman'
    for i in range(1, 5):
        with open(os.path.join(folder_path, f'fayl_{i}.txt'), 'w') as f:
            f.write(f'Bu fayl {i}.')
    print("4 ta fayl yaratildi _ ")

def popka_nushalash(src_folder):
    dest_folder = 'D:/Man_bekorchiman/nushalangan_popka'
    shutil.copytree(src_folder, dest_folder)
    print(f"{src_folder} popkasi nushalandi _ : {dest_folder}")

def popka_ochirish(folder_path):
    shutil.rmtree(folder_path)
    print(f"Popka o'chirildi _ : {folder_path}")

def file_ochirish(file_path):
    os.remove(file_path)
    print(f"Fayl ochirildi _ : {file_path}")

def bosh_popkani_ochirish(folder_path):
    os.rmdir(folder_path)
    print(f"Bosh popka ochirildi _ : {folder_path}")

def fayl_soni(folder_path):
    num_files = len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])
    print(f"Fayllani soni _ : {num_files}")
    return num_files

def popka_soni(folder_path):
    num_folders = len([f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))])
    print(f"Popkalana soni _ : {num_folders}")
    return num_folders

if __name__ == '__main__':
    popka_yaratish()
    fayl_yaratish()
    fayl_soni('D:/Man_bekorchiman')
    popka_soni('D:/Man_bekorchiman')
    # file_ochirish()
    # bosh_popkani_ochirish()
