from androguard.misc import AnalyzeAPK
from androguard.util import set_log
from file_oper import find_files_with_extension

import os
import sys

set_log("ERROR")

def find_permission_in_dir(perm_name: str, dir_name: str):
    files = find_files_with_extension(dir_name, ".apk")
    for apk_file in files:
        try:
            full_path = os.path.join(dir_name, apk_file)
            permissions = get_apk_permissions(full_path)
            
            # 检查权限
            for perm in permissions:
                if perm_name in perm:
                    print(f"找到: {apk_file}")
                    print(f"  权限: {perm}")
                    break
        except Exception as e:
            print(f"解析失败 {apk_file}: {e}")

def get_apk_permissions(apk_path: str):
    """
    分析APK文件并返回权限列表
    
    Args:
        apk_path (str): APK文件路径
        
    Returns:
        list: 权限列表
    """
    try:
        # 分析APK文件
        a, d, dx = AnalyzeAPK(apk_path)
        
        # 获取权限列表
        permissions = a.get_permissions()
        
        return permissions
    except Exception as e:
        print(f"分析APK时出错: {e}")
        return []

def get_permissions_of_apk(apk_name: str):
    apk, _, _ = AnalyzeAPK(apk_name)
    permissions = apk.get_permissions()
    return permissions

def main():
    # 检查命令行参数
    if len(sys.argv) != 2:
        print("用法: python apk_permissions.py <APK文件路径>")
        print("示例: python apk_permissions.py app.apk")
        sys.exit(1)
    
    apk_path = sys.argv[1]
    
    # 检查文件是否存在
    if not os.path.exists(apk_path):
        print(f"错误: 文件 '{apk_path}' 不存在")
        sys.exit(1)
    
    # 检查是否为APK文件
    if not apk_path.lower().endswith('.apk'):
        print("警告: 文件扩展名不是.apk，但将继续尝试分析")
    
    # 获取权限列表
    permissions = get_apk_permissions(apk_path)
    
    if permissions:
        print(f"\nAPK文件: {apk_path}")
        print(f"发现 {len(permissions)} 个权限:\n")
        print("=" * 80)
        
        # 按字母顺序排序并显示权限
        for i, permission in enumerate(sorted(permissions), 1):
            # 提取权限名称（去掉android.permission.前缀）
            if '.' in permission:
                perm_name = permission.split('.')[-1]
            else:
                perm_name = permission
            
            # 格式化的输出
            print(f"{permission}")
            #print(f"{i:3d}. {permission}")
            #print(f"    简化名: {perm_name}")
            #print("-" * 80)
    else:
        print("未找到任何权限或分析失败")

if __name__ == "__main__":
    main()
