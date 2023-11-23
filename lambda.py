import os
import shutil
import sys

run_mdp_template = "run_mdp.mdp"
output_files = '.'

def write_mdp(mdp_content, mdp_filename, output_directory):
    with open(os.path.join(output_directory, mdp_filename), 'w') as f:
        f.write(mdp_content)

# 读取模板文件内容
with open(run_mdp_template, 'r') as f:
    mdp_template_content = f.read()

#lambda_value = [0.0, 0.2, 0.4, 0.6, 0.8, 0.9, 1.0]
lambda_values = [0,1,2,3,4,5,6]

if len(sys.argv) > 1 and sys.argv[1] == '-d':
    if len(sys.argv) > 2:
        output_files = os.path.join(output_files, sys.argv[2])

for lambda_value in lambda_values:
    lambda_number = str(lambda_value)  # 将小数点替换为下划线
    lambda_directory = os.path.join(output_files, f'lambda_0{lambda_number}')

    if not os.path.exists(lambda_directory):
        os.mkdir(lambda_directory)

    gro_file = os.path.join(output_files, 'equil.gro')
    top_file = os.path.join(output_files, 'topol.top')

    shutil.copy(gro_file, os.path.join(lambda_directory, 'equil.gro'))
    shutil.copy(top_file, lambda_directory)

    mdp_content = mdp_template_content.format(lambda_value)

    # 写入替换后的内容到新的mdp文件中
    write_mdp(mdp_content, 'run.mdp', lambda_directory)