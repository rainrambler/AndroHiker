#!/usr/bin/env python3
import os
import sys
import subprocess
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed

def process_apk(apk_path, target_permission, verbose=False):
    """处理单个APK文件"""
    if verbose:
        print(f"检查: {apk_path}")
    
    aapt_path = r"C:\Program Files\dotnet\packs\Microsoft.Android.Sdk.Windows\35.0.78\tools\aapt2.exe"
    try:
        result = subprocess.run(
            [aapt_path, 'd', 'permissions', apk_path],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0 and target_permission.lower() in result.stdout.lower():
            return apk_path
    except:
        pass
    return None

def main():
    parser = argparse.ArgumentParser(description='在APK文件中搜索特定权限（多线程版）')
    parser.add_argument('directory', help='要搜索的目录路径')
    parser.add_argument('permission', help='要搜索的权限名称')
    parser.add_argument('--verbose', '-v', action='store_true', help='显示详细输出')
    parser.add_argument('--threads', '-t', type=int, default=4, help='线程数（默认: 4）')
    
    args = parser.parse_args()
    
    # 查找APK文件
    apk_files = []
    for root, dirs, files in os.walk(args.directory):
        for file in files:
            if file.lower().endswith('.apk'):
                apk_files.append(os.path.join(root, file))
    
    print(f"找到 {len(apk_files)} 个APK文件")
    
    # 使用线程池并行处理
    matching_apks = []
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        future_to_apk = {
            executor.submit(process_apk, apk, args.permission, args.verbose): apk 
            for apk in apk_files
        }
        
        for future in as_completed(future_to_apk):
            result = future.result()
            if result:
                matching_apks.append(result)
                print(f"✓ 匹配: {result}")
    
    # 输出结果
    print(f"\n包含权限 '{args.permission}' 的APK: {len(matching_apks)}/{len(apk_files)}")
    for apk in matching_apks:
        print(f"  - {apk}")

if __name__ == "__main__":
    main()