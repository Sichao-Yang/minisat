# Done

- simple_sat_python
- SAT-SOLVER-DPLL: 它的literal的正负号也是用2*l+0/1来encode的.
- SAT-SOLVER-CDCL: 它的variable就是encode后的literal. 和上面的initializaiton不太一样.


# Understanding [MiniSAT](http://minisat.se/)

入门可以先看下CMU大佬[marijn heule](https://www.cs.cmu.edu/~mheule/)写的[microsat](https://github.com/marijnheule/microsat), 然后来看minisat.

minisat相关paper和slides在我zotero的 `09_Formal_methods\SAT\Minisat` 目录下, 该项目里的doc主要是存放一些笔记.

## Install

两种方法：

### 自己make


注意: 因为最新版本的minisat做了很多别的优化, 不适合入门阅读, 所以我下载了[MiniSat_v1.14.2006-Aug-29.src.zip)](http://minisat.se/downloads/MiniSat_v1.14.2006-Aug-29.src.zip)来研究, 这个也是最接近1.13 paper的版本. 需要调试的话, 直接用 `make d` 安装.


2.0以上版本:

[github地址](https://github.com/niklasso/minisat) 里的master 分支上直接拉下来，用windows subsystem ubuntu装会失败的。原因是新版本的c++11标准不支持项目代码里的某种声明方式。

解决方案在这个[issue](https://github.com/niklasso/minisat/issues/16)有讨论，最简单的做法就是拉这个[fork](https://github.com/agurfinkel/minisat)里的版本。
``



### 系统安装

直接 `apt install minisat`就行。

## Play

创建文件`tmp.cnf`，输入：

```bash
p cnf 2 3

-1 2 0
1 2 0
-1 -2 0
```

line1：p指的是project，cnf指的是cnf编码，2指的是有两个变量（1和2），3指的是有三个约束子句。
line2：空格（可选）
line3、line4、line5：负号代表该序号的变量取反，无符号代表该变量取原变量，以0结尾

运行：`minisat tmp.cnf log`

## PythonAPI

https://pysathq.github.io/ 这个项目，封装了一层python API，可以调用很多经典的SAT solver。可以用作看完minisat后的后续学习材料。[paper地址](https://alexeyignatiev.github.io/assets/pdf/imms-sat18-preprint.pdf)
