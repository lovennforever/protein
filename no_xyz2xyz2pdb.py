#单个.xyz转成标准的.xyz
def convert_to_xyz(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()
# 保存第二行内容
    second_line = lines[1].strip()
    # 删除第一行
    lines = lines[1:]

    # 提取原子坐标信息，跳过包含数字的行
    atom_coords = []
    for line in lines:
        line = line.strip().split('\t')
        if len(line) >= 4 and not any(char.isdigit() for char in line[0]):
            atom_coords.append([line[0]] + [float(coord) for coord in line[1:4]])

    with open(output_file_path, 'w') as output_file:
        # 写入原子数
        num_atoms = len(atom_coords)
        output_file.write(str(num_atoms) + '\n')
 # 写入第二行内容
        output_file.write(second_line + '\n')

        # 写入原子标识符和坐标
        for atom in atom_coords:
            output_file.write(f'{atom[0]:2s}\t{atom[1]:14.10f}\t{atom[2]:14.10f}\t{atom[3]:14.10f}\n')

    print(f'Successfully converted {input_file_path} to {output_file_path}.')

input_file_path = r"E:\protein\mole\1000\1000.xyz\916.xyz"
output_file_path = r"E:\protein\mole\1000\new.xyz\916.xyz"

convert_to_xyz(input_file_path, output_file_path)



#目录下的所有.xyz转成标准的.xyz
import os

def process_xyz_files(input_dir, output_dir):
    # 获取输入目录下的所有.xyz文件
    file_list = [file_name for file_name in os.listdir(input_dir) if file_name.endswith(".xyz")]

    for file_name in file_list:
        input_file_path = os.path.join(input_dir, file_name)
        output_file_path = os.path.join(output_dir, file_name)

        convert_to_xyz(input_file_path, output_file_path)

input_dir = r"E:\protein\mole\1000\1000.xyz"
output_dir = r"E:\protein\mole\1000\new.xyz"

process_xyz_files(input_dir, output_dir)



#目录下的所有.xyz转成标准的.xyz
import os

def process_xyz_files(input_dir, output_dir):
    # 获取输入目录下的所有.xyz文件
    file_list = [file_name for file_name in os.listdir(input_dir) if file_name.endswith(".xyz")]

    for file_name in file_list:
        input_file_path = os.path.join(input_dir, file_name)
        output_file_path = os.path.join(output_dir, file_name)

        convert_to_xyz(input_file_path, output_file_path)

input_dir = r"E:\protein\mole\1000\1000.xyz"
output_dir = r"E:\protein\mole\1000\new.xyz"

process_xyz_files(input_dir, output_dir)



#目录下所有.xyz文件转化为.pdb文件
import os
from openbabel import openbabel as ob

def convert_xyz_to_pdb(xyz_file, pdb_file):
    conv = ob.OBConversion()
    conv.SetInFormat('xyz')
    conv.SetOutFormat('pdb')
    mol = ob.OBMol()
    conv.ReadFile(mol, xyz_file)
    conv.WriteFile(mol, pdb_file)

def convert_all_xyz_to_pdb(input_dir, output_dir):
    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 处理输入目录下的所有.xyz文件
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.xyz'):
                xyz_file = os.path.join(root, file)
                pdb_file = os.path.join(output_dir, f"{os.path.splitext(file)[0]}.pdb")
                convert_xyz_to_pdb(xyz_file, pdb_file)

# 调用示例
input_dir = r"E:\protein\mole\1000\1000.xyz"
output_dir = r"E:\protein\mole\1000\new_pbd"
convert_all_xyz_to_pdb(input_dir, output_dir)