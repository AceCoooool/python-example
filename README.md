# python-example

> 这里的代码全部来自: https://github.com/geekcomputers/Python

## 1. 文件操作相关

- [file_rename.py](FILE/file_rename.py) - 将指定文件夹下面所有后缀名为`old_ext`（比如`txt`）的文件更改后缀名为`new_ext`（比如`png`）

  ```shell
  python file_rename.py 指定文件夹 旧后缀名 新后缀名 
  ```

- [create_dir.py](FILE/create_dir.py) - 如果不存在文件夹则创建

  ```shell
  python create_dir.py 路径
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

- [file_merge.py](FILE/file_merge.py) - 将指定文件夹下面指定后缀名的所有文件合并到一起

  ```shell
  python file_merge.py 指定文件夹 目标文件 指定后缀名
  ```

  > 注：此处合并没有考虑文件的相对顺序，其实你很容易改为处理批量文件合并



## 2. 操作系统相关

- [os_info.py](OS/os_info.py) - 返回当前操作系统的基本信息（主要利用`platform`这个库）

  ```shell
  python os_info.py
  ```

- port_check：TODO

## 3. 脚本相关

- [script_count.py](SCRIPT/script_count.py) - 统计指定文件夹下面某种类型文件的数量

  ```shell
  python script_count.py 指定文件夹 文件后缀名
  ```

- [script_list.py](SCRIPT/script_list.py) - 将指定文件夹下所有（包括子目录）文件名输出到指定文件下面

  ```shell
  python scripy_list.py 指定文件夹 输出文件  # 输出文件即类似log.txt, 方便记录
  ```
