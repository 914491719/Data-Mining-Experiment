# Data-Mining-Experiment
数据挖掘-实验

#### 实验一 《多源数据集成、清洗和统计》

- **题目** 
广州大学某班有同学100人，现要从两个数据源汇总学生数据。
第一个数据源在数据库中，第二个数据源在txt文件中。
两个数据源课程存在缺失、冗余和不一致性，请用C/C++/Java程序实现对两个数据源的一致性合并以及每个学生样本的数值量化。

- **两个数据源合并内存并统计** 
 
1.	学生中家乡在Beijing的所有课程的平均成绩。
2.	学生中家乡在广州，课程1在80分以上，且课程9在9分以上的男同学的数量。(备注：该处做了修正，课程10数据为空，更改为课程9)
3.	比较广州和上海两地女生的平均体能测试成绩，哪个地区的更强些？
4.	学习成绩和体能测试成绩，两者的相关性是多少？（九门课的成绩分别与体能成绩计算相关性）

- **数据来源** 
data.txt文件存放其中一个数据源，数据库中的数据源通过python提取后放入内存，两者合并后放入result1中。


#### 实验二 《数据统计和可视化》

- **基于实验一中清洗后的数据练习统计和视化操作，100个同学（样本），每个同学有11门课程的成绩（11维的向量）；那么构成了一个100x11的数据矩阵。以你擅长的语言C/C++/Java/Python/Matlab，编程计算：** 
1.	请以课程1成绩为x轴，体能成绩为y轴，画出散点图。
2.	以5分为间隔，画出课程1的成绩直方图。
3.	对每门成绩进行z-score归一化，得到归一化的数据矩阵。
4.	计算出100x100的相关矩阵，并可视化出混淆矩阵。（为避免歧义，这里“协相关矩阵”进一步细化更正为100x100的相关矩阵，100为学生样本数目，视实际情况而定）
5.	根据相关矩阵，找到距离每个样本最近的三个样本，得到100x3的矩阵（每一行为对应三个样本的ID）输出到txt文件中，以\t,\n间隔。


#### 实验三 《k-means聚类算法》

- **题目**
用C++实现k-means聚类算法，
1.	对实验二中的z-score归一化的成绩数据进行测试，观察聚类为2类，3类，4类，5类的结果，观察得出什么结论？

2.	由老师给出测试数据，进行测试，并画出可视化出散点图，类中心，类半径，并分析聚为几类合适。

#### 实验四 《逻辑回归二分类》

- **题目**
学习sigmoid函数和逻辑回归算法。将实验三.2中的样例数据用聚类的结果打标签{0，1}，并用逻辑回归模型拟合。
1.	学习并画出sigmoid函数
2.	设计梯度下降算法，实现逻辑回归模型的学习过程。
3.	根据给定数据（实验三.2），用梯度下降算法进行数据拟合，并用学习好的模型对(2,6)分类。
（对2,3实现有难度的同学，可以直接调用sklearn中LogisticRegression进行学习）


- **组员信息** 
组长：卢学文
组员：卢学文 夏旭 李鸿洋
