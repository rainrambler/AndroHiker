import os
import subprocess
import sys

def find_img_files(directory):
    """查找目录下所有.img文件"""
    img_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.img'):
                img_files.append(os.path.join(root, file))
    return img_files

def extract_img_file(img_path):
    """解压单个.img文件"""
    # 获取文件名（不含路径和扩展名）
    base_name = os.path.splitext(os.path.basename(img_path))[0]
    
    # 创建输出目录
    output_dir = r"D:\TMP" + "\\" + base_name
    
    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"创建输出目录: {output_dir}")
    
    # 构建命令
    command = [".\\extract.erofs.exe", "-i", img_path, "-x", "-o", output_dir]
    
    print(f"正在解压: {os.path.basename(img_path)}")
    print(f"命令: {' '.join(command)}")
    
    try:
        # 执行命令
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(f"解压成功: {base_name}")
        print(result.stdout)
        if result.stderr:
            print(f"警告: {result.stderr}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"解压失败: {base_name}")
        print(f"错误信息: {e.stderr}")
        return False
    except FileNotFoundError:
        print(f"错误: 找不到 extract.erofs.exe 文件")
        print("请确保 extract.erofs.exe 在当前目录下")
        return False

def main():
    print("=== EROFS镜像解压工具 ===")
    
    # 获取用户输入的目录
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = input("请输入要搜索的目录路径: ").strip()
    
    # 验证目录是否存在
    if not os.path.isdir(directory):
        print(f"错误: 目录不存在 - {directory}")
        input("按回车键退出...")
        return
    
    print(f"正在搜索目录: {directory}")
    
    # 查找所有.img文件
    img_files = find_img_files(directory)
    
    if not img_files:
        print("未找到任何.img文件")
        input("按回车键退出...")
        return
    
    print(f"找到 {len(img_files)} 个.img文件:")
    for i, img_file in enumerate(img_files, 1):
        print(f"{i}. {img_file}")
    
    # 询问用户是否继续
    response = input(f"\n是否开始解压这 {len(img_files)} 个文件? (y/n): ").strip().lower()
    if response != 'y' and response != 'yes':
        print("操作已取消")
        input("按回车键退出...")
        return
    
    print("\n开始解压...")
    print("-" * 50)
    
    # 解压所有文件
    success_count = 0
    failed_files = []
    
    for img_file in img_files:
        success = extract_img_file(img_file)
        if success:
            success_count += 1
        else:
            failed_files.append(os.path.basename(img_file))
        print("-" * 50)
    
    # 显示结果摘要
    print("\n=== 解压完成 ===")
    print(f"成功: {success_count}/{len(img_files)}")
    
    if failed_files:
        print("失败的文件:")
        for file in failed_files:
            print(f"  - {file}")
    
    input("按回车键退出...")

if __name__ == "__main__":
    main()