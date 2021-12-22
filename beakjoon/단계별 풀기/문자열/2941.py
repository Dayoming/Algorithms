# 크로아티아 알파벳

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

seq = input()
seq_cnt = len(seq)

for i in croatia:
    if i in seq:
        temp = seq.count(i)
        seq_cnt = seq_cnt - temp

print(seq_cnt)