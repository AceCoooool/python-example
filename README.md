# python-example

> 这里的代码大部分修改自: https://github.com/geekcomputers/Python

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

- [count_characters.py](FILE/count_characters.py) - 统计目标文件里面的各字符数目（比如`a`出现的次数等 ）

  ```shell
  python count_characters.py 目标文件
  ```

  > 注：此处不区分大小写，全部转为大写。但你可以轻易改为区分大小写

- [file_organize.py](FILE/file_organize.py) - 对指定文件夹下面的文件进行"分类"

  ```shell
  # others=True代表将不在类别内的放入Folders文件夹
  python file_organize.py 指定的文件夹 --others=False  
  ```

  > 注：此处只是针对一些特定类型的文件进行了归类，你可以自行添加更多类型

- [file_copy.py](FILE/file_copy.py) - 将源文件夹下面所有内容复制到目标文件夹下面（其实就是备份）

  ```shell
  python file_copy.py 源文件夹 目标文件夹
  ```

  > 注：目标文件夹不允许一开始就存在

- 


## 2. 操作系统相关

- [os_info.py](OS/os_info.py) - 返回当前操作系统的基本信息（主要利用`platform`这个库）

  ```shell
  python os_info.py
  ```

- port_check：TODO

- [check_internet.py](OS/check_internet.py) - 检查系统是否处于联网状态

  ```shell
  python check_internet.py 你可以指定检查的网站
  ```

  > 注：默认采用http://baidu.com作为验证网站

- [check_env.py](OS/check_env.py) - 检查指定文件里面的变量是否存在于环境变量中

  ```shell
  python check_env.py 指定文件
  ```

  > 注：你可以利用`os.environ`来查看所有的环境变量，此处的目标主要是检查自己指定的环境变量是否存在

- 

## 3. 脚本相关

- [script_count.py](SCRIPT/script_count.py) - 统计指定文件夹下面某种类型文件的数量

  ```shell
  python script_count.py 指定文件夹 文件后缀名
  ```

- [script_list.py](SCRIPT/script_list.py) - 将指定文件夹下所有（包括子目录）文件名输出到指定文件下面

  ```shell
  python scripy_list.py 指定文件夹 输出文件  # 输出文件即类似log.txt, 方便记录
  ```

- [script_download.py](SCRIPT/script_download.py) - 批量下载指定网址下面指定后缀的文件到指定目录下面去

  ```shell
  python script_download.py 网址 后缀名 指定目录  # 指定目录指的是保存下载的结果
  ```

- 

## 4. 算法相关

- [decimal_to_binary.py](ALGOS/decimal_to_binary.py) - 将十进制数字(可以为float)转换为二进制

  ```shell
  python decimal_to_binary.py 数字 保留二进制小数位数(默认为7)   
  ```

  > 注：其中**保留二进制小数位数**指的是比如`0.2`转为二进制保留7位就为`.0 0 1 1 0 0 1`（即有7个`0/1`）

- [merge_sort.py](ALGO/merge_sort.py) - 归并排序

  ```shell
  python merge_sort.py 待排序的数组   # 例如 5,2,3,1,4
  ```

  > 注：此处只是为了展示算法，更方便的方式其实可以从文件读取

- [palindrome_check.py](ALGO/palindrome_check.py) - 检查是否为回文字符串

  ```shell
  python palindrome_check.py 待检测的字符串
  ```

  > 注：这里只是demo，处理非常长的字符串可以从文件读取

- [decimal_to_hex.py](ALGO/decimal_to_hex.py) - 十进制转为十六进制（必须为int类型）

  ```shell
  python decimal_to_hex.py 数字
  ```

- [permute_and_combine.py](ALGO/permute_and_combine.py) - 排列组合计算

  ```shell
  python permute_and_combine.py n r --c=False
  ```

  > 注：`--c=True`代表计算$C_n^r$，而`--c=False`代表计算$A_n^r$

- [factors.py](ALGO/factors.py) - 获得某个数的所有因子

  ```shell
  python factors.py 某个正整数
  ```

- [primes.py](ALGO/primes.py) - 获得`[2, num]`之间的所有质数

  ```shell
  python primes.py 某个正整数
  ```

- [kmp.py](ALGO/kmp.py) - 采用kmp算法进行字符串匹配

  ```shell
  python kmp.py 模板字符串 文本字符串
  ```

  > 注：如果文本字符串中包含模板字符串则返回True，否则返回False.  
  >
  > 其实可以进一步改写为返回具体下标

- [text_replace.py](ALGO/text_replace.py) - 将指定字符串里面所有某符号替换为新的某符号

  ```shell
  python text_replace.py 指定字符串 某符号 新符合
  ```

  > 注：这里的符号往往是指分隔符

- [spiral_matrix.py](ALGO/spiral_matrix.py) - 返回`kxk`的螺旋矩阵（从1开始，k为正整数）

  ```shell
  python spiral_matrix.py k
  ```

- [two_sum.py](ALGO/two_sum.py) - 寻找数组中是否存在两数之和为某个值

  ```shell
  python two_sum.py 字符串 某个值
  ```

  > 注：此处数组用字符串表示，比如`[1, 2, 3, 4]`，这里对应字符串就为`'1 2 3 4'`（记得用空格分隔）

## 5. 简单示例（不通用的情况）

- [read_csv.py](DEMO/read_csv.py) - 利用pandas读取csv文件的简单实例

  ```shell
  python read_csv.py
  ```

  > 注：csv文件需要注意各元素之间除分隔符外别添加额外的空格等

- [read_excel.py](DEMO/read_excel.py) - 利用xlrd读取xlsx文件的简单实例

  ```shell
  python read_excel.py 
  ```

- [write_excel.py](DEMO/write_excel.py) - 利用xlwt写excel文件的简单实例

  ```shell
  python write_excel.py
  ```

- [sierpinski_triangle.py](DEMO/sierpinski_triangle.py) - 绘制谢尔宾斯基三角形（可以指定depth）

  ```shell
  python sierpinski_triangle.py depth
  ```

  > 注：上述depth代表任意正整数（这个程序看着玩就好.....）
  >
  > 关于谢尔宾斯基三角形可以参考：[Sierpinski triangle](https://en.wikipedia.org/wiki/Sierpinski_triangle)

- [webcam.py](DEMO/webcam.py) - 摄像头示例

  ```shell
  python webcam.py
  ```

## 6. 图像相关

- 系列1：opencv教程（翻译自：[Gasyori100knock](https://github.com/yoyoyo-yo/Gasyori100knock)）

