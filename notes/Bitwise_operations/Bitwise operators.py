# ~ (turns all of 0 to 1 and all of 1 to 0) like ! in bool
# 5  0101 => ~5 1010

# for other two imagine 0 as False and 1 as True

# | (like 'or', '||')
# 0 | 0 = 0; 0 | 1 = 1; 1 | 1 = 1
# 5  0101     3  0011     5 | 3  0111

# & (like 'and', '&&')
# 0 & 0 = 0; 0 & 1 = 0; 1 & 1 = 1
# 5  0101     3  0011     5 & 3  0001

# ^ (XOR)
# 0 ^ 0 = 0; 0 ^ 1 = 1; 1 ^ 1 = 0
# 5  0101     3  0011     5 ^ 3  0110


# bit shifts
# Bits are moved (shifted) to the left or right
#  The bits that fall outside the number are lost and replaced by 0

# Left shift (<< operator)
# from: 1 1 0 1 0 0 1 1
# to: x 1 0 1 0 0 1 1 0

# Right shift (>> operator)
# from: 0 1 1 0 0 1 1 1
# to:   0 0 1 1 0 0 1 1 x
