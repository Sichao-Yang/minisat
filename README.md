# Done

- simple_sat_python - 这个有个对应的blog可以入手
- SAT-SOLVER-DPLL & SAT-SOLVER-CDCL: 
- - var的正负号也是用2*(v-1)+0/1来encode的. 它的variable的assignment是存在f.literals向量里的，命名上有点奇怪；
- - 且这两个solver里对f.literals的元素（一个var）赋值定义是相反的（cdcl里0代表 !a, 1代表 a; dpll 相反）；
- - CDCL里implement的不是1st ULP，而是更简单的lastULP，也就是它不需要找单个ULP，每次直接对当前decision level的所有implied vars做resolve；
- - 这两个做unit propogate的时候都没用two literals watchlist；


# Understanding [MiniSAT](http://minisat.se/)

该项目存放了一些和sat solver特别是minisat相关的代码和comments。

## Install

1.14版本：

注意: 因为最新版本的minisat做了很多别的优化, 不适合入门阅读, 所以我下载了[MiniSat_v1.14.2006-Aug-29.src.zip)](http://minisat.se/downloads/MiniSat_v1.14.2006-Aug-29.src.zip)来研究, 这个也是最接近1.13 paper的版本. 需要调试的话, 直接用 `make d` 安装.


2.0以上版本:

[github地址](https://github.com/niklasso/minisat) 里的master 分支上直接拉下来，用windows subsystem ubuntu装会失败的。原因是新版本的c++11标准不支持项目代码里的声明方式。

解决方案在这个[issue](https://github.com/niklasso/minisat/issues/16)有讨论，最简单的做法就是拉这个[fork](https://github.com/agurfinkel/minisat)里的版本。
``

## Play

创建文件`tmp.cnf`，输入：

```bash
p cnf 2 3

-1 2 0
1 2 0
-1 -2 0
```

format说明：

line1：p指的是project，cnf指的是编码方式，2指的是有两个变量（1和2），3指的是有三个约束子句。
line2：空格（可选）
line3、line4、line5：负号代表该序号的变量取反，无符号代表该变量取原变量，以0结尾

运行：`minisat tests/tmp.cnf log`