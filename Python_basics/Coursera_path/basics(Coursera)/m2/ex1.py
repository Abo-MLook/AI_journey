sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
last = sports[:-4:-1]
print(last)

x = "a dasasd a"
b = x.split('d')
print(b)
print(type(b))


b = "My, what a lovely day"
x = b.split(',')
z = "".join(x)
print(z)
y = z.split() #! not putting anything in split it will split any whitespace character
a = "||".join(y)
print(a)
print(type(a))



m = sports[1:2] # type is list
print(len(m))
m1 = sports[1]   # type is String
nums = [x for x in range(0,68)]
print(nums)

original_str = "The quick brown rhino jumped over the extremely lazy fox"
num_words_list = [len(x) for x in  original_str.split(" ") ]
print(num_words_list)

let = ""
let.join("b")
print(let)