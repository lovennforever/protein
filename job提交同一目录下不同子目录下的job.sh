#!/bin/bash

# 设置当前工作目录路径
FREE_ENERGY="."

# 遍历当前目录下的子目录
for dir in "$FREE_ENERGY"/*/; do
  # 进入子目录
  cd "$dir"
  
  # 提交 job.sh
  sbatch job.sh
  
  # 返回上一级目录
  cd ..
done