import cx_Oracle
import pandas as pd
import numpy as np
from math import sqrt
import copy



# 读取数据库数据
def readDB():
    db_conn = cx_Oracle.connect("cc", "ccpassword", "localhost/OurCourse")
    db_cur = db_conn.cursor()
    result = db_cur.execute("select * from STUDENT")
    return result, db_cur, db_conn


# 读取txt数据
def readTxt():
    txtData_set = pd.read_csv('data.txt', sep=',')
    txtData = np.array(txtData_set)
    return txtData


# 数据单位一致（以数据库为准）
def uniformity(txtData, title):
    for i in range(0, txtData.shape[1]):
        for j in range(0, txtData.shape[0]):
            if i == title.index('SHEIGHT'):
                txtData[j][i] = txtData[j][i] * 100#txt文件里单位是米，换算为cm
            if i == title.index('SNO'):
                txtData[j][i] = txtData[j][i] % 1000#sno只保留后三位
            if i == title.index('SGENDER'):
                if txtData[j][i] == 'male':
                    txtData[j][i] = 'boy'
                if txtData[j][i] == 'female':
                    txtData[j][i] = 'girl'


# 处理数据冗余
def redundancy(txtData_row, title, txtData):
    dataLabel = {}
    i = 0
    while (i < txtData_row):
        if txtData[i][title.index('SNO')] not in dataLabel:
            dataLabel[txtData[i][title.index('SNO')]] = 0
        dataLabel[txtData[i][title.index('SNO')]] += 1
        if dataLabel[txtData[i][title.index('SNO')]] > 1:
            print("出现数据冗余,行数为%d" % (i))
            txtData = np.delete(txtData, i, 0)
            i -= 1
        txtData_row = txtData.shape[0]
        i += 1
    return txtData


# 课程C10随机生成5到10的随机分数
def arr_Column(arr, Cnum):
    size = len(arr)
    arr[:, Cnum] = np.random.randint(5, 10, size)
    return arr


# 数据合并
def complementary(db_cur, txtData_row, title, txtData):
    i: int = 0
    while (i < txtData_row):
        num = i + 1
        if num != txtData[i][title.index('SNO')]:
            # print(num)#从数据库中，按学号提取每一行
            arr = db_cur.execute('select * from STUDENT where SNO = %s and rownum<2' % num)
            testData = []
            for re in arr:
                re = list(re)
                testData.append(re)
            testData = np.array(testData)
            testData = testData.flatten()
            if testData.shape == ():
                # txtData = np.append(txtData,testData, axis=2)
                txtData = np.row_stack((txtData, testData))
        txtData_row = txtData.shape[0]
        i += 1
    #    txtData[txtData[:,1].argsort()]

    i = 0

    dataLabel = {}
#判断是否有重复人
    while (i < txtData_row):
        if txtData[i][title.index('SNO')] not in dataLabel:
            dataLabel[txtData[i][title.index('SNO')]] = 0
        dataLabel[txtData[i][title.index('SNO')]] += 1
#如果有重复的人就删除第二个重复的
        if dataLabel[txtData[i][title.index('SNO')]] > 1:
            txtData = np.delete(txtData, i, 0)
            i -= 1
        txtData_row = txtData.shape[0]
        i += 1

    txtData = txtData[txtData[:, 0].argsort()]

    test = []

    for i in range(txtData.shape[0]):
        for j in range(txtData.shape[1]):
            if pd.isna(txtData[i][j]) or txtData[i][j] == None:
                id = txtData[i][title.index('SNO')]
                res = db_cur.execute("select %s from STUDENT where SNO = %s" % (title[j], id))
                for re in res:
                    re = list(re)
                    if re != None:
                        txtData[i][j] = re[0]
    print(txtData)
    np.savetxt('result1.txt', txtData, fmt='%s')#合并后文件保存为result1
    return txtData

# 回答问题
def Caculate(txtData, title):
    # 1.	学生中家乡在Beijing的所有课程的平均成绩。
    # 2.	学生中家乡在广州，课程1在80分以上，且课程9在9分以上的男同学的数量。
    # 3.	比较广州和上海两地女生的平均体能测试成绩，哪个地区的更强些？
    # 4.	每门学习成绩和体能测试成绩，两者的相关性是多少？
    Snum = 0
    total = 0
    for i in txtData:
        if i[title.index('SCITY')] == 'Beijing':
            Snum += 1
            #            if i[1]=='Maxine':
            #                print(1)
            for j in range(title.index('C1'), title.index('C9')):
                if True != np.isnan(i[j]):
                    total += i[j]
    #            if True==np.isnan(total):
    #                print(1)
    ans1 = total / Snum

    Snum = 0
    Gnum = 0
    for i in txtData:
        if i[title.index('SCITY')] == 'Guangzhou' and i[title.index('C1')] > 80 and i[title.index('C9')] >= 9 and i[
            title.index('SGENDER')] == 'BOY':
            Snum += 1
    ans2 = Snum

    G_girl = txtData[txtData[:, title.index('SCITY')] == 'Guangzhou', title.index('SCONSTITUTION')]
    S_girl = txtData[txtData[:, title.index('SCITY')] == 'Shanghai', title.index('SCONSTITUTION')]
    G_score = 0
    S_score = 0
    score = {'bad': 1, 'general': 2, 'good': 4, 'excellent': 8}
    for i in G_girl:
        G_score += score[i]
        Gnum += 1
    for i in S_girl:
        S_score += score[i]
        Snum += 1
    if S_score / Snum > G_score / Gnum:
        ans3 = 'Shanghai'
    else:
        ans3 = 'Guangzhou'

    Ax = {5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: [], 13: [], 14: []}
    Ax_sum = {5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}
    B_sum = 0
    Bx = []
    Snum = 0
    for i in txtData:
        for x in range(title.index('C1'), title.index('C10') + 1):
            if np.isnan(i[x]) == True:
                i[x] = 68
            Ax_sum[x] += i[x]
            Ax[x].append(i[x])
        if type(i[title.index('SCONSTITUTION')]) == str:
            B_sum += score[i[title.index('SCONSTITUTION')]]
            Bx.append(score[i[title.index('SCONSTITUTION')]])
        else:
            B_sum += 0
            Bx.append(3)
        Snum += 1
    # 这里对空值的处理是，替换成不计空值成员前的平均值取整（通过excel计算）
    # 替换后再重新计算平均值和方差等数值

    A_mean = {5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}
    for k in Ax_sum:
        A_mean[k] = (Ax_sum[k] / Snum)
    B_mean = B_sum / Snum

    A_variance = {5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}
    B_variance = 0

    for i in Ax:
        for j in Ax[i]:
            A_variance[i] += (j - A_mean[i]) ** 2
        A_variance[i] /= (Snum)

    for i in Bx:
        B_variance += (i - B_mean) ** 2
    B_variance /= (Snum)
    coefficient = {'C1': 0, 'C2': 0, 'C3': 0, 'C4': 0, 'C5': 0, 'C6': 0, 'C7': 0, 'C8': 0, 'C9': 0, 'C10': 0}
    Cx = copy.copy(Ax)
    Cx[15] = Bx
    for i in Ax:
        for z, j in zip(Ax[i], Bx):
            coefficient[title[i]] += ((z - A_mean[i]) / sqrt(A_variance[i])) * ((j - B_mean) / sqrt(B_variance))

    ans4 = coefficient
    print('问题1：', ans1, '\n'
                        '问题2: ', ans2, '\n'
                                       '问题3：', ans3, '\n'
                                                     '问题4：', ans4, '\n')


def main():
    result,db_cur,db_conn=readDB()#调用数据库并保存
    title = [i[0] for i in db_cur.description]#以数据库为准保存表头
    print(title)
    txtData=readTxt()#调用txt并保存
    uniformity(txtData,title)#维持txt的数据一致性
    txtData_row = txtData.shape[0]
    txtData=arr_Column(txtData,title.index('C10'))
    txtData=redundancy(txtData_row,title,txtData)
    txtData=complementary(db_cur, txtData_row, title,txtData)
    Caculate(txtData,title)
    db_cur.close()
    db_conn.close()

if __name__ == '__main__':
    main()