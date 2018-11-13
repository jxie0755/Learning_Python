# Q2
s = 1
def to(s):
    ix = s[1:2]     # [4]
    ward[1] = 6     # ward = [3, 6, 5]
    def re(st):
        if st is not ward:    # ward is ward, skip this
            nonlocal s
            s = s.extend(ix)
            return re(ward)
        else:                 # execute this
            st.append(ix)     # ward.append([4,5])
    return re

ward = [3, 4] + list([5])
# [3, 4, 5]
print(to(ward)(s))  # 注意to(ward) return 函数re, 而re(s)这里调用的s是global的s,不是to(s)那个s, 也就是不是ward
# re(1)
# ward = ward.extend([4]) = [3,6,5,4]
# re(ward)
# ward.append(ix), ward = [3,6,5,4,[4]]
print(ward)
# >>>
# [3, 6, 5, 4, [4]]
