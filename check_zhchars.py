import re
import sys
from typing import List, Tuple

from file_oper import append_line_to_file

def is_chinese_char(char: str) -> bool:
    """判断字符是否为中文字符"""
    # 匹配中文字符的正则表达式（包括中文标点）
    return bool(re.match(r'[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]', char))

def find_chinese_positions(text: str) -> List[int]:
    """找到所有中文字符的位置"""
    positions = []
    for i, char in enumerate(text):
        if is_chinese_char(char):
            positions.append(i)
    return positions

def merge_intervals(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """合并重叠的区间"""
    if not intervals:
        return []
    
    # 按起始位置排序
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        # 如果当前区间与最后一个区间重叠或相邻，则合并
        if current[0] <= last[1]:
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)
    
    return merged

def extract_text_segments(text: str, window_size: int = 50) -> List[str]:
    """提取包含中文字符的文本段"""
    # 找到所有中文字符位置
    chinese_positions = find_chinese_positions(text)
    
    if not chinese_positions:
        return []
    
    # 为每个中文字符创建区间
    intervals = []
    for pos in chinese_positions:
        start = max(0, pos - window_size)
        end = min(len(text), pos + window_size + 1)  # +1 因为切片不包含结束位置
        intervals.append((start, end))
    
    # 合并重叠区间
    merged_intervals = merge_intervals(intervals)
    
    # 提取文本段
    segments = []
    for start, end in merged_intervals:
        segments.append(text[start:end])
    
    return segments

def process_file(file_path: str, encoding: str = 'utf-8') -> None:
    """处理文件并输出结果"""
    try:
        with open(file_path, 'r', encoding=encoding, errors='ignore') as file:
            text = file.read()
    except UnicodeDecodeError:
        # 如果utf-8失败，尝试其他编码
        try:
            with open(file_path, 'r', encoding='gbk', errors='ignore') as file:
                text = file.read()
        except Exception as e:
            print(f"无法读取文件: {e}")
            return
    
    segments = extract_text_segments(text)
    
    if not segments:
        print("文件中未找到中文字符。")
        return
    
    print(f"在文件 '{file_path}' 中找到 {len(segments)} 个包含中文字符的片段:")
    print("=" * 80)
    
    for i, segment in enumerate(segments, 1):
        append_line_to_file("zh_1229.txt", f"\n片段 {i}:")
        append_line_to_file("zh_1229.txt", "-" * 60)
        append_line_to_file("zh_1229.txt", segment)
        append_line_to_file("zh_1229.txt", "-" * 60)

def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("使用方法: python check_zhchars.py <文件路径> [编码格式]")
        print("示例: python check_zhchars.py input.txt utf-8")
        sys.exit(1)
    
    file_path = sys.argv[1]
    encoding = sys.argv[2] if len(sys.argv) > 2 else 'utf-8'
    
    process_file(file_path, encoding)

if __name__ == "__main__":
    main()
