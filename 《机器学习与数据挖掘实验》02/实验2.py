import pandas as pd
import numpy as np
from math import sqrt
import copy
import matplotlib.pyplot as plt
import pickle


#读取txt数据（读取实验一保存的数据）
def readTxt():
    title=['SNO','SNAME','SCITY','SGENDER','SHEIGHT','C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','SCONSTITUTION']
    txtData_set = pd.read_csv('result1.txt',sep=' ',header=None)
    txtData = np.array(txtData_set)
    return txtData,title


def Max_3_fun(S_coefficient,ignore):
    re=[0,0,0]
    rank=[0,0,0]
    index=0
    for i in S_coefficient:
        if ignore==index:
            index += 1
            continue
        for j in range(0, 3):
            if i > re[j]:
                re.insert(j,i)
                rank.insert(j,index)
                break
        index += 1

    return rank[0],rank[1],rank[2]


#实验1用的计算，因为其中有很多数据会用到所以照搬了
def Caculate(txtData,title):
    Snum=0
    total=0
    for i in txtData:
        if i[title.index('SCITY')]=='Beijing':
            Snum+=1
#            if i[1]=='Maxine':
#                print(1)
            for j in range(title.index('C1'),title.index('C9')):
                if True!=np.isnan(i[j]):
                    total+=i[j]
#            if True==np.isnan(total):
#                print(1)
    ans1=total/Snum


    Snum = 0
    Gnum=0
    for i in txtData:
        if i[title.index('SCITY')] == 'Guangzhou' and i[title.index('C1')]>80 and i[title.index('C9')]>=9 and i[title.index('SGENDER')]=='BOY':
            Snum+=1
    ans2=Snum


    G_girl=txtData[txtData[:,title.index('SCITY')]=='Guangzhou',title.index('SCONSTITUTION')]
    S_girl=txtData[txtData[:,title.index('SCITY')]=='Shanghai',title.index('SCONSTITUTION')]
    G_score=0
    S_score=0
    score={'bad':1,'general':2,'good':4,'excellent':8}
    for i in G_girl:
        G_score +=score[i]
        Gnum+=1
    for i in S_girl:
        S_score +=score[i]
        Snum += 1
    if S_score/Snum>G_score/Gnum:
        ans3='Shanghai'
    else:
        ans3='Guangzhou'

    Ax={5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[],13:[]}
    Ax_sum = {5: 0, 6:0,  7:0, 8:0,  9:0,  10:0,  11:0,  12:0,  13:0}
    B_sum = 0
    Bx=[]
    Snum=0
    for i in txtData:
        for x in range(title.index('C1'),title.index('C10')):
            if np.isnan(i[x]) == True:
                i[x]=68
            Ax_sum[x]+=i[x]
            Ax[x].append(i[x])
        if type(i[title.index('SCONSTITUTION')])==str:
            B_sum+=score[i[title.index('SCONSTITUTION')]]
            Bx.append(score[i[title.index('SCONSTITUTION')]])
        else:
            B_sum +=0
            Bx.append(3)
        Snum+=1
#这里对空值的处理是，替换成不计空值成员前的平均值取整（通过excel计算）
#替换后再重新计算平均值和方差等数值



    A_mean= {5: 0, 6:0,  7:0, 8:0,  9:0,  10:0,  11:0,  12:0,  13:0}
    for k in Ax_sum:
        A_mean[k]=(Ax_sum[k]/Snum)
    B_mean =B_sum/Snum

    A_variance={5: 0, 6:0,  7:0, 8:0,  9:0,  10:0,  11:0,  12:0,  13:0}
    B_variance=0

    for i in Ax:
        for j in Ax[i]:
            A_variance[i]+=(j-A_mean[i])**2
        A_variance[i]/=(Snum)

    for i in Bx:
        B_variance+=(i-B_mean)**2
    B_variance/=(Snum)
    coefficient={'C1': 0, 'C2':0,  'C3':0, 'C4':0,  'C5':0,  'C6':0,  'C7':0,  'C8':0,  'C9':0}
    Cx=copy.copy(Ax)
    Cx[14]=Bx
    for i in Ax:
        for z,j in zip(Ax[i],Bx):
            coefficient[title[i]]+=((z-A_mean[i])/sqrt(A_variance[i]))*((j-B_mean)/sqrt(B_variance))

    ans4=coefficient

    return Ax,Bx,Cx,A_mean,B_mean,A_variance,B_variance






def experiment(Ax,Bx,Cx,A_mean,B_mean,A_variance,B_variance):
    Z_Ax = {5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: [], 13: []}
    Z_Bx = []

    # 实验二第1题
    plt.scatter(Ax[5], Bx, marker='o')
    plt.show()

    # 实验二第2题
    bin = [zx * 5 for zx in range(0, 21)]
    plt.hist(x=Ax[5],  # 指定绘图数据
             bins=bin,
             edgecolor='black',  # 指定直方图的边框色
             align='mid',
             )
    plt.show()

    # 实验二第3题
    for i in Ax:
        for j in Ax[i]:
            Z_Ax[i].append((j - A_mean[i]) / sqrt(A_variance[i]))
    for i in Bx:
        Z_Bx.append((i - B_mean) / sqrt(B_variance))
    Z_Ax[14] = Z_Bx
    print()
    orderedNames = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    dataMatrix = np.array([Z_Ax[i] for i in orderedNames])
    print("实验二第3题:",dataMatrix)

    #将本题答案保存一下以供实验三使用
    pickle_file = open('z-scoreData.txt','wb')#必须是wb
    pickle.dump(dataMatrix,pickle_file)
    pickle_file.close()

    # 实验二第4题 相关矩阵
    S_variance = []
    S_mean = []
    for i in range(0, len(Ax[5])):
        Mid = 0
        for j in Cx:
            Mid += Cx[j][i]
        S_mean.append(Mid / 10)
        Mid = 0
        for j in Cx:
            Mid += (Cx[j][i] - S_mean[i]) ** 2
        S_variance.append(Mid)

    s = (len(Ax[5]), len(Ax[5]))
    S_coefficient = np.zeros(s)
    for i in range(0, len(Ax[5])):
        for j in range(0, len(Ax[5])):
            for z in Cx:
                S_coefficient[i][j] += ((Cx[z][i] - S_mean[i]) / sqrt(S_variance[i])) * (
                            (Cx[z][j] - S_mean[j]) / sqrt(S_variance[j]))
    print("实验二第4题:",S_coefficient)

    # 实验二第5题
    s = (len(Ax[5]), 3)
    Max_3 = np.zeros(s)
    for i in range(0, len(Ax[5])):
        Max_3[i][0], Max_3[i][1], Max_3[i][2] = Max_3_fun(S_coefficient[i], i)
    Max_3 = np.array(Max_3)
    np.savetxt('result2.txt', Max_3, fmt='%d', delimiter="\t")
    print("实验二第5题:",Max_3)


def main():
    txtData,title=readTxt()
    Ax,Bx,Cx,A_mean,B_mean,A_variance,B_variance=Caculate(txtData,title)
    experiment(Ax,Bx,Cx,A_mean,B_mean,A_variance,B_variance)

if __name__ == '__main__':
    main()