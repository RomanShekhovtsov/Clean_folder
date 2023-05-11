import os
import shutil
import string
import sys


def normalize(name):
    translit_dict = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i',
        'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f',
        'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'sh', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'I',
        'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F',
        'Х': 'H', 'Ц': 'C', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Sh', 'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya'
    }
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)

    normalized_name = ''
    for char in name:
        if char in valid_chars:
            normalized_name += char
        elif char in translit_dict:
            normalized_name += translit_dict[char]
        else:
            normalized_name += '_'

    return normalized_name

def process_folder(folder_path):
    image_extensions = ('JPEG', 'PNG', 'JPG', 'SVG')
    video_extensions = ('AVI', 'MP4', 'MOV', 'MKV')
    document_extensions = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
    audio_extensions = ('MP3', 'OGG', 'WAV', 'AMR')
    archive_extensions = ('ZIP', 'GZ', 'TAR')

    known_extensions = set()
    unknown_extensions = set()

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_name, file_ext = os.path.splitext(file)
            file_ext = file_ext[1:].upper()
            known_extensions.add(file_ext)

            if file_ext in image_extensions:
                destination_folder = os.path.join(folder_path, 'images')
                process_file(file, root, destination_folder)
            elif file_ext in video_extensions:
                destination_folder = os.path.join(folder_path, 'video')
                process_file(file, root, destination_folder)
            elif file_ext in document_extensions:
                destination_folder = os.path.join(folder_path, 'documents')
                process_file(file, root, destination_folder)
            elif file_ext in audio_extensions:
                destination_folder = os.path.join(folder_path, 'audio')
                process_file(file, root, destination_folder)
            elif file_ext in archive_extensions:
                destination_folder = os.path.join(folder_path, 'archives')
                process_archive(file, root, destination_folder)
            else:
                unknown_extensions.add(file_ext)

        # print('Known extensions:', known_extensions)
        # print('Unknown extensions:', unknown_extensions)

def process_file(file, source_folder, destination_folder):
    source_path = os.path.join(source_folder, file)
    destination_path = os.path.join(destination_folder, normalize(file))

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    shutil.move(source_path, destination_path)
    print('Moved:', file)

def process_archive(file, source_folder, destination_folder):
    archive_path = os.path.join(source_folder, file)

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    shutil.unpack_archive(archive_path, destination_folder)

    archive_name, _ = os.path.splitext(file)
    archive_files = os.listdir(destination_folder)

    for archive_file in archive_files:
        archive_file_path = os.path.join(destination_folder, archive_file)
        if os.path.isfile(archive_file_path):
            destination_subfolder = os.path.join(destination_folder, archive_name)
            process_file(archive_file, destination_folder, destination_subfolder)

    shutil.rmtree(destination_folder)
    # print('Unpacked and moved:', file)


def run():
    if len(sys.argv) > 1:
        target_folder = sys.argv[1]
        process_folder(target_folder)
    else:
        print('Please provide the target folder path as a command line argument.')

if __name__ == '__main__':
    run()