import os
import sys
import argparse
from pathlib import Path

def find_lines_with_keywords(file_path, keywords):
    """
    读取文件并查找包含所有关键字的行
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                line = line.rstrip('\n')  # 移除行尾换行符
                # 检查该行是否包含所有关键字
                if all(keyword in line for keyword in keywords):
                    print(f"{file_path}:{line_num}: {line}")
    except UnicodeDecodeError:
        # 如果utf-8编码失败，尝试其他编码
        try:
            with open(file_path, 'r', encoding='gbk') as file:
                for line_num, line in enumerate(file, 1):
                    line = line.rstrip('\n')
                    if all(keyword in line for keyword in keywords):
                        print(f"{file_path}:{line_num}: {line}")
        except Exception as e:
            print(f"警告: 无法读取文件 {file_path} (编码问题): {e}", file=sys.stderr)
    except Exception as e:
        print(f"警告: 读取文件 {file_path} 时出错: {e}", file=sys.stderr)

def search_files(directory, keywords):
    """
    递归遍历目录，查找所有.txt文件
    """
    if not os.path.exists(directory):
        print(f"错误: 路径 '{directory}' 不存在", file=sys.stderr)
        return
    
    if not keywords:
        print("错误: 未提供关键字", file=sys.stderr)
        return
    
    # 将路径转换为绝对路径
    directory = os.path.abspath(directory)
    
    print(f"正在搜索路径: {directory}")
    print(f"关键字: {', '.join(keywords)}")
    print("-" * 50)
    
    found_files = 0
    found_lines = 0
    
    # 使用pathlib递归遍历目录
    for file_path in Path(directory).rglob("*.txt"):
        found_files += 1
        lines_found_in_file = 0
        
        # 统计文件中的匹配行数
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    if all(keyword in line for keyword in keywords):
                        lines_found_in_file += 1
        except:
            pass
        
        if lines_found_in_file > 0:
            found_lines += lines_found_in_file
            print(f"\n在文件 {file_path} 中找到 {lines_found_in_file} 个匹配行:")
            # 实际打印匹配的行
            find_lines_with_keywords(file_path, keywords)
    
    print("-" * 50)
    print(f"搜索完成!")
    print(f"扫描了 {found_files} 个.txt文件")
    print(f"总共找到 {found_lines} 个匹配行")

def main():
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='在文本文件中搜索包含所有关键字的行')
    parser.add_argument('path', help='要搜索的目录或文件路径')
    parser.add_argument('keywords', nargs='+', help='要搜索的关键字（一个或多个）')
    
    # 解析命令行参数
    args = parser.parse_args()
    
    # 开始搜索
    search_files(args.path, args.keywords)

if __name__ == "__main__":
    # 如果没有命令行参数，使用交互模式
    if len(sys.argv) > 1:
        main()
    else:
        print("文本文件关键字搜索工具")
        print("=" * 50)
        
        # 获取用户输入
        path = input("请输入要搜索的路径: ").strip()
        
        if not path:
            print("错误: 必须提供路径", file=sys.stderr)
            sys.exit(1)
            
        keywords_input = input("请输入要搜索的关键字(用空格分隔多个关键字): ").strip()
        
        if not keywords_input:
            print("错误: 必须提供至少一个关键字", file=sys.stderr)
            sys.exit(1)
            
        keywords = keywords_input.split()
        
        # 开始搜索
        search_files(path, keywords)