#!/usr/bin/env python3
"""
TXT文件字母转大写工具

功能：读取txt文件，将文件内容中的所有字母转为大写，并另存为新文件

使用方法：
python txt_to_uppercase.py input.txt [output.txt]

参数说明：
- input.txt: 输入文件路径（必需）
- output.txt: 输出文件路径（可选，默认为 input_uppercase.txt）
"""

import sys
import os


def convert_to_uppercase(input_file, output_file=None):
    """
    将txt文件内容转为大写并保存
    
    Args:
        input_file (str): 输入文件路径
        output_file (str): 输出文件路径，如果为None则自动生成
    
    Returns:
        bool: 转换是否成功
    """
    try:
        # 检查输入文件是否存在
        if not os.path.exists(input_file):
            print(f"错误：输入文件 '{input_file}' 不存在")
            return False
        
        # 如果未指定输出文件，自动生成文件名
        if output_file is None:
            base_name = os.path.splitext(input_file)[0]
            output_file = f"{base_name}_uppercase.txt"
        
        # 读取输入文件
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 将内容转为大写
        uppercase_content = content.upper()
        
        # 写入输出文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(uppercase_content)
        
        print(f"成功将文件 '{input_file}' 转为大写并保存为 '{output_file}'")
        print(f"原始文件大小: {len(content)} 字符")
        print(f"转换后文件大小: {len(uppercase_content)} 字符")
        
        return True
        
    except Exception as e:
        print(f"转换过程中发生错误: {e}")
        return False


def main():
    """主函数"""
    # 检查命令行参数
    if len(sys.argv) < 2:
        print("用法: python txt_to_uppercase.py input.txt [output.txt]")
        print("\n示例:")
        print("  python txt_to_uppercase.py demo.txt")
        print("  python txt_to_uppercase.py demo.txt result.txt")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    # 执行转换
    success = convert_to_uppercase(input_file, output_file)
    
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()