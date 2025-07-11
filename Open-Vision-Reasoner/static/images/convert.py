import os
import subprocess

# 设置你存放 PDF 文件的目录路径
folder_path = 'Open-Vision-Reasoner/static/images'  # 当前目录，也可以换成绝对路径

# 遍历文件夹中所有 PDF 文件
for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(folder_path, filename)
        png_name = filename.replace('.pdf', '.png')
        png_path = os.path.join(folder_path, png_name)

        # 构建 ImageMagick convert 命令
        cmd = [
            'convert',
            '-density', '300',        # 设置清晰度
            pdf_path,
            '-quality', '100',
            png_path
        ]

        print(f"Converting {filename} -> {png_name} ...")
        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error converting {filename}: {e}")