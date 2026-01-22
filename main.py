from find_perm import find_permissions_in_dir
import sys
import os

def main():
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
    
    perms = ["INJECT_EVENTS", "CAPTURE_VIDEO", "ACCESSIBILITY_SERVICE"]
    find_permissions_in_dir(perms, directory)
    

if __name__ == "__main__":
    main()
