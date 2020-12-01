# Data-Mining-Experiment
数据挖掘-实验

#### 实验一 《多源数据集成、清洗和统计》

_ **题目**
广州大学某班有同学100人，现要从两个数据源汇总学生数据。
第一个数据源在数据库中，第二个数据源在txt文件中。
两个数据源课程存在缺失、冗余和不一致性，请用C/C++/Java程序实现对两个数据源的一致性合并以及每个学生样本的数值量化。
	数据库表：ID (int),  姓名(string), 家乡(string:限定为Beijing / Guangzhou / Shenzhen / Shanghai), 性别（string:boy/girl）、身高（float:单位是cm)）、课程1成绩（float）、课程2成绩（float）、...、课程10成绩(float)、体能测试成绩（string：bad/general/good/excellent）；其中课程1-课程5为百分制，课程6-课程10为十分制。
	txt文件：ID(string：6位学号)，性别（string:male/female）、身高（string:单位是m)）、课程1成绩（string）、课程2成绩（string）、...、课程10成绩(string)、体能测试成绩（string：差/一般/良好/优秀）；其中课程1-课程5为百分制，课程6-课程10为十分制。

_ **参考**
数据库中Stu表数据
ID	Name	City	Gender	Height	C1	...	C10	Constitution
1	Sun	Beijing	boy	160	87		9	good
2	Zhu	Shenzhen	girl	177	66		8	excellent
...	...	...	...	...	...	...	...	...
student.txt中
 
ID		Name	City		Gender	Height    C1	。。。	C10	        Constitution
202001 Sun  Beijing male  180       87 。。。 9  good
202003  Tang  Hanghai male  156       91 。。。 10         general
...  ...  ...  ..  ... ..  ...  ...  ...

_ **两个数据源合并后读入内存，并统计：**
 
1.	学生中家乡在Beijing的所有课程的平均成绩。
2.	学生中家乡在广州，课程1在80分以上，且课程9在9分以上的男同学的数量。(备注：该处做了修正，课程10数据为空，更改为课程9)
3.	比较广州和上海两地女生的平均体能测试成绩，哪个地区的更强些？
4.	学习成绩和体能测试成绩，两者的相关性是多少？（九门课的成绩分别与体能成绩计算相关性）

_ **提示**
参考数据结构：
Student{
int id;
string id;
vector<float> data;
}
可能用到的公式：
均值公式	 
协方差公式	 
z-score规范化	 
数组A和数组B的相关性	 
这里A=[a1, a2,...ak,..., an],
B=[b1, b2,...bk,..., bn],
mean(A)代表A中元素的平均值
std是标准差，即对协方差的开平方。
点乘的定义： 
 
注意：计算部分不能调用库函数；画图/可视化显示可以用可视化API或工具实现。





# 小组成员
组长：卢学文
组员：卢学文 夏旭 李鸿洋
