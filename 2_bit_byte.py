# 二进制与字符编码
# 1字节 = 8位
# 1byte = 8bit 可以表示 2^8 = 256种状态

# 二进制0，1 --> ASCII --> GB2312(中文编码) --> GBK(中文编码) --> GB18030(中文编码) --> Unicode(几乎包含全世界字符) --> UTF-8

print(chr(0b100111001011000))
print(ord("乘"))