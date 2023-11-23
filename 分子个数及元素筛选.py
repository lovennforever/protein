#!/usr/bin/env python
# coding: utf-8

# In[13]:


import os

input_dir = r'D:\dsgdb9nsd.xyz\dsgdb9nsd.xyz'  # 输入目录
output_dir = r'D:\dsgdb9nsd_new.xyz'  # 输出目录

# 创建输出目录
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

atom_counts = {'C': 0, 'H': 0, 'O': 0, 'N': 0}  # 统计元素出现次数的字典

def process_file(file_path):
    with open(file_path, 'r') as file:
        # 读取第一行数据
        first_line = file.readline().strip()

        # 提取数值
        values = [float(x) for x in first_line.split() if x.isdigit()]

        # 判断数值是否在20到30之间
        if len(values) > 0 and 20 <= values[0] <= 30:
            output_file_path = os.path.join(output_dir, os.path.basename(file_path))
            with open(output_file_path, 'w') as output_file:
                output_file.write(first_line + '\n')
                for line in file:
                    output_file.write(line)
                print(f'文件 {output_file_path} 保存完成')
                    
            for line in open(output_file_path, 'r'):
                line = line.strip().split()
                if len(line) > 0 and line[0] in atom_counts:
                    atom_counts[line[0]] += 1

# 遍历输入目录下的所有.xyz文件
for file_name in os.listdir(input_dir):
    if file_name.endswith('.xyz'):
        file_path = os.path.join(input_dir, file_name)
        process_file(file_path)

# 生成输出文件路径
output_count_file_path = os.path.join(output_dir, 'atom_counts.txt')

# 保存统计结果到输出文件
with open(output_count_file_path, 'w') as output_count_file:
    for atom, count in atom_counts.items():
        output_count_file.write(f'{atom}: {count}\n')

print('处理完成！')


# In[17]:


import os
import random
import shutil
input_dir = r'D:\dsgdb9nsd_new.xyz'  # 输入目录
output_dir = r'D:\dsgdb9nsd_1000.xyz'  # 输出目录

# 创建输出目录
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

file_list = [file for file in os.listdir(input_dir) if file.endswith('.xyz')]
random_files = random.sample(file_list, 1000)  # 从文件列表中随机选择 1000 个文件

for file_name in random_files:
    file_path = os.path.join(input_dir, file_name)
    output_file_path = os.path.join(output_dir, file_name)
    shutil.copyfile(file_path, output_file_path)
    print(f'文件 {output_file_path} 保存完成')

print('处理完成！')


# In[40]:


import os
import random
import shutil

def count_atoms(filepath):
    """读取文件并统计关键字出现的次数之和"""
    total_count = 0
    
    with open(filepath) as f:
        for line in f:
            atom = line.split()[0]
            if atom in ['C', 'H', 'O', 'N']:
                total_count += 1

    return total_count

if __name__ == '__main__':
    directory = r'D:\dsgdb9nsd.xyz'
    output_directory = r'D:\1000.xyz'

    # 创建保存结果的目录
    os.makedirs(output_directory, exist_ok=True)

    # 遍历目录下所有的 .xyz 文件
    files = [f for f in os.listdir(directory) if f.endswith('.xyz')]

    selected_files = []

    for filename in files:
        # 读取文件
        filepath = os.path.join(directory, filename)
        total_count = count_atoms(filepath)

        # 检查出现次数之和是否在20到30之间
        if 20 <= total_count <= 30:
            selected_files.append(filepath)

    # 如果筛选的文件数量超过1000个，随机选择1000个文件
    if len(selected_files) > 1000:
        selected_files = random.sample(selected_files, 1000)

    # 将符合条件的文件复制到输出目录
    for i, filepath in enumerate(selected_files):
        output_filepath = os.path.join(output_directory, f'{i+1}.xyz')
        shutil.copy(filepath, output_filepath)

    print('筛选完成！')


# In[41]:


import os
import random
import shutil

def count_atoms(filepath):
    """读取文件并统计关键字出现的次数之和"""
    total_count = 0
    
    with open(filepath) as f:
        for line in f:
            atom = line.split()[0]
            if atom in ['C', 'H', 'O', 'N']:
                total_count += 1

    return total_count

if __name__ == '__main__':
    directory = r'D:\dsgdb9nsd.xyz'
    output_directory = r'D:\1000_new.xyz'

    # 创建保存结果的目录
    os.makedirs(output_directory, exist_ok=True)

    # 遍历目录下所有的 .xyz 文件
    files = [f for f in os.listdir(directory) if f.endswith('.xyz')]

    selected_files = []

    for filename in files:
        # 读取文件
        filepath = os.path.join(directory, filename)
        total_count = count_atoms(filepath)

        # 检查出现次数之和是否在20到30之间
        if 20 <= total_count <= 30:
            selected_files.append(filepath)

    # 如果筛选的文件数量超过1000个，随机选择1000个文件
    if len(selected_files) > 1000:
        selected_files = random.sample(selected_files, 1000)

    # 将符合条件的文件复制到输出目录（保持原有文件名不变）
    for filepath in selected_files:
        output_filepath = os.path.join(output_directory, os.path.basename(filepath))
        shutil.copy(filepath, output_filepath)

    print('筛选完成！')


# In[ ]:




