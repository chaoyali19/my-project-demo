# TXT文件字母转大写工具

这是一个用Python编写的工具，用于将TXT文件中的所有字母转换为大写并另存为新文件。

## 功能特性

- 支持读取任意TXT文件
- 将文件内容中的所有字母转换为大写
- 支持指定输出文件名或自动生成
- 具有错误处理和参数验证

## 安装使用

1. 确保系统中已安装Python 3.x
2. 下载脚本文件 `txt_to_uppercase.py`

## 使用方法

### 基本用法

```bash
python txt_to_uppercase.py 输入文件.txt
```

### 指定输出文件名

```bash
python txt_to_uppercase.py 输入文件.txt 输出文件.txt
```

## 示例

假设有一个文件 `demo.txt`，内容为：

```
Hello World!
This is a test file.
123 numbers and special characters: @#$%
```

运行命令：

```bash
python txt_to_uppercase.py demo.txt
```

将会生成文件 `demo_uppercase.txt`，内容为：

```
HELLO WORLD!
THIS IS A TEST FILE.
123 NUMBERS AND SPECIAL CHARACTERS: @#$%
```

## 脚本说明

- 支持UTF-8编码
- 保留数字和特殊字符
- 自动处理文件不存在等异常情况
- 输出文件默认名格式为 `原文件名_uppercase.txt`

## 版本信息

- 版本: 1.0
- 语言: Python 3.x
- 作者: chaoyali19