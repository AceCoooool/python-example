# python-example

> 这里的代码全部来自: https://github.com/geekcomputers/Python

## 1. 文件操作相关

- [batch_file_rename.py](FILE/batch_file_rename.py) - 将指定文件夹下面所有后缀名为`old_ext`（比如`txt`）的文件更改后缀名为`new_ext`（比如`png`）

  ```shell
  python batch_file_rename.py 指定文件夹 旧后缀名 新后缀名 
  ```

- [create_dir_if_not_there.py](FILE/create_dir_if_not_there.py) - 如果不存在文件夹则创建

  ```shell
  python create_dir_if_not_there.py 路径
  ```

- [file_info.py](FILE/file_info.py) - 输出指定文件的信息（包含的段落数，文件大小，最后修改时间等等）

  ```
  python file_info.py 指定文件
  ```

- [folder_size.py](FILE/folder_size.py) - 输出指定文件夹下面所有文件的大小之和（注: 不包含子文件夹）

  ```shell
  python folder_size.py 指定文件夹
  ```

- [file_zip.py](FILE/file_zip.py) - 压缩指定文件夹下面后缀名为"指定后缀名"的所有文件

  ```shell
  # 其中的remove代表是否移除这些文件
  python file_zip.py 指定文件夹 指定后缀名 --remove=False
  ```

- [move_files_over_x_days.py](FILE/move_files_over_x_days.py) - 将源文件夹下面超过N天的文件移到目标文件夹下面去

  ```shell
  python move_files_over_x_days.py 源文件夹 目标文件夹 天数
  ```

- 


