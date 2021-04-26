import re
import math
import numpy as np
from collections import Counter


train_data = []
for line in open("train.txt","r"):
    train_data.append(line)


test_data = []
for line in open("test.txt","r"):
    test_data.append(line)


notdga_len = np.zeros(500); dga_len = np.zeros(432);
notdga_num = np.zeros(500);  dga_num = np.zeros(432);
notdga_entropy = np.zeros(500);  dga_entropy = np.zeros(432);



# 计算域名长度
def domain_length(domain):
    domain = domain.split('.')[0]
    length = len(domain)
    return length


# 计算域名中的数字个数
def domain_number(domain):
    domain = domain.split('.')[0]
    pattern = re.compile('[0-9]+')
    numlist = pattern.findall(domain)
    if numlist :
        number = len(numlist[0])
        return number
    else:
        return 0


# 计算域名的熵
def domain_entropy(domain):
    domain = domain.split('.')[0]
    d_len = len(domain)
    count = Counter(i for i in domain).most_common()
    entropy = -sum(j / d_len * (math.log(j / d_len)) for i, j in count)
    return entropy


# 存储各属性
def domain_feat():
    for i in range(0,len(train_data)):
        domain = train_data[i].split(',')[0].split('.')[0]
        if train_data[i].split(',')[1].strip() == 'notdga':
            notdga_len[i] = domain_length(domain)
            notdga_num[i] = domain_number(domain)
            notdga_entropy[i] = domain_entropy(domain)
        else:
            dga_len[i-500] = domain_length(domain)
            dga_num[i-500] = domain_number(domain)
            dga_entropy[i-500] = domain_entropy(domain)



if __name__=="__main__":
    fw = open('result.txt', 'w')
    domain_feat()
    notdga_len_max = max(notdga_len)
    notdga_len_min = min(notdga_len)
    notdga_num_max = max(notdga_num)
    notdga_num_min = min(notdga_num)
    notdga_entropy_max = max(notdga_entropy)
    notdga_entropy_min = min(notdga_entropy)
    dga_len_max = max(dga_len)
    dga_len_min = min(dga_len)
    dga_num_max = max(dga_num)
    dga_num_min = min(dga_num)
    dga_entropy_max = max(dga_entropy)
    dga_entropy_min = min(dga_entropy)

  
    sum_notdgalen = 0
    sum_notdganum = 0
    sum_notdgaentropy = 0
    for i in range(0,len(notdga_len)):
        sum_notdgalen += notdga_len[i]
        sum_notdganum += notdga_num[i]
        sum_notdgaentropy += notdga_entropy[i]
    aver_notdgalen = sum_notdgalen / len(notdga_len)
    aver_notdganum = sum_notdganum / len(notdga_num)
    aver_notdgaentropy = sum_notdgaentropy / len(notdga_entropy)

    sum_dgalen = 0
    sum_dganum = 0
    sum_dgaentropy = 0
    for i in range(0, len(dga_len)):
        sum_dgalen += dga_len[i]
        sum_dganum += dga_num[i]
        sum_dgaentropy += dga_entropy[i]
    aver_dgalen = sum_dgalen / len(dga_len)
    aver_dganum = sum_dganum / len(dga_num)
    aver_dgaentropy = sum_dgaentropy / len(dga_entropy)

    numof_notdga = 0
    for i in range(0,len(test_data)):
        domain = test_data[i].split('.')[0]
        test_len = domain_length(domain)
        test_num = domain_number(domain)
        test_entropy = domain_entropy(domain)
        if (test_len <= notdga_len_max) and (test_len >= notdga_len_min):
            fw.write(test_data[i].strip()+',notdga\n')
        else:
            fw.write(test_data[i].strip()+',dga\n')
