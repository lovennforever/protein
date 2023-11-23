#!/bin/bash
#SBATCH -J gp              # 作业名是 test
#SBATCH -p defq            # 提交到默认的 defq 队列
#SBATCH -N 2               # 使用2个节点
#SBATCH --ntasks-per-node=10  # 每个节点开启6个进程
#SBATCH --cpus-per-task=1     # 每个进程占用一个 CPU 核心
#SBATCH -t 50000:00        # 任务最大运行时间是 500 分钟
#SBATCH --mem=10G          # 申请10GB内存

# Load Gromacs module
module load cuda11.1/toolkit/11.1.1
module load anaconda
module load lammps/gmx

# Set current working directory path
FREE_ENERGY="."

# Execute `gmx editconf` command
gmx editconf -f 343.pdb -o box.gro -bt dodecahedron -d 1.2 -box 5 5 5

# Execute `gmx solvate` command
gmx solvate -cp box.gro -cs -o solvated.gro -p topol.top -maxsol 600

# Execute `gmx grompp` command for energy minimization
gmx grompp -f em.mdp -c solvated.gro -o em.tpr

# Execute `srun` command for energy minimization
gmx mdrun -v -deffnm em

# Execute `gmx grompp` command for equilibration
gmx grompp -f equil.mdp -c em.gro -o equil.tpr

# Execute `srun` command for equilibration
gmx mdrun -deffnm equil

# Execute `python3` command for lambda settings
python3 lambda.py

# Create lambda directories
for i in 0 1 2 3 4 5 6; do
    LAMBDA=$(printf "%02d" $i)
    mkdir -p "lambda_$LAMBDA"
    cd "lambda_$LAMBDA" || exit
    gmx grompp -f run.mdp -c equil.gro -r equil.gro -p topol.top
    gmx mdrun
    cd ..
done
# Execute `gmx bar` command for free energy calculation
gmx bar -b 100 -f lambda_0?/dhdl.xvg