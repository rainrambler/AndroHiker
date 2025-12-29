import os
import unicodedata
import re

def append_line_to_file(file_path: str, line: str, append_newline: bool = True):
    ''' Append a line to a file. '''
    line_new = line
    if append_newline:
        line_new = line_new + "\n"
    try:
        with open(file_path, 'a+', encoding ='utf-8') as file:
            file.write(line_new)
    except Exception as e:
        print(f"Error: {e}")

def find_files_with_extension(directory, extension):
    """
    查找目录下指定扩展名的所有文件。
    :param directory: 目标目录
    :param extension: 文件扩展名（如 ".txt"）
    :return: 符合条件的文件路径列表
    """
    matching_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                matching_files.append(os.path.join(root, file))
    return matching_files

def dir_exists(dir0: str) -> bool:
    ''' Check directory exists '''
    if not os.path.exists(dir0):
        return False
    return os.path.isdir(dir0)

def file_exists(filename: str) -> bool:
    ''' Check file exists '''
    if not os.path.exists(filename):
        return False
    return os.path.isfile(filename)

def delete_file(file_path: str):
    ''' Delete a file. '''
    try:
        os.remove(file_path)
        print(f"{file_path} has been deleted successfully.")
    except FileNotFoundError:
        print(f"{file_path} does not exist.")
    except PermissionError:
        print(f"Permission denied: {file_path}")
    except Exception as e:
        print(f"Error occurred: {e}")

def get_file_path(filename: str) -> str:
    return os.path.dirname(filename)
