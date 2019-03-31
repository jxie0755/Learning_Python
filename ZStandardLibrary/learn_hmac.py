# Learn hmac


# 通过哈希算法，我们可以验证一段数据是否有效，方法就是对比该数据的哈希值
    # 例如，判断用户口令是否正确，我们用保存在数据库中的password_md5对比计算md5(password)的结果
        # 如果一致，用户输入的口令就是正确的

# 为了防止黑客通过彩虹表根据哈希值反推原始口令:
    # 在计算哈希的时候，不能仅针对原始输入计算
    # 还需要增加一个salt来使得相同的输入也能得到不同的哈希
    # 这样，大大增加了黑客破解的难度。
    # 如果salt是我们自己随机生成的，通常我们计算MD5时采用md5(message + salt)。

# 但实际上，把salt看做一个“口令”，加salt的哈希就是：
    # 计算一段message的哈希时，根据不通口令计算出不同的哈希。
    # 要验证哈希值，必须同时提供正确的口令。

# 这实际上就是Hmac算法：
    # Keyed-Hashing for Message Authentication。
    # 它通过一个标准算法，在计算哈希的过程中，把key混入计算过程中。
    # 和我们自定义的加salt算法不同，Hmac算法针对所有哈希算法都通用，无论是MD5还是SHA-1。
    # 采用Hmac替代我们自己的salt算法，可以使程序算法更标准化，也更安全。

# Python自带的hmac模块实现了标准的Hmac算法:
    # hmac输出的长度和原始哈希算法的长度一致。
    # 需要注意传入的key和message都是bytes类型，str类型需要首先编码为bytes

import hashlib
import hmac

message = b'Hello, world!'
# 普通MD5
message_md5 = hashlib.md5(message)
print(message_md5.hexdigest()) # >>> 6cd3556deb0da54bca060b4c39479839

# 使用hmac
key_f = b''
key_t = b'secret'
# 如果消息很长，同样可以多次调用h_f.update(msg)
h_f = hmac.new(key_f, message, digestmod='MD5')
print(h_f.hexdigest())         # >>> aa9a95b3aa6dcef53bf23e2a3f801b44
                               # 即使是空字符也会不一样

h_t = hmac.new(key_t, message, digestmod='MD5')
print(h_t.hexdigest())         # >>>  fa4ee7d173f2d97ee79022d1a7355bcf
