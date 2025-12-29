from androguard.misc import AnalyzeAPK
from androguard.util import set_log
from file_oper import find_files_with_extension

import os

set_log("ERROR")

def find_permission_in_dir(perm_name: str, dir_name: str):
    files = find_files_with_extension(dir_name, ".apk")
    for apk_file in files:
        try:
            full_path = os.path.join(dir_name, apk_file)
            apk, _, _ = AnalyzeAPK(full_path)
            permissions = apk.get_permissions()
            
            # 检查权限
            for perm in permissions:
                if perm_name in perm:
                    print(f"找到: {apk_file}")
                    print(f"  权限: {perm}")
                    break
        except Exception as e:
            print(f"解析失败 {apk_file}: {e}")
