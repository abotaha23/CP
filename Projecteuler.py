from itertools import product,  permutations
from math import factorial as f, sqrt
from fractions import *
from collections import Counter
from time import time
# problem 1
'''
result=0
for number in range(1000):
    if number%3 == 0 or number%5 == 0:
        result=result+number
#print(result)
#problem 2
a=1
b=2
sum=0
c=0
while c<=4000000:
    c = a + b
    a = b
    b = c
    if c%2 == 0:
        sum=sum+c
'''
# print(sum+2)
# problem 3
'''
i=2
n=600851475143
while i*i<n:
    while n%i==0:
        n=n/i
    i+=1
#print(n)
#problem 4
#print("good"[::-1])
'''
'''
def parlindrome(str):
    return str==str[::-1]
max=0
for i in range(100, 1000):
    for x in range(i+1, 1000):
        p=i*x
        if p > max and parlindrome(str(p)):
            max = p
'''
# print(max)
# problem 5
# weak code
'''
o=1
while True:
    if o%2==0 and o%3==0 and o%4==0 and o%5==0 and o%6==0 and o%7==0 and o%8==0 and o%9==0 and o%10==0and o%11==0 and o%12==0 and o%13==0 and o%14==0 and o%15==0 and o%16==0 and o%17==0 and o%18==0 and o%19==0 and o%20==0:
        print(o)
        break
    else:o+=1
#stronger code
#Be proud this is yours.
b=1
'''
'''
while True:
    if all(b%n==0 for n in range(2, 20)):
        print(b)
        break
    else:
        b+=1
'''
# problem 6

import time

'''
start=time.time()
sum_then_power=0
power_then_sum=0
for n in range(1, 101):
    power_then_sum+=n**2
for b in range(1, 101):
    sum_then_power+=b
print(sum_then_power**2-power_then_sum)
finish=time.time()
print(finish-start)
'''
'''
#problem 7

start=time.time()
num=4
prime_nums=[]
while True:
    if all(num%n!=0 for n in range(2, num)):
        prime_nums+=[num]
        num+=1
        if len(prime_nums)==9999:
            print(prime_nums[-1])
            break
    else:
        num+=1

finish=time.time()
print(finish-start)
'''
# problem 8
'''
start=time.time()
nums=[]
products=[]
for n in "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450":
    nums += [int(n)]

for i in range(988):
    product=nums[i]
    for b in range(i + 1,  i + 13):
        product *= nums[b]
    products+=[product]
print(max(products))
finish=time.time()
print(finish-start)
number = "73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450"
print(number)
'''
# problem 9
'''
start = time.time()
from math import *
while True:
    for a in range(1,  1000):
        for b in range(a+1,  1000):
            c = 1000-a-b
            if c == sqrt(a**2 + b**2):
                print(a*b*c)
                break
    break
finish = time.time()
print(finish-start)
'''
# problem 10
'''
start = time.time()
prime_nums = [2]
sum = 0
for i in range(3,  2000000):
    if any(i % n == 0 for n in range(2,  i)):
        continue
    else:
        sum += i
print(sum+2)
print(time.time()-start)

start = time.time()
sum = 0
i = 2
while i < 40000:
    if any(i % n == 0 for n in range(2,  i)):
        i += 1
        continue
    else:
        sum += i
    i += 1
print(sum)
print(time.time()-start)
'''
'''
start = time.time()
limit = 2000000
is_prime_array = [True] * limit


# functions finish the process much faster !!!
def prime_sieve(index):
    the_sum = 0
    for i in range(2,  limit):
        if index[i]:
            the_sum += i
            k = i * 2
            while k < limit:
                index[k] = False
                k += i
    return the_sum


print(prime_sieve(is_prime_array))
print("Time spent=",  time.time()-start)
'''
'''
start = time.time()
grid = [8,  2,  22,  97,  38,  15,  00,  40,  00,  75,  4,  5,  7,  78,  52,  12,  50,  77,  91,  8, 
        49,  49,  99,  40,  17,  81,  18,  57,  60,  87,  17,  40,  98,  43,  69,  48,  4,  56,  62,  00, 
        81,  49,  31,  73,  55,  79,  14,  29,  93,  71,  40,  67,  53,  88,  30,  3,  49,  13,  36,  65, 
        52,  70,  95,  23,  4,  60,  11,  42,  69,  24,  68,  56,  1,  32,  56,  71,  37,  2,  36,  91, 
        22,  31,  16,  71,  51,  67,  63,  89,  41,  92,  36,  54,  22,  40,  40,  28,  66,  33,  13,  80, 
        24,  47,  32,  60,  99,  3,  45,  2,  44,  75,  33,  53,  78,  36,  84,  20,  35,  17,  12,  50, 
        32,  98,  81,  28,  64,  23,  67,  10,  26,  38,  40,  67,  59,  54,  70,  66,  18,  38,  64,  70, 
        67,  26,  20,  68,  2,  62,  12,  20,  95,  63,  94,  39,  63,  8,  40,  91,  66,  49,  94,  21, 
        24,  55,  58,  5,  66,  73,  99,  26,  97,  17,  78,  78,  96,  83,  14,  88,  34,  89,  63,  72, 
        21,  36,  23,  9,  75,  00,  76,  44,  20,  45,  35,  14,  00,  61,  33,  97,  34,  31,  33,  95, 
        78,  17,  53,  28,  22,  75,  31,  67,  15,  94,  3,  80,  4,  62,  16,  14,  9,  53,  56,  92, 
        16,  39,  5,  42,  96,  35,  31,  47,  55,  58,  88,  24,  00,  17,  54,  24,  36,  29,  85,  57, 
        86,  56,  00,  48,  35,  71,  89,  7,  5,  44,  44,  37,  44,  60,  21,  58,  51,  54,  17,  58, 
        19,  80,  81,  68,  5,  94,  47,  69,  28,  73,  92,  13,  86,  52,  17,  77,  4,  89,  55,  40, 
        4,  52,  8,  83,  97,  35,  99,  16,  7,  97,  57,  32,  16,  26,  26,  79,  33,  27,  98,  66, 
        88,  36,  68,  87,  57,  62,  20,  72,  3,  46,  33,  67,  46,  55,  12,  32,  63,  93,  53,  69, 
        4,  42,  16,  73,  38,  25,  39,  11,  24,  94,  72,  18,  8,  46,  29,  32,  40,  62,  76,  36, 
        20,  69,  36,  41,  72,  30,  23,  88,  34,  62,  99,  69,  82,  67,  59,  85,  74,  4,  36,  16, 
        20,  73,  35,  29,  78,  31,  90,  1,  74,  31,  49,  71,  48,  86,  81,  16,  23,  57,  5,  54, 
        1,  70,  54,  71,  83,  51,  54,  69,  16,  92,  33,  48,  61,  43,  52,  1,  89,  19,  67,  48]
collection = []
max_num = 0
i = 0
a = 0
n = 0
b = 19
x = 0
y = 0
z = 0
u = 0
nums = []
while i < 340:
    up_down = grid[i] * grid[i + 20] * grid[40 + i] * grid[60 + i]
    collection += [up_down]
    nums += [(grid[i],  grid[i + 20],  grid[i + 40],  grid[(60 + i)])]
    if i == 320 + u:
        i -= 319
        u += 1
    else:
        i += 20
while a < 397:
    left_right = grid[a] * grid[a + 1] * grid[2 + a] * grid[3 + a]
    collection += [left_right]
    nums += [(grid[a],  grid[a + 1],  grid[a + 2],  grid[3 + a])]
    a += 1
    if a == (17 + 20 * x):
        a += 3
        x += 1
while n < 337:
    diagonally_right = grid[n] * grid[n + 21] * grid[42 + n] * grid[63 + n]
    collection += [diagonally_right]
    nums += [(grid[n],  grid[n + 21],  grid[n + 42],  grid[63 + n])]
    n += 1
    if n == (17 + 20 * y):
        n += 3
        y += 1
while b < 340:
    diagonally_left = grid[b] * grid[b + 19] * grid[b + 38] * grid[b + 57]
    collection += [diagonally_left]
    nums += [(grid[b],  grid[b + 19],  grid[b + 38],  grid[b + 57])]
    b -= 1
    if b == (2 + 20 * z):
        b += 37
        z += 1
print(max(collection),  nums[collection.index(max(collection))])

print("Time spent: ",  time.time() - start)
'''
'''
# problem 12
# this solution is more fast than the below.
start = time.time()
b = 3
c = 3
factors = []
while len(factors) != 250:
    factors = []
    c += b
    b += 1
    n = 2
    while True:
        if c % n == 0:
            factors += [True]
            n += 1
            if n > c ** 0.5 or len(factors) == 250:
                break
        else:
            n += 1
print(c,  time.time() - start)
'''
'''
start = time.time()
c = 3
b = 3
factors = []
while len(factors) != 250:
    c += b
    b += 1
    factors = []
    for n in range(2,  int(c ** 0.5 + 1)):
        if c % n == 0:
            factors += [True]
        if len(factors) == 250:
            break
print(c,  time.time() - start)
'''
'''
# problem 13
numbers = [37107287533902102798797998220837590246510135740250, 
           46376937677490009712648124896970078050417018260538, 
           74324986199524741059474233309513058123726617309629, 
           91942213363574161572522430563301811072406154908250, 
           23067588207539346171171980310421047513778063246676, 
           89261670696623633820136378418383684178734361726757, 
           28112879812849979408065481931592621691275889832738, 
           44274228917432520321923589422876796487670272189318, 
           47451445736001306439091167216856844588711603153276, 
           70386486105843025439939619828917593665686757934951, 
           62176457141856560629502157223196586755079324193331, 
           64906352462741904929101432445813822663347944758178, 
           92575867718337217661963751590579239728245598838407, 
58203565325359399008402633568948830189458628227828, 
80181199384826282014278194139940567587151170094390, 
35398664372827112653829987240784473053190104293586, 
86515506006295864861532075273371959191420517255829, 
71693888707715466499115593487603532921714970056938, 
54370070576826684624621495650076471787294438377604, 
53282654108756828443191190634694037855217779295145, 
36123272525000296071075082563815656710885258350721, 
45876576172410976447339110607218265236877223636045, 
17423706905851860660448207621209813287860733969412, 
81142660418086830619328460811191061556940512689692, 
51934325451728388641918047049293215058642563049483, 
62467221648435076201727918039944693004732956340691, 
15732444386908125794514089057706229429197107928209, 
55037687525678773091862540744969844508330393682126, 
18336384825330154686196124348767681297534375946515, 
80386287592878490201521685554828717201219257766954, 
78182833757993103614740356856449095527097864797581, 
16726320100436897842553539920931837441497806860984, 
48403098129077791799088218795327364475675590848030, 
87086987551392711854517078544161852424320693150332, 
59959406895756536782107074926966537676326235447210, 
69793950679652694742597709739166693763042633987085, 
41052684708299085211399427365734116182760315001271, 
65378607361501080857009149939512557028198746004375, 
35829035317434717326932123578154982629742552737307, 
94953759765105305946966067683156574377167401875275, 
88902802571733229619176668713819931811048770190271, 
25267680276078003013678680992525463401061632866526, 
36270218540497705585629946580636237993140746255962, 
24074486908231174977792365466257246923322810917141, 
91430288197103288597806669760892938638285025333403, 
34413065578016127815921815005561868836468420090470, 
23053081172816430487623791969842487255036638784583, 
11487696932154902810424020138335124462181441773470, 
63783299490636259666498587618221225225512486764533, 
67720186971698544312419572409913959008952310058822, 
95548255300263520781532296796249481641953868218774, 
76085327132285723110424803456124867697064507995236, 
37774242535411291684276865538926205024910326572967, 
23701913275725675285653248258265463092207058596522, 
29798860272258331913126375147341994889534765745501, 
18495701454879288984856827726077713721403798879715, 
38298203783031473527721580348144513491373226651381, 
34829543829199918180278916522431027392251122869539, 
40957953066405232632538044100059654939159879593635, 
29746152185502371307642255121183693803580388584903, 
41698116222072977186158236678424689157993532961922, 
62467957194401269043877107275048102390895523597457, 
23189706772547915061505504953922979530901129967519, 
86188088225875314529584099251203829009407770775672, 
11306739708304724483816533873502340845647058077308, 
82959174767140363198008187129011875491310547126581, 
97623331044818386269515456334926366572897563400500, 
42846280183517070527831839425882145521227251250327, 
55121603546981200581762165212827652751691296897789, 
32238195734329339946437501907836945765883352399886, 
75506164965184775180738168837861091527357929701337, 
62177842752192623401942399639168044983993173312731, 
32924185707147349566916674687634660915035914677504, 
99518671430235219628894890102423325116913619626622, 
73267460800591547471830798392868535206946944540724, 
76841822524674417161514036427982273348055556214818, 
97142617910342598647204516893989422179826088076852, 
87783646182799346313767754307809363333018982642090, 
10848802521674670883215120185883543223812876952786, 
71329612474782464538636993009049310363619763878039, 
62184073572399794223406235393808339651327408011116, 
66627891981488087797941876876144230030984490851411, 
60661826293682836764744779239180335110989069790714, 
85786944089552990653640447425576083659976645795096, 
66024396409905389607120198219976047599490197230297, 
64913982680032973156037120041377903785566085089252, 
16730939319872750275468906903707539413042652315011, 
94809377245048795150954100921645863754710598436791, 
78639167021187492431995700641917969777599028300699, 
15368713711936614952811305876380278410754449733078, 
40789923115535562561142322423255033685442488917353, 
44889911501440648020369068063960672322193204149535, 
41503128880339536053299340368006977710650566631954, 
81234880673210146739058568557934581403627822703280, 
82616570773948327592232845941706525094512325230608, 
22918802058777319719839450180888072429661980811197, 
77158542502016545090413245809786882778948721859617, 
72107838435069186155435662884062257473692284509516, 
20849603980134001723930671666823555245252804609722, 
53503534226472524250874054075591789781264330331690]
n = 0
for i in range(100):
    n += numbers[i]
print(str(n)[0: 10])
'''
# problem 14
'''
import time
start = time.time()


def largest(limit):
    i = 13
    number_of_elements = []
    while i < limit:
        n = i
        collatz_nums = [n]
        while n != 1:
            if n % 2 == 0:
                n /= 2
                collatz_nums += [n]
            else:
                n = 3 * n + 1
                collatz_nums += [n]
        number_of_elements += [len(collatz_nums)]
        i += 2
    return number_of_elements



print(largest(1000000).index(max(largest(1000000))) * 2 + 13)


print("Time spent: ",  time.time() - start)
'''
'''
i = 13
while i < 14:
    n = i
    collatz_nums = [n]
    while n != 1:
        if n % 2 == 0:
            n /= 2
            collatz_nums += [n]
        else:
            n = 3 * n + 1
            collatz_nums += [n]
    i += 1
print(collatz_nums)
'''
# problem 15

'''
def possibilities(limit):
    coordinates = [] # The all coordinates ever
    new_coordinate = [] # each new coordinate
    origin_coordinate = [0,  limit]
    variable_coordinate = origin_coordinate
    for i in range(1,  limit + 1):
        for n in range(limit):
            if variable_coordinate[0] != limit:
                variable_coordinate[0] += 1
                new_coordinate += variable_coordinate
            if variable_coordinate[1] != 0:
                variable_coordinate[1] -= 1
                new_coordinate += variable_coordinate
            if variable_coordinate == [limit,  0]:
                coordinates += [new_coordinate]
                break
        variable_coordinate = origin_coordinate
        variable_coordinate[1] -= i
    for u in range(len(coordinates)):
        if coordinates.count(coordinates[u]) != 1:
            coordinates.remove(coordinates[u])
    return coordinates


print(possibilities(2),  len(possibilities(2)))
# problem 17

def collect(limit):
    import time
    start = time.time()
    letters_sum = 0
    for i in range(1,  limit + 1):
        # units
        if str(i)[-1] in ["1",  "2",  "6"]:
            letters_sum += 3
        if str(i)[-1] in ["3",  "7",  "8"]:
            letters_sum += 5
        if str(i)[-1] in ["4",  "5",  "9"]:
            letters_sum += 4
        # tens
        if len(str(i)) > 1:
            if str(i)[-2] + str(i)[-1] in ["10",  "11",  "12",  "13"]:
                letters_sum += 3
            if str(i)[-2] + str(i)[-1] in ["14",  "16",  "17",  "19"]:
                letters_sum += 4
            if str(i)[-2] + str(i)[-1] in ["15",  "18"]:
                letters_sum += 3
            if str(i)[-2] in ["2",  "3",  "8",  "9"]:
                letters_sum += 6
            if str(i)[-2] in ["5",  "6"]:
                letters_sum += 5
            if str(i)[-2] == "7":
                letters_sum += 7
            if str(i)[-2] == "4":
                letters_sum += 5
        # thousands
        if len(str(i)) > 2:
            if i in range(101,  200) or i in range(201,  300) or i in range(601,  700):
                letters_sum += 13
            if i in range(301,  400) or i in range(701,  800) or i in range(801,  900):
                letters_sum += 15
            if i in range(401,  500) or i in range(501,  600) or i in range(901,  1000):
                letters_sum += 14
            if i in [100,  200,  600]:
                letters_sum += 10
            if i in [300,  700,  800]:
                letters_sum += 12
            if i in [400,  500,  900]:
                letters_sum += 11
        if i == 1000:
            letters_sum += 11
    return letters_sum,   'Time spent: ',  time.time()-start


print(collect(1000))

# problem 18
nums = [[75], 
[95,  64], 
[17,  47,  82], 
[18,  35,  87,  10], 
[20,  4,  82,  47,  65], 
[19,  1,  23,  75,  3,  34], 
[88,  2,  77,  73,  7,  63,  67], 
[99,  65,  4,  28,  6,  16,  70,  92], 
[41,  41,  26,  56,  83,  40,  80,  70,  33], 
[41,  48,  72,  33,  47,  32,  37,  16,  94,  29], 
[53,  71,  44,  65,  25,  43,  91,  52,  97,  51,  14], 
[70,  11,  33,  28,  77,  73,  17,  78,  39,  68,  17,  57], 
[91,  71,  52,  38,  17,  14,  91,  43,  58,  50,  27,  29,  48], 
[63,  66,  4,  68,  89,  53,  67,  30,  73,  16,  69,  87,  40,  31], 
[4,  62,  98,  27,  23,  9,  70,  98,  73,  93,  38,  53,  60,  4,  23]]


def biggest():
    while len(nums) != 1:  # when it reaches a solution the loop will break
        i = -1
        while -i < len(nums[-1]):
            nums[-2][i] += max(nums[-1][i],  nums[-1][i - 1])  # summing up the biggest numbers
            i -= 1
        nums.pop()
    return nums[0][0]

print(biggest())
# Great job bro you made it so far.
# problem 19
import time,  calendar
start = time.time()


def sunday():
    counter = 0
    date = {"order": 1,  "day": 3,  "month": 1,  "year": 1900}
    while date["year"] != 2001:
        if date["order"] == 1 and date["day"] == 2 and date["year"] > 1900:
            counter += 1
        date["order"] += 1
        date["day"] += 1
        if date["order"] == 29 and date["month"] == 2 and not calendar.isleap(date["year"]):  # there are two solutions
            # the first one you have already made and the second one you made it now using the module calendar.
            date["order"] = 1
            date["month"] += 1
        if date["order"] == 31 and date["month"] not in [1,  2,  3,  5,  7,  8,  10,  12]:
            date["order"] = 1
            date["month"] += 1
        if date["order"] == 32 and date["month"] in [1,  3,  5,  7,  8,  10,  12]:
            date["order"] = 1
            date["month"] += 1
        if date["order"] == 30 and date["month"] == 2 and calendar.isleap(date["year"]):
            date["order"] = 1
            date["month"] += 1
        if date["day"] == 8:
            date["day"] = 1
        if date["month"] == 13:
            date["month"] = 1
            date["year"] += 1
    return counter


print(sunday(),  time.time() - start)
# Keep going my great programmer.
# problem 20
from math import *
start = time.time()
sum = 0
for i in str(factorial(100)):
    sum += int(i)
print(sum,  time.time() - start)
import time
# problem 21
start = time.time()


def amicable(limit):
    total = 0
    for i in range(2,  limit):
        d_i = 0
        di = 0
        for n in range(1,  i):
            if i % n == 0:
                di += n
        for m in range(1,  di):
            if di % m == 0:
                d_i += m
        if i == d_i and i != di:
            total += i
    return total


print(amicable(10000),  time.time() - start)
# You're fascinating !!!
# problem 22
start = time.time()
names = ["MARY", "PATRICIA", "LINDA", "BARBARA", "ELIZABETH", "JENNIFER", "MARIA", "SUSAN", "MARGARET", "DOROTHY", 
         "LISA", "NANCY", "KAREN", "BETTY", "HELEN", "SANDRA", "DONNA", "CAROL", "RUTH", "SHARON", "MICHELLE", "LAURA", 
         "SARAH", "KIMBERLY", "DEBORAH", "JESSICA", "SHIRLEY", "CYNTHIA", "ANGELA", "MELISSA", "BRENDA", "AMY", "ANNA", 
         "REBECCA", "VIRGINIA", "KATHLEEN", "PAMELA", "MARTHA", "DEBRA", "AMANDA", "STEPHANIE", "CAROLYN", "CHRISTINE", 
         "MARIE", "JANET", "CATHERINE", "FRANCES", "ANN", "JOYCE", "DIANE", "ALICE", "JULIE", "HEATHER", "TERESA", "DORIS", 
         "GLORIA", "EVELYN", "JEAN", "CHERYL", "MILDRED", "KATHERINE", "JOAN", "ASHLEY", "JUDITH", "ROSE", "JANICE", "KELLY", 
         "NICOLE", "JUDY", "CHRISTINA", "KATHY", "THERESA", "BEVERLY", "DENISE", "TAMMY", "IRENE", "JANE", "LORI", "RACHEL", 
         "MARILYN", "ANDREA", "KATHRYN", "LOUISE", "SARA", "ANNE", "JACQUELINE", "WANDA", "BONNIE", "JULIA", "RUBY", "LOIS", 
         "TINA", "PHYLLIS", "NORMA", "PAULA", "DIANA", "ANNIE", "LILLIAN", "EMILY", "ROBIN", "PEGGY", "CRYSTAL", "GLADYS", 
         "RITA", "DAWN", "CONNIE", "FLORENCE", "TRACY", "EDNA", "TIFFANY", "CARMEN", "ROSA", "CINDY", "GRACE", "WENDY", "VICTORIA", 
         "EDITH", "KIM", "SHERRY", "SYLVIA", "JOSEPHINE", "THELMA", "SHANNON", "SHEILA", "ETHEL", "ELLEN", "ELAINE", "MARJORIE", "CARRIE", 
         "CHARLOTTE", "MONICA", "ESTHER", "PAULINE", "EMMA", "JUANITA", "ANITA", "RHONDA", "HAZEL", "AMBER", "EVA", "DEBBIE", "APRIL", "LESLIE", "CLARA", "LUCILLE", "JAMIE", "JOANNE", "ELEANOR", "VALERIE", "DANIELLE", "MEGAN", "ALICIA", "SUZANNE", "MICHELE", "GAIL", "BERTHA", "DARLENE", "VERONICA", "JILL", "ERIN", "GERALDINE", "LAUREN", "CATHY", "JOANN", "LORRAINE", "LYNN", "SALLY", "REGINA", "ERICA", "BEATRICE", "DOLORES", "BERNICE", "AUDREY", "YVONNE", "ANNETTE", "JUNE", "SAMANTHA", "MARION", "DANA", "STACY", "ANA", "RENEE", "IDA", "VIVIAN", "ROBERTA", "HOLLY", "BRITTANY", "MELANIE", "LORETTA", "YOLANDA", "JEANETTE", "LAURIE", "KATIE", "KRISTEN", "VANESSA", "ALMA", "SUE", "ELSIE", "BETH", "JEANNE", "VICKI", "CARLA", "TARA", "ROSEMARY", "EILEEN", "TERRI", "GERTRUDE", "LUCY", "TONYA", "ELLA", "STACEY", "WILMA", "GINA", "KRISTIN", "JESSIE", "NATALIE", "AGNES", "VERA", "WILLIE", "CHARLENE", "BESSIE", "DELORES", "MELINDA", "PEARL", "ARLENE", "MAUREEN", "COLLEEN", "ALLISON", "TAMARA", "JOY", "GEORGIA", "CONSTANCE", "LILLIE", "CLAUDIA", "JACKIE", "MARCIA", "TANYA", "NELLIE", "MINNIE", "MARLENE", "HEIDI", "GLENDA", "LYDIA", "VIOLA", "COURTNEY", "MARIAN", "STELLA", "CAROLINE", "DORA", "JO", "VICKIE", "MATTIE", "TERRY", "MAXINE", "IRMA", "MABEL", "MARSHA", "MYRTLE", "LENA", "CHRISTY", "DEANNA", "PATSY", "HILDA", "GWENDOLYN", "JENNIE", "NORA", "MARGIE", "NINA", "CASSANDRA", "LEAH", "PENNY", "KAY", "PRISCILLA", "NAOMI", "CAROLE", "BRANDY", "OLGA", "BILLIE", "DIANNE", "TRACEY", "LEONA", "JENNY", "FELICIA", "SONIA", "MIRIAM", "VELMA", "BECKY", "BOBBIE", "VIOLET", "KRISTINA", "TONI", "MISTY", "MAE", "SHELLY", "DAISY", "RAMONA", "SHERRI", "ERIKA", "KATRINA", "CLAIRE", "LINDSEY", "LINDSAY", "GENEVA", "GUADALUPE", "BELINDA", "MARGARITA", "SHERYL", "CORA", "FAYE", "ADA", "NATASHA", "SABRINA", "ISABEL", "MARGUERITE", "HATTIE", "HARRIET", "MOLLY", "CECILIA", "KRISTI", "BRANDI", "BLANCHE", "SANDY", "ROSIE", "JOANNA", "IRIS", "EUNICE", "ANGIE", "INEZ", "LYNDA", "MADELINE", "AMELIA", "ALBERTA", "GENEVIEVE", "MONIQUE", "JODI", "JANIE", "MAGGIE", "KAYLA", "SONYA", "JAN", "LEE", "KRISTINE", "CANDACE", "FANNIE", "MARYANN", "OPAL", "ALISON", "YVETTE", "MELODY", "LUZ", "SUSIE", "OLIVIA", "FLORA", "SHELLEY", "KRISTY", "MAMIE", "LULA", "LOLA", "VERNA", "BEULAH", "ANTOINETTE", "CANDICE", "JUANA", "JEANNETTE", "PAM", "KELLI", "HANNAH", "WHITNEY", "BRIDGET", "KARLA", "CELIA", "LATOYA", "PATTY", "SHELIA", "GAYLE", "DELLA", "VICKY", "LYNNE", "SHERI", "MARIANNE", "KARA", "JACQUELYN", "ERMA", "BLANCA", "MYRA", "LETICIA", "PAT", "KRISTA", "ROXANNE", "ANGELICA", "JOHNNIE", "ROBYN", "FRANCIS", "ADRIENNE", "ROSALIE", "ALEXANDRA", "BROOKE", "BETHANY", "SADIE", "BERNADETTE", "TRACI", "JODY", "KENDRA", "JASMINE", "NICHOLE", "RACHAEL", "CHELSEA", "MABLE", "ERNESTINE", "MURIEL", "MARCELLA", "ELENA", "KRYSTAL", "ANGELINA", "NADINE", "KARI", "ESTELLE", "DIANNA", "PAULETTE", "LORA", "MONA", "DOREEN", "ROSEMARIE", "ANGEL", "DESIREE", "ANTONIA", "HOPE", "GINGER", "JANIS", "BETSY", "CHRISTIE", "FREDA", "MERCEDES", "MEREDITH", "LYNETTE", "TERI", "CRISTINA", "EULA", "LEIGH", "MEGHAN", "SOPHIA", "ELOISE", "ROCHELLE", "GRETCHEN", "CECELIA", "RAQUEL", "HENRIETTA", "ALYSSA", "JANA", "KELLEY", "GWEN", "KERRY", "JENNA", "TRICIA", "LAVERNE", "OLIVE", "ALEXIS", "TASHA", "SILVIA", "ELVIRA", "CASEY", "DELIA", "SOPHIE", "KATE", "PATTI", "LORENA", "KELLIE", "SONJA", "LILA", "LANA", "DARLA", "MAY", "MINDY", "ESSIE", "MANDY", "LORENE", "ELSA", "JOSEFINA", "JEANNIE", "MIRANDA", "DIXIE", "LUCIA", "MARTA", "FAITH", "LELA", "JOHANNA", "SHARI", "CAMILLE", "TAMI", "SHAWNA", "ELISA", "EBONY", "MELBA", "ORA", "NETTIE", "TABITHA", "OLLIE", "JAIME", "WINIFRED", "KRISTIE", "MARINA", "ALISHA", "AIMEE", "RENA", "MYRNA", "MARLA", "TAMMIE", "LATASHA", "BONITA", "PATRICE", "RONDA", "SHERRIE", "ADDIE", "FRANCINE", "DELORIS", "STACIE", "ADRIANA", "CHERI", "SHELBY", "ABIGAIL", "CELESTE", "JEWEL", "CARA", "ADELE", "REBEKAH", "LUCINDA", "DORTHY", "CHRIS", "EFFIE", "TRINA", "REBA", "SHAWN", "SALLIE", "AURORA", "LENORA", "ETTA", "LOTTIE", "KERRI", "TRISHA", "NIKKI", "ESTELLA", "FRANCISCA", "JOSIE", "TRACIE", "MARISSA", "KARIN", "BRITTNEY", "JANELLE", "LOURDES", "LAUREL", "HELENE", "FERN", "ELVA", "CORINNE", "KELSEY", "INA", "BETTIE", "ELISABETH", "AIDA", "CAITLIN", "INGRID", "IVA", "EUGENIA", "CHRISTA", "GOLDIE", "CASSIE", "MAUDE", "JENIFER", "THERESE", "FRANKIE", "DENA", "LORNA", "JANETTE", "LATONYA", "CANDY", "MORGAN", "CONSUELO", "TAMIKA", "ROSETTA", "DEBORA", "CHERIE", "POLLY", "DINA", "JEWELL", "FAY", "JILLIAN", "DOROTHEA", "NELL", "TRUDY", "ESPERANZA", "PATRICA", "KIMBERLEY", "SHANNA", "HELENA", "CAROLINA", "CLEO", "STEFANIE", "ROSARIO", "OLA", "JANINE", "MOLLIE", "LUPE", "ALISA", "LOU", "MARIBEL", "SUSANNE", "BETTE", "SUSANA", "ELISE", "CECILE", "ISABELLE", "LESLEY", "JOCELYN", "PAIGE", "JONI", "RACHELLE", "LEOLA", "DAPHNE", "ALTA", "ESTER", "PETRA", "GRACIELA", "IMOGENE", "JOLENE", "KEISHA", "LACEY", "GLENNA", "GABRIELA", "KERI", "URSULA", "LIZZIE", "KIRSTEN", "SHANA", "ADELINE", "MAYRA", "JAYNE", "JACLYN", "GRACIE", "SONDRA", "CARMELA", "MARISA", "ROSALIND", "CHARITY", "TONIA", "BEATRIZ", "MARISOL", "CLARICE", "JEANINE", "SHEENA", "ANGELINE", "FRIEDA", "LILY", "ROBBIE", "SHAUNA", "MILLIE", "CLAUDETTE", "CATHLEEN", "ANGELIA", "GABRIELLE", "AUTUMN", "KATHARINE", "SUMMER", "JODIE", "STACI", "LEA", "CHRISTI", "JIMMIE", "JUSTINE", "ELMA", "LUELLA", "MARGRET", "DOMINIQUE", "SOCORRO", "RENE", "MARTINA", "MARGO", "MAVIS", "CALLIE", "BOBBI", "MARITZA", "LUCILE", "LEANNE", "JEANNINE", "DEANA", "AILEEN", "LORIE", "LADONNA", "WILLA", "MANUELA", "GALE", "SELMA", "DOLLY", "SYBIL", "ABBY", "LARA", "DALE", "IVY", "DEE", "WINNIE", "MARCY", "LUISA", "JERI", "MAGDALENA", "OFELIA", "MEAGAN", "AUDRA", "MATILDA", "LEILA", "CORNELIA", "BIANCA", "SIMONE", "BETTYE", "RANDI", "VIRGIE", "LATISHA", "BARBRA", "GEORGINA", "ELIZA", "LEANN", "BRIDGETTE", "RHODA", "HALEY", "ADELA", "NOLA", "BERNADINE", "FLOSSIE", "ILA", "GRETA", "RUTHIE", "NELDA", "MINERVA", "LILLY", "TERRIE", "LETHA", "HILARY", "ESTELA", "VALARIE", "BRIANNA", "ROSALYN", "EARLINE", "CATALINA", "AVA", "MIA", "CLARISSA", "LIDIA", "CORRINE", "ALEXANDRIA", "CONCEPCION", "TIA", "SHARRON", "RAE", "DONA", "ERICKA", "JAMI", "ELNORA", "CHANDRA", "LENORE", "NEVA", "MARYLOU", "MELISA", "TABATHA", "SERENA", "AVIS", "ALLIE", "SOFIA", "JEANIE", "ODESSA", "NANNIE", "HARRIETT", "LORAINE", "PENELOPE", "MILAGROS", "EMILIA", "BENITA", "ALLYSON", "ASHLEE", "TANIA", "TOMMIE", "ESMERALDA", "KARINA", "EVE", "PEARLIE", "ZELMA", "MALINDA", "NOREEN", "TAMEKA", "SAUNDRA", "HILLARY", "AMIE", "ALTHEA", "ROSALINDA", "JORDAN", "LILIA", "ALANA", "GAY", "CLARE", "ALEJANDRA", "ELINOR", "MICHAEL", "LORRIE", "JERRI", "DARCY", "EARNESTINE", "CARMELLA", "TAYLOR", "NOEMI", "MARCIE", "LIZA", "ANNABELLE", "LOUISA", "EARLENE", "MALLORY", "CARLENE", "NITA", "SELENA", "TANISHA", "KATY", "JULIANNE", "JOHN", "LAKISHA", "EDWINA", "MARICELA", "MARGERY", "KENYA", "DOLLIE", "ROXIE", "ROSLYN", "KATHRINE", "NANETTE", "CHARMAINE", "LAVONNE", "ILENE", "KRIS", "TAMMI", "SUZETTE", "CORINE", "KAYE", "JERRY", "MERLE", "CHRYSTAL", "LINA", "DEANNE", "LILIAN", "JULIANA", "ALINE", "LUANN", "KASEY", "MARYANNE", "EVANGELINE", "COLETTE", "MELVA", "LAWANDA", "YESENIA", "NADIA", "MADGE", "KATHIE", "EDDIE", "OPHELIA", "VALERIA", "NONA", "MITZI", "MARI", "GEORGETTE", "CLAUDINE", "FRAN", "ALISSA", "ROSEANN", "LAKEISHA", "SUSANNA", "REVA", "DEIDRE", "CHASITY", "SHEREE", "CARLY", "JAMES", "ELVIA", "ALYCE", "DEIRDRE", "GENA", "BRIANA", "ARACELI", "KATELYN", "ROSANNE", "WENDI", "TESSA", "BERTA", "MARVA", "IMELDA", "MARIETTA", "MARCI", "LEONOR", "ARLINE", "SASHA", "MADELYN", "JANNA", "JULIETTE", "DEENA", "AURELIA", "JOSEFA", "AUGUSTA", "LILIANA", "YOUNG", "CHRISTIAN", "LESSIE", "AMALIA", "SAVANNAH", "ANASTASIA", "VILMA", "NATALIA", "ROSELLA", "LYNNETTE", "CORINA", "ALFREDA", "LEANNA", "CAREY", "AMPARO", "COLEEN", "TAMRA", "AISHA", "WILDA", "KARYN", "CHERRY", "QUEEN", "MAURA", "MAI", "EVANGELINA", "ROSANNA", "HALLIE", "ERNA", "ENID", "MARIANA", "LACY", "JULIET", "JACKLYN", "FREIDA", "MADELEINE", "MARA", "HESTER", "CATHRYN", "LELIA", "CASANDRA", "BRIDGETT", "ANGELITA", "JANNIE", "DIONNE", "ANNMARIE", "KATINA", "BERYL", "PHOEBE", "MILLICENT", "KATHERYN", "DIANN", "CARISSA", "MARYELLEN", "LIZ", "LAURI", "HELGA", "GILDA", "ADRIAN", "RHEA", "MARQUITA", "HOLLIE", "TISHA", "TAMERA", "ANGELIQUE", "FRANCESCA", "BRITNEY", "KAITLIN", "LOLITA", "FLORINE", "ROWENA", "REYNA", "TWILA", "FANNY", "JANELL", "INES", "CONCETTA", "BERTIE", "ALBA", "BRIGITTE", "ALYSON", "VONDA", "PANSY", "ELBA", "NOELLE", "LETITIA", "KITTY", "DEANN", "BRANDIE", "LOUELLA", "LETA", "FELECIA", "SHARLENE", "LESA", "BEVERLEY", "ROBERT", "ISABELLA", "HERMINIA", "TERRA", "CELINA", "TORI", "OCTAVIA", "JADE", "DENICE", "GERMAINE", "SIERRA", "MICHELL", "CORTNEY", "NELLY", "DORETHA", "SYDNEY", "DEIDRA", "MONIKA", "LASHONDA", "JUDI", "CHELSEY", "ANTIONETTE", "MARGOT", "BOBBY", "ADELAIDE", "NAN", "LEEANN", "ELISHA", "DESSIE", "LIBBY", "KATHI", "GAYLA", "LATANYA", "MINA", "MELLISA", "KIMBERLEE", "JASMIN", "RENAE", "ZELDA", "ELDA", "MA", "JUSTINA", "GUSSIE", "EMILIE", "CAMILLA", "ABBIE", "ROCIO", "KAITLYN", "JESSE", "EDYTHE", "ASHLEIGH", "SELINA", "LAKESHA", "GERI", "ALLENE", "PAMALA", "MICHAELA", "DAYNA", "CARYN", "ROSALIA", "SUN", "JACQULINE", "REBECA", "MARYBETH", "KRYSTLE", "IOLA", "DOTTIE", "BENNIE", "BELLE", "AUBREY", "GRISELDA", "ERNESTINA", "ELIDA", "ADRIANNE", "DEMETRIA", "DELMA", "CHONG", "JAQUELINE", "DESTINY", "ARLEEN", "VIRGINA", "RETHA", "FATIMA", "TILLIE", "ELEANORE", "CARI", "TREVA", "BIRDIE", "WILHELMINA", "ROSALEE", "MAURINE", "LATRICE", "YONG", "JENA", "TARYN", "ELIA", "DEBBY", "MAUDIE", "JEANNA", "DELILAH", "CATRINA", "SHONDA", "HORTENCIA", "THEODORA", "TERESITA", "ROBBIN", "DANETTE", "MARYJANE", "FREDDIE", "DELPHINE", "BRIANNE", "NILDA", "DANNA", "CINDI", "BESS", "IONA", "HANNA", "ARIEL", "WINONA", "VIDA", "ROSITA", "MARIANNA", "WILLIAM", "RACHEAL", "GUILLERMINA", "ELOISA", "CELESTINE", "CAREN", "MALISSA", "LONA", "CHANTEL", "SHELLIE", "MARISELA", "LEORA", "AGATHA", "SOLEDAD", "MIGDALIA", "IVETTE", "CHRISTEN", "ATHENA", "JANEL", "CHLOE", "VEDA", "PATTIE", "TESSIE", "TERA", "MARILYNN", "LUCRETIA", "KARRIE", "DINAH", "DANIELA", "ALECIA", "ADELINA", "VERNICE", "SHIELA", "PORTIA", "MERRY", "LASHAWN", "DEVON", "DARA", "TAWANA", "OMA", "VERDA", "CHRISTIN", "ALENE", "ZELLA", "SANDI", "RAFAELA", "MAYA", "KIRA", "CANDIDA", "ALVINA", "SUZAN", "SHAYLA", "LYN", "LETTIE", "ALVA", "SAMATHA", "ORALIA", "MATILDE", "MADONNA", "LARISSA", "VESTA", "RENITA", "INDIA", "DELOIS", "SHANDA", "PHILLIS", "LORRI", "ERLINDA", "CRUZ", "CATHRINE", "BARB", "ZOE", "ISABELL", "IONE", "GISELA", "CHARLIE", "VALENCIA", "ROXANNA", "MAYME", "KISHA", "ELLIE", "MELLISSA", "DORRIS", "DALIA", "BELLA", "ANNETTA", "ZOILA", "RETA", "REINA", "LAURETTA", "KYLIE", "CHRISTAL", "PILAR", "CHARLA", "ELISSA", "TIFFANI", "TANA", "PAULINA", "LEOTA", "BREANNA", "JAYME", "CARMEL", "VERNELL", "TOMASA", "MANDI", "DOMINGA", "SANTA", "MELODIE", "LURA", "ALEXA", "TAMELA", "RYAN", "MIRNA", "KERRIE", "VENUS", "NOEL", "FELICITA", "CRISTY", "CARMELITA", "BERNIECE", "ANNEMARIE", "TIARA", "ROSEANNE", "MISSY", "CORI", "ROXANA", "PRICILLA", "KRISTAL", "JUNG", "ELYSE", "HAYDEE", "ALETHA", "BETTINA", "MARGE", "GILLIAN", "FILOMENA", "CHARLES", "ZENAIDA", "HARRIETTE", "CARIDAD", "VADA", "UNA", "ARETHA", "PEARLINE", "MARJORY", "MARCELA", "FLOR", "EVETTE", "ELOUISE", "ALINA", "TRINIDAD", "DAVID", "DAMARIS", "CATHARINE", "CARROLL", "BELVA", "NAKIA", "MARLENA", "LUANNE", "LORINE", "KARON", "DORENE", "DANITA", "BRENNA", "TATIANA", "SAMMIE", "LOUANN", "LOREN", "JULIANNA", "ANDRIA", "PHILOMENA", "LUCILA", "LEONORA", "DOVIE", "ROMONA", "MIMI", "JACQUELIN", "GAYE", "TONJA", "MISTI", "JOE", "GENE", "CHASTITY", "STACIA", "ROXANN", "MICAELA", "NIKITA", "MEI", "VELDA", "MARLYS", "JOHNNA", "AURA", "LAVERN", "IVONNE", "HAYLEY", "NICKI", "MAJORIE", "HERLINDA", "GEORGE", "ALPHA", "YADIRA", "PERLA", "GREGORIA", "DANIEL", "ANTONETTE", "SHELLI", "MOZELLE", "MARIAH", "JOELLE", "CORDELIA", "JOSETTE", "CHIQUITA", "TRISTA", "LOUIS", "LAQUITA", "GEORGIANA", "CANDI", "SHANON", "LONNIE", "HILDEGARD", "CECIL", "VALENTINA", "STEPHANY", "MAGDA", "KAROL", "GERRY", "GABRIELLA", "TIANA", "ROMA", "RICHELLE", "RAY", "PRINCESS", "OLETA", "JACQUE", "IDELLA", "ALAINA", "SUZANNA", "JOVITA", "BLAIR", "TOSHA", "RAVEN", "NEREIDA", "MARLYN", "KYLA", "JOSEPH", "DELFINA", "TENA", "STEPHENIE", "SABINA", "NATHALIE", "MARCELLE", "GERTIE", "DARLEEN", "THEA", "SHARONDA", "SHANTEL", "BELEN", "VENESSA", "ROSALINA", "ONA", "GENOVEVA", "COREY", "CLEMENTINE", "ROSALBA", "RENATE", "RENATA", "MI", "IVORY", "GEORGIANNA", "FLOY", "DORCAS", "ARIANA", "TYRA", "THEDA", "MARIAM", "JULI", "JESICA", "DONNIE", "VIKKI", "VERLA", "ROSELYN", "MELVINA", "JANNETTE", "GINNY", "DEBRAH", "CORRIE", "ASIA", "VIOLETA", "MYRTIS", "LATRICIA", "COLLETTE", "CHARLEEN", "ANISSA", "VIVIANA", "TWYLA", "PRECIOUS", "NEDRA", "LATONIA", "LAN", "HELLEN", "FABIOLA", "ANNAMARIE", "ADELL", "SHARYN", "CHANTAL", "NIKI", "MAUD", "LIZETTE", "LINDY", "KIA", "KESHA", "JEANA", "DANELLE", "CHARLINE", "CHANEL", "CARROL", "VALORIE", "LIA", "DORTHA", "CRISTAL", "SUNNY", "LEONE", "LEILANI", "GERRI", "DEBI", "ANDRA", "KESHIA", "IMA", "EULALIA", "EASTER", "DULCE", "NATIVIDAD", "LINNIE", "KAMI", "GEORGIE", "CATINA", "BROOK", "ALDA", "WINNIFRED", "SHARLA", "RUTHANN", "MEAGHAN", "MAGDALENE", "LISSETTE", "ADELAIDA", "VENITA", "TRENA", "SHIRLENE", "SHAMEKA", "ELIZEBETH", "DIAN", "SHANTA", "MICKEY", "LATOSHA", "CARLOTTA", "WINDY", "SOON", "ROSINA", "MARIANN", "LEISA", "JONNIE", "DAWNA", "CATHIE", "BILLY", "ASTRID", "SIDNEY", "LAUREEN", "JANEEN", "HOLLI", "FAWN", "VICKEY", "TERESSA", "SHANTE", "RUBYE", "MARCELINA", "CHANDA", "CARY", "TERESE", "SCARLETT", "MARTY", "MARNIE", "LULU", "LISETTE", "JENIFFER", "ELENOR", "DORINDA", "DONITA", "CARMAN", "BERNITA", "ALTAGRACIA", "ALETA", "ADRIANNA", "ZORAIDA", "RONNIE", "NICOLA", "LYNDSEY", "KENDALL", "JANINA", "CHRISSY", "AMI", "STARLA", "PHYLIS", "PHUONG", "KYRA", "CHARISSE", "BLANCH", "SANJUANITA", "RONA", "NANCI", "MARILEE", "MARANDA", "CORY", "BRIGETTE", "SANJUANA", "MARITA", "KASSANDRA", "JOYCELYN", "IRA", "FELIPA", "CHELSIE", "BONNY", "MIREYA", "LORENZA", "KYONG", "ILEANA", "CANDELARIA", "TONY", "TOBY", "SHERIE", "OK", "MARK", "LUCIE", "LEATRICE", "LAKESHIA", "GERDA", "EDIE", "BAMBI", "MARYLIN", "LAVON", "HORTENSE", "GARNET", "EVIE", "TRESSA", "SHAYNA", "LAVINA", "KYUNG", "JEANETTA", "SHERRILL", "SHARA", "PHYLISS", "MITTIE", "ANABEL", "ALESIA", "THUY", "TAWANDA", "RICHARD", "JOANIE", "TIFFANIE", "LASHANDA", "KARISSA", "ENRIQUETA", "DARIA", "DANIELLA", "CORINNA", "ALANNA", "ABBEY", "ROXANE", "ROSEANNA", "MAGNOLIA", "LIDA", "KYLE", "JOELLEN", "ERA", "CORAL", "CARLEEN", "TRESA", "PEGGIE", "NOVELLA", "NILA", "MAYBELLE", "JENELLE", "CARINA", "NOVA", "MELINA", "MARQUERITE", "MARGARETTE", "JOSEPHINA", "EVONNE", "DEVIN", "CINTHIA", "ALBINA", "TOYA", "TAWNYA", "SHERITA", "SANTOS", "MYRIAM", "LIZABETH", "LISE", "KEELY", "JENNI", "GISELLE", "CHERYLE", "ARDITH", "ARDIS", "ALESHA", "ADRIANE", "SHAINA", "LINNEA", "KAROLYN", "HONG", "FLORIDA", "FELISHA", "DORI", "DARCI", "ARTIE", "ARMIDA", "ZOLA", "XIOMARA", "VERGIE", "SHAMIKA", "NENA", "NANNETTE", "MAXIE", "LOVIE", "JEANE", "JAIMIE", "INGE", "FARRAH", "ELAINA", "CAITLYN", "STARR", "FELICITAS", "CHERLY", "CARYL", "YOLONDA", "YASMIN", "TEENA", "PRUDENCE", "PENNIE", "NYDIA", "MACKENZIE", "ORPHA", "MARVEL", "LIZBETH", "LAURETTE", "JERRIE", "HERMELINDA", "CAROLEE", "TIERRA", "MIRIAN", "META", "MELONY", "KORI", "JENNETTE", "JAMILA", "ENA", "ANH", "YOSHIKO", "SUSANNAH", "SALINA", "RHIANNON", "JOLEEN", "CRISTINE", "ASHTON", "ARACELY", "TOMEKA", "SHALONDA", "MARTI", "LACIE", "KALA", "JADA", "ILSE", "HAILEY", "BRITTANI", "ZONA", "SYBLE", "SHERRYL", "RANDY", "NIDIA", "MARLO", "KANDICE", "KANDI", "DEB", "DEAN", "AMERICA", "ALYCIA", "TOMMY", "RONNA", "NORENE", "MERCY", "JOSE", "INGEBORG", "GIOVANNA", "GEMMA", "CHRISTEL", "AUDRY", "ZORA", "VITA", "VAN", "TRISH", "STEPHAINE", "SHIRLEE", "SHANIKA", "MELONIE", "MAZIE", "JAZMIN", "INGA", "HOA", "HETTIE", "GERALYN", "FONDA", "ESTRELLA", "ADELLA", "SU", "SARITA", "RINA", "MILISSA", "MARIBETH", "GOLDA", "EVON", "ETHELYN", "ENEDINA", "CHERISE", "CHANA", "VELVA", "TAWANNA", "SADE", "MIRTA", "LI", "KARIE", "JACINTA", "ELNA", "DAVINA", "CIERRA", "ASHLIE", "ALBERTHA", "TANESHA", "STEPHANI", "NELLE", "MINDI", "LU", "LORINDA", "LARUE", "FLORENE", "DEMETRA", "DEDRA", "CIARA", "CHANTELLE", "ASHLY", "SUZY", "ROSALVA", "NOELIA", "LYDA", "LEATHA", "KRYSTYNA", "KRISTAN", "KARRI", "DARLINE", "DARCIE", "CINDA", "CHEYENNE", "CHERRIE", "AWILDA", "ALMEDA", "ROLANDA", "LANETTE", "JERILYN", "GISELE", "EVALYN", "CYNDI", "CLETA", "CARIN", "ZINA", "ZENA", "VELIA", "TANIKA", "PAUL", "CHARISSA", "THOMAS", "TALIA", "MARGARETE", "LAVONDA", "KAYLEE", "KATHLENE", "JONNA", "IRENA", "ILONA", "IDALIA", "CANDIS", "CANDANCE", "BRANDEE", "ANITRA", "ALIDA", "SIGRID", "NICOLETTE", "MARYJO", "LINETTE", "HEDWIG", "CHRISTIANA", "CASSIDY", "ALEXIA", "TRESSIE", "MODESTA", "LUPITA", "LITA", "GLADIS", "EVELIA", "DAVIDA", "CHERRI", "CECILY", "ASHELY", "ANNABEL", "AGUSTINA", "WANITA", "SHIRLY", "ROSAURA", "HULDA", "EUN", "BAILEY", "YETTA", "VERONA", "THOMASINA", "SIBYL", "SHANNAN", "MECHELLE", "LUE", "LEANDRA", "LANI", "KYLEE", "KANDY", "JOLYNN", "FERNE", "EBONI", "CORENE", "ALYSIA", "ZULA", "NADA", "MOIRA", "LYNDSAY", "LORRETTA", "JUAN", "JAMMIE", "HORTENSIA", "GAYNELL", "CAMERON", "ADRIA", "VINA", "VICENTA", "TANGELA", "STEPHINE", "NORINE", "NELLA", "LIANA", "LESLEE", "KIMBERELY", "ILIANA", "GLORY", "FELICA", "EMOGENE", "ELFRIEDE", "EDEN", "EARTHA", "CARMA", "BEA", "OCIE", "MARRY", "LENNIE", "KIARA", "JACALYN", "CARLOTA", "ARIELLE", "YU", "STAR", "OTILIA", "KIRSTIN", "KACEY", "JOHNETTA", "JOEY", "JOETTA", "JERALDINE", "JAUNITA", "ELANA", "DORTHEA", "CAMI", "AMADA", "ADELIA", "VERNITA", "TAMAR", "SIOBHAN", "RENEA", "RASHIDA", "OUIDA", "ODELL", "NILSA", "MERYL", "KRISTYN", "JULIETA", "DANICA", "BREANNE", "AUREA", "ANGLEA", "SHERRON", "ODETTE", "MALIA", "LORELEI", "LIN", "LEESA", "KENNA", "KATHLYN", "FIONA", "CHARLETTE", "SUZIE", "SHANTELL", "SABRA", "RACQUEL", "MYONG", "MIRA", "MARTINE", "LUCIENNE", "LAVADA", "JULIANN", "JOHNIE", "ELVERA", "DELPHIA", "CLAIR", "CHRISTIANE", "CHAROLETTE", "CARRI", "AUGUSTINE", "ASHA", "ANGELLA", "PAOLA", "NINFA", "LEDA", "LAI", "EDA", "SUNSHINE", "STEFANI", "SHANELL", "PALMA", "MACHELLE", "LISSA", "KECIA", "KATHRYNE", "KARLENE", "JULISSA", "JETTIE", "JENNIFFER", "HUI", "CORRINA", "CHRISTOPHER", "CAROLANN", "ALENA", "TESS", "ROSARIA", "MYRTICE", "MARYLEE", "LIANE", "KENYATTA", "JUDIE", "JANEY", "IN", "ELMIRA", "ELDORA", "DENNA", "CRISTI", "CATHI", "ZAIDA", "VONNIE", "VIVA", "VERNIE", "ROSALINE", "MARIELA", "LUCIANA", "LESLI", "KARAN", "FELICE", "DENEEN", "ADINA", "WYNONA", "TARSHA", "SHERON", "SHASTA", "SHANITA", "SHANI", "SHANDRA", "RANDA", "PINKIE", "PARIS", "NELIDA", "MARILOU", "LYLA", "LAURENE", "LACI", "JOI", "JANENE", "DOROTHA", "DANIELE", "DANI", "CAROLYNN", "CARLYN", "BERENICE", "AYESHA", "ANNELIESE", "ALETHEA", "THERSA", "TAMIKO", "RUFINA", "OLIVA", "MOZELL", "MARYLYN", "MADISON", "KRISTIAN", "KATHYRN", "KASANDRA", "KANDACE", "JANAE", "GABRIEL", "DOMENICA", "DEBBRA", "DANNIELLE", "CHUN", "BUFFY", "BARBIE", "ARCELIA", "AJA", "ZENOBIA", "SHAREN", "SHAREE", "PATRICK", "PAGE", "MY", "LAVINIA", "KUM", "KACIE", "JACKELINE", "HUONG", "FELISA", "EMELIA", "ELEANORA", "CYTHIA", "CRISTIN", "CLYDE", "CLARIBEL", "CARON", "ANASTACIA", "ZULMA", "ZANDRA", "YOKO", "TENISHA", "SUSANN", "SHERILYN", "SHAY", "SHAWANDA", "SABINE", "ROMANA", "MATHILDA", "LINSEY", "KEIKO", "JOANA", "ISELA", "GRETTA", "GEORGETTA", "EUGENIE", "DUSTY", "DESIRAE", "DELORA", "CORAZON", "ANTONINA", "ANIKA", "WILLENE", "TRACEE", "TAMATHA", "REGAN", "NICHELLE", "MICKIE", "MAEGAN", "LUANA", "LANITA", "KELSIE", "EDELMIRA", "BREE", "AFTON", "TEODORA", "TAMIE", "SHENA", "MEG", "LINH", "KELI", "KACI", "DANYELLE", "BRITT", "ARLETTE", "ALBERTINE", "ADELLE", "TIFFINY", "STORMY", "SIMONA", "NUMBERS", "NICOLASA", "NICHOL", "NIA", "NAKISHA", "MEE", "MAIRA", "LOREEN", "KIZZY", "JOHNNY", "JAY", "FALLON", "CHRISTENE", "BOBBYE", "ANTHONY", "YING", "VINCENZA", "TANJA", "RUBIE", "RONI", "QUEENIE", "MARGARETT", "KIMBERLI", "IRMGARD", "IDELL", "HILMA", "EVELINA", "ESTA", "EMILEE", "DENNISE", "DANIA", "CARL", "CARIE", "ANTONIO", "WAI", "SANG", "RISA", "RIKKI", "PARTICIA", "MUI", "MASAKO", "MARIO", "LUVENIA", "LOREE", "LONI", "LIEN", "KEVIN", "GIGI", "FLORENCIA", "DORIAN", "DENITA", "DALLAS", "CHI", "BILLYE", "ALEXANDER", "TOMIKA", "SHARITA", "RANA", "NIKOLE", "NEOMA", "MARGARITE", "MADALYN", "LUCINA", "LAILA", "KALI", "JENETTE", "GABRIELE", "EVELYNE", "ELENORA", "CLEMENTINA", "ALEJANDRINA", "ZULEMA", "VIOLETTE", "VANNESSA", "THRESA", "RETTA", "PIA", "PATIENCE", "NOELLA", "NICKIE", "JONELL", "DELTA", "CHUNG", "CHAYA", "CAMELIA", "BETHEL", "ANYA", "ANDREW", "THANH", "SUZANN", "SPRING", "SHU", "MILA", "LILLA", "LAVERNA", "KEESHA", "KATTIE", "GIA", "GEORGENE", "EVELINE", "ESTELL", "ELIZBETH", "VIVIENNE", "VALLIE", "TRUDIE", "STEPHANE", "MICHEL", "MAGALY", "MADIE", "KENYETTA", "KARREN", "JANETTA", "HERMINE", "HARMONY", "DRUCILLA", "DEBBI", "CELESTINA", "CANDIE", "BRITNI", "BECKIE", "AMINA", "ZITA", "YUN", "YOLANDE", "VIVIEN", "VERNETTA", "TRUDI", "SOMMER", "PEARLE", "PATRINA", "OSSIE", "NICOLLE", "LOYCE", "LETTY", "LARISA", "KATHARINA", "JOSELYN", "JONELLE", "JENELL", "IESHA", "HEIDE", "FLORINDA", "FLORENTINA", "FLO", "ELODIA", "DORINE", "BRUNILDA", "BRIGID", "ASHLI", "ARDELLA", "TWANA", "THU", "TARAH", "SUNG", "SHEA", "SHAVON", "SHANE", "SERINA", "RAYNA", "RAMONITA", "NGA", "MARGURITE", "LUCRECIA", "KOURTNEY", "KATI", "JESUS", "JESENIA", "DIAMOND", "CRISTA", "AYANA", "ALICA", "ALIA", "VINNIE", "SUELLEN", "ROMELIA", "RACHELL", "PIPER", "OLYMPIA", "MICHIKO", "KATHALEEN", "JOLIE", "JESSI", "JANESSA", "HANA", "HA", "ELEASE", "CARLETTA", "BRITANY", "SHONA", "SALOME", "ROSAMOND", "REGENA", "RAINA", "NGOC", "NELIA", "LOUVENIA", "LESIA", "LATRINA", "LATICIA", "LARHONDA", "JINA", "JACKI", "HOLLIS", "HOLLEY", "EMMY", "DEEANN", "CORETTA", "ARNETTA", "VELVET", "THALIA", "SHANICE", "NETA", "MIKKI", "MICKI", "LONNA", "LEANA", "LASHUNDA", "KILEY", "JOYE", "JACQULYN", "IGNACIA", "HYUN", "HIROKO", "HENRY", "HENRIETTE", "ELAYNE", "DELINDA", "DARNELL", "DAHLIA", "COREEN", "CONSUELA", "CONCHITA", "CELINE", "BABETTE", "AYANNA", "ANETTE", "ALBERTINA", "SKYE", "SHAWNEE", "SHANEKA", "QUIANA", "PAMELIA", "MIN", "MERRI", "MERLENE", "MARGIT", "KIESHA", "KIERA", "KAYLENE", "JODEE", "JENISE", "ERLENE", "EMMIE", "ELSE", "DARYL", "DALILA", "DAISEY", "CODY", "CASIE", "BELIA", "BABARA", "VERSIE", "VANESA", "SHELBA", "SHAWNDA", "SAM", "NORMAN", "NIKIA", "NAOMA", "MARNA", "MARGERET", "MADALINE", "LAWANA", "KINDRA", "JUTTA", "JAZMINE", "JANETT", "HANNELORE", "GLENDORA", "GERTRUD", "GARNETT", "FREEDA", "FREDERICA", "FLORANCE", "FLAVIA", "DENNIS", "CARLINE", "BEVERLEE", "ANJANETTE", "VALDA", "TRINITY", "TAMALA", "STEVIE", "SHONNA", "SHA", "SARINA", "ONEIDA", "MICAH", "MERILYN", "MARLEEN", "LURLINE", "LENNA", "KATHERIN", "JIN", "JENI", "HAE", "GRACIA", "GLADY", "FARAH", "ERIC", "ENOLA", "EMA", "DOMINQUE", "DEVONA", "DELANA", "CECILA", "CAPRICE", "ALYSHA", "ALI", "ALETHIA", "VENA", "THERESIA", "TAWNY", "SONG", "SHAKIRA", "SAMARA", "SACHIKO", "RACHELE", "PAMELLA", "NICKY", "MARNI", "MARIEL", "MAREN", "MALISA", "LIGIA", "LERA", "LATORIA", "LARAE", "KIMBER", "KATHERN", "KAREY", "JENNEFER", "JANETH", "HALINA", "FREDIA", "DELISA", "DEBROAH", "CIERA", "CHIN", "ANGELIKA", "ANDREE", "ALTHA", "YEN", "VIVAN", "TERRESA", "TANNA", "SUK", "SUDIE", "SOO", "SIGNE", "SALENA", "RONNI", "REBBECCA", "MYRTIE", "MCKENZIE", "MALIKA", "MAIDA", "LOAN", "LEONARDA", "KAYLEIGH", "FRANCE", "ETHYL", "ELLYN", "DAYLE", "CAMMIE", "BRITTNI", "BIRGIT", "AVELINA", "ASUNCION", "ARIANNA", "AKIKO", "VENICE", "TYESHA", "TONIE", "TIESHA", "TAKISHA", "STEFFANIE", "SINDY", "SANTANA", "MEGHANN", "MANDA", "MACIE", "LADY", "KELLYE", "KELLEE", "JOSLYN", "JASON", "INGER", "INDIRA", "GLINDA", "GLENNIS", "FERNANDA", "FAUSTINA", "ENEIDA", "ELICIA", "DOT", "DIGNA", "DELL", "ARLETTA", "ANDRE", "WILLIA", "TAMMARA", "TABETHA", "SHERRELL", "SARI", "REFUGIO", "REBBECA", "PAULETTA", "NIEVES", "NATOSHA", "NAKITA", "MAMMIE", "KENISHA", "KAZUKO", "KASSIE", "GARY", "EARLEAN", "DAPHINE", "CORLISS", "CLOTILDE", "CAROLYNE", "BERNETTA", "AUGUSTINA", "AUDREA", "ANNIS", "ANNABELL", "YAN", "TENNILLE", "TAMICA", "SELENE", "SEAN", "ROSANA", "REGENIA", "QIANA", "MARKITA", "MACY", "LEEANNE", "LAURINE", "KYM", "JESSENIA", "JANITA", "GEORGINE", "GENIE", "EMIKO", "ELVIE", "DEANDRA", "DAGMAR", "CORIE", "COLLEN", "CHERISH", "ROMAINE", "PORSHA", "PEARLENE", "MICHELINE", "MERNA", "MARGORIE", "MARGARETTA", "LORE", "KENNETH", "JENINE", "HERMINA", "FREDERICKA", "ELKE", "DRUSILLA", "DORATHY", "DIONE", "DESIRE", "CELENA", "BRIGIDA", "ANGELES", "ALLEGRA", "THEO", "TAMEKIA", "SYNTHIA", "STEPHEN", "SOOK", "SLYVIA", "ROSANN", "REATHA", "RAYE", "MARQUETTA", "MARGART", "LING", "LAYLA", "KYMBERLY", "KIANA", "KAYLEEN", "KATLYN", "KARMEN", "JOELLA", "IRINA", "EMELDA", "ELENI", "DETRA", "CLEMMIE", "CHERYLL", "CHANTELL", "CATHEY", "ARNITA", "ARLA", "ANGLE", "ANGELIC", "ALYSE", "ZOFIA", "THOMASINE", "TENNIE", "SON", "SHERLY", "SHERLEY", "SHARYL", "REMEDIOS", "PETRINA", "NICKOLE", "MYUNG", "MYRLE", "MOZELLA", "LOUANNE", "LISHA", "LATIA", "LANE", "KRYSTA", "JULIENNE", "JOEL", "JEANENE", "JACQUALINE", "ISAURA", "GWENDA", "EARLEEN", "DONALD", "CLEOPATRA", "CARLIE", "AUDIE", "ANTONIETTA", "ALISE", "ALEX", "VERDELL", "VAL", "TYLER", "TOMOKO", "THAO", "TALISHA", "STEVEN", "SO", "SHEMIKA", "SHAUN", "SCARLET", "SAVANNA", "SANTINA", "ROSIA", "RAEANN", "ODILIA", "NANA", "MINNA", "MAGAN", "LYNELLE", "LE", "KARMA", "JOEANN", "IVANA", "INELL", "ILANA", "HYE", "HONEY", "HEE", "GUDRUN", "FRANK", "DREAMA", "CRISSY", "CHANTE", "CARMELINA", "ARVILLA", "ARTHUR", "ANNAMAE", "ALVERA", "ALEIDA", "AARON", "YEE", "YANIRA", "VANDA", "TIANNA", "TAM", "STEFANIA", "SHIRA", "PERRY", "NICOL", "NANCIE", "MONSERRATE", "MINH", "MELYNDA", "MELANY", "MATTHEW", "LOVELLA", "LAURE", "KIRBY", "KACY", "JACQUELYNN", "HYON", "GERTHA", "FRANCISCO", "ELIANA", "CHRISTENA", "CHRISTEEN", "CHARISE", "CATERINA", "CARLEY", "CANDYCE", "ARLENA", "AMMIE", "YANG", "WILLETTE", "VANITA", "TUYET", "TINY", "SYREETA", "SILVA", "SCOTT", "RONALD", "PENNEY", "NYLA", "MICHAL", "MAURICE", "MARYAM", "MARYA", "MAGEN", "LUDIE", "LOMA", "LIVIA", "LANELL", "KIMBERLIE", "JULEE", "DONETTA", "DIEDRA", "DENISHA", "DEANE", "DAWNE", "CLARINE", "CHERRYL", "BRONWYN", "BRANDON", "ALLA", "VALERY", "TONDA", "SUEANN", "SORAYA", "SHOSHANA", "SHELA", "SHARLEEN", "SHANELLE", "NERISSA", "MICHEAL", "MERIDITH", "MELLIE", "MAYE", "MAPLE", "MAGARET", "LUIS", "LILI", "LEONILA", "LEONIE", "LEEANNA", "LAVONIA", "LAVERA", "KRISTEL", "KATHEY", "KATHE", "JUSTIN", "JULIAN", "JIMMY", "JANN", "ILDA", "HILDRED", "HILDEGARDE", "GENIA", "FUMIKO", "EVELIN", "ERMELINDA", "ELLY", "DUNG", "DOLORIS", "DIONNA", "DANAE", "BERNEICE", "ANNICE", "ALIX", "VERENA", "VERDIE", "TRISTAN", "SHAWNNA", "SHAWANA", "SHAUNNA", "ROZELLA", "RANDEE", "RANAE", "MILAGRO", "LYNELL", "LUISE", "LOUIE", "LOIDA", "LISBETH", "KARLEEN", "JUNITA", "JONA", "ISIS", "HYACINTH", "HEDY", "GWENN", "ETHELENE", "ERLINE", "EDWARD", "DONYA", "DOMONIQUE", "DELICIA", "DANNETTE", "CICELY", "BRANDA", "BLYTHE", "BETHANN", "ASHLYN", "ANNALEE", "ALLINE", "YUKO", "VELLA", "TRANG", "TOWANDA", "TESHA", "SHERLYN", "NARCISA", "MIGUELINA", "MERI", "MAYBELL", "MARLANA", "MARGUERITA", "MADLYN", "LUNA", "LORY", "LORIANN", "LIBERTY", "LEONORE", "LEIGHANN", "LAURICE", "LATESHA", "LARONDA", "KATRICE", "KASIE", "KARL", "KALEY", "JADWIGA", "GLENNIE", "GEARLDINE", "FRANCINA", "EPIFANIA", "DYAN", "DORIE", "DIEDRE", "DENESE", "DEMETRICE", "DELENA", "DARBY", "CRISTIE", "CLEORA", "CATARINA", "CARISA", "BERNIE", "BARBERA", "ALMETA", "TRULA", "TEREASA", "SOLANGE", "SHEILAH", "SHAVONNE", "SANORA", "ROCHELL", "MATHILDE", "MARGARETA", "MAIA", "LYNSEY", "LAWANNA", "LAUNA", "KENA", "KEENA", "KATIA", "JAMEY", "GLYNDA", "GAYLENE", "ELVINA", "ELANOR", "DANUTA", "DANIKA", "CRISTEN", "CORDIE", "COLETTA", "CLARITA", "CARMON", "BRYNN", "AZUCENA", "AUNDREA", "ANGELE", "YI", "WALTER", "VERLIE", "VERLENE", "TAMESHA", "SILVANA", "SEBRINA", "SAMIRA", "REDA", "RAYLENE", "PENNI", "PANDORA", "NORAH", "NOMA", "MIREILLE", "MELISSIA", "MARYALICE", "LARAINE", "KIMBERY", "KARYL", "KARINE", "KAM", "JOLANDA", "JOHANA", "JESUSA", "JALEESA", "JAE", "JACQUELYNE", "IRISH", "ILUMINADA", "HILARIA", "HANH", "GENNIE", "FRANCIE", "FLORETTA", "EXIE", "EDDA", "DREMA", "DELPHA", "BEV", "BARBAR", "ASSUNTA", "ARDELL", "ANNALISA", "ALISIA", "YUKIKO", "YOLANDO", "WONDA", "WEI", "WALTRAUD", "VETA", "TEQUILA", "TEMEKA", "TAMEIKA", "SHIRLEEN", "SHENITA", "PIEDAD", "OZELLA", "MIRTHA", "MARILU", "KIMIKO", "JULIANE", "JENICE", "JEN", "JANAY", "JACQUILINE", "HILDE", "FE", "FAE", "EVAN", "EUGENE", "ELOIS", "ECHO", "DEVORAH", "CHAU", "BRINDA", "BETSEY", "ARMINDA", "ARACELIS", "APRYL", "ANNETT", "ALISHIA", "VEOLA", "USHA", "TOSHIKO", "THEOLA", "TASHIA", "TALITHA", "SHERY", "RUDY", "RENETTA", "REIKO", "RASHEEDA", "OMEGA", "OBDULIA", "MIKA", "MELAINE", "MEGGAN", "MARTIN", "MARLEN", "MARGET", "MARCELINE", "MANA", "MAGDALEN", "LIBRADA", "LEZLIE", "LEXIE", "LATASHIA", "LASANDRA", "KELLE", "ISIDRA", "ISA", "INOCENCIA", "GWYN", "FRANCOISE", "ERMINIA", "ERINN", "DIMPLE", "DEVORA", "CRISELDA", "ARMANDA", "ARIE", "ARIANE", "ANGELO", "ANGELENA", "ALLEN", "ALIZA", "ADRIENE", "ADALINE", "XOCHITL", "TWANNA", "TRAN", "TOMIKO", "TAMISHA", "TAISHA", "SUSY", "SIU", "RUTHA", "ROXY", "RHONA", "RAYMOND", "OTHA", "NORIKO", "NATASHIA", "MERRIE", "MELVIN", "MARINDA", "MARIKO", "MARGERT", "LORIS", "LIZZETTE", "LEISHA", "KAILA", "KA", "JOANNIE", "JERRICA", "JENE", "JANNET", "JANEE", "JACINDA", "HERTA", "ELENORE", "DORETTA", "DELAINE", "DANIELL", "CLAUDIE", "CHINA", "BRITTA", "APOLONIA", "AMBERLY", "ALEASE", "YURI", "YUK", "WEN", "WANETA", "UTE", "TOMI", "SHARRI", "SANDIE", "ROSELLE", "REYNALDA", "RAGUEL", "PHYLICIA", "PATRIA", "OLIMPIA", "ODELIA", "MITZIE", "MITCHELL", "MISS", "MINDA", "MIGNON", "MICA", "MENDY", "MARIVEL", "MAILE", "LYNETTA", "LAVETTE", "LAURYN", "LATRISHA", "LAKIESHA", "KIERSTEN", "KARY", "JOSPHINE", "JOLYN", "JETTA", "JANISE", "JACQUIE", "IVELISSE", "GLYNIS", "GIANNA", "GAYNELLE", "EMERALD", "DEMETRIUS", "DANYELL", "DANILLE", "DACIA", "CORALEE", "CHER", "CEOLA", "BRETT", "BELL", "ARIANNE", "ALESHIA", "YUNG", "WILLIEMAE", "TROY", "TRINH", "THORA", "TAI", "SVETLANA", "SHERIKA", "SHEMEKA", "SHAUNDA", "ROSELINE", "RICKI", "MELDA", "MALLIE", "LAVONNA", "LATINA", "LARRY", "LAQUANDA", "LALA", "LACHELLE", "KLARA", "KANDIS", "JOHNA", "JEANMARIE", "JAYE", "HANG", "GRAYCE", "GERTUDE", "EMERITA", "EBONIE", "CLORINDA", "CHING", "CHERY", "CAROLA", "BREANN", "BLOSSOM", "BERNARDINE", "BECKI", "ARLETHA", "ARGELIA", "ARA", "ALITA", "YULANDA", "YON", "YESSENIA", "TOBI", "TASIA", "SYLVIE", "SHIRL", "SHIRELY", "SHERIDAN", "SHELLA", "SHANTELLE", "SACHA", "ROYCE", "REBECKA", "REAGAN", "PROVIDENCIA", "PAULENE", "MISHA", "MIKI", "MARLINE", "MARICA", "LORITA", "LATOYIA", "LASONYA", "KERSTIN", "KENDA", "KEITHA", "KATHRIN", "JAYMIE", "JACK", "GRICELDA", "GINETTE", "ERYN", "ELINA", "ELFRIEDA", "DANYEL", "CHEREE", "CHANELLE", "BARRIE", "AVERY", "AURORE", "ANNAMARIA", "ALLEEN", "AILENE", "AIDE", "YASMINE", "VASHTI", "VALENTINE", "TREASA", "TORY", "TIFFANEY", "SHERYLL", "SHARIE", "SHANAE", "SAU", "RAISA", "PA", "NEDA", "MITSUKO", "MIRELLA", "MILDA", "MARYANNA", "MARAGRET", "MABELLE", "LUETTA", "LORINA", "LETISHA", "LATARSHA", "LANELLE", "LAJUANA", "KRISSY", "KARLY", "KARENA", "JON", "JESSIKA", "JERICA", "JEANELLE", "JANUARY", "JALISA", "JACELYN", "IZOLA", "IVEY", "GREGORY", "EUNA", "ETHA", "DREW", "DOMITILA", "DOMINICA", "DAINA", "CREOLA", "CARLI", "CAMIE", "BUNNY", "BRITTNY", "ASHANTI", "ANISHA", "ALEEN", "ADAH", "YASUKO", "WINTER", "VIKI", "VALRIE", "TONA", "TINISHA", "THI", "TERISA", "TATUM", "TANEKA", "SIMONNE", "SHALANDA", "SERITA", "RESSIE", "REFUGIA", "PAZ", "OLENE", "NA", "MERRILL", "MARGHERITA", "MANDIE", "MAN", "MAIRE", "LYNDIA", "LUCI", "LORRIANE", "LORETA", "LEONIA", "LAVONA", "LASHAWNDA", "LAKIA", "KYOKO", "KRYSTINA", "KRYSTEN", "KENIA", "KELSI", "JUDE", "JEANICE", "ISOBEL", "GEORGIANN", "GENNY", "FELICIDAD", "EILENE", "DEON", "DELOISE", "DEEDEE", "DANNIE", "CONCEPTION", "CLORA", "CHERILYN", "CHANG", "CALANDRA", "BERRY", "ARMANDINA", "ANISA", "ULA", "TIMOTHY", "TIERA", "THERESSA", "STEPHANIA", "SIMA", "SHYLA", "SHONTA", "SHERA", "SHAQUITA", "SHALA", "SAMMY", "ROSSANA", "NOHEMI", "NERY", "MORIAH", "MELITA", "MELIDA", "MELANI", "MARYLYNN", "MARISHA", "MARIETTE", "MALORIE", "MADELENE", "LUDIVINA", "LORIA", "LORETTE", "LORALEE", "LIANNE", "LEON", "LAVENIA", "LAURINDA", "LASHON", "KIT", "KIMI", "KEILA", "KATELYNN", "KAI", "JONE", "JOANE", "JI", "JAYNA", "JANELLA", "JA", "HUE", "HERTHA", "FRANCENE", "ELINORE", "DESPINA", "DELSIE", "DEEDRA", "CLEMENCIA", "CARRY", "CAROLIN", "CARLOS", "BULAH", "BRITTANIE", "BOK", "BLONDELL", "BIBI", "BEAULAH", "BEATA", "ANNITA", "AGRIPINA", "VIRGEN", "VALENE", "UN", "TWANDA", "TOMMYE", "TOI", "TARRA", "TARI", "TAMMERA", "SHAKIA", "SADYE", "RUTHANNE", "ROCHEL", "RIVKA", "PURA", "NENITA", "NATISHA", "MING", "MERRILEE", "MELODEE", "MARVIS", "LUCILLA", "LEENA", "LAVETA", "LARITA", "LANIE", "KEREN", "ILEEN", "GEORGEANN", "GENNA", "GENESIS", "FRIDA", "EWA", "EUFEMIA", "EMELY", "ELA", "EDYTH", "DEONNA", "DEADRA", "DARLENA", "CHANELL", "CHAN", "CATHERN", "CASSONDRA", "CASSAUNDRA", "BERNARDA", "BERNA", "ARLINDA", "ANAMARIA", "ALBERT", "WESLEY", "VERTIE", "VALERI", "TORRI", "TATYANA", "STASIA", "SHERISE", "SHERILL", "SEASON", "SCOTTIE", "SANDA", "RUTHE", "ROSY", "ROBERTO", "ROBBI", "RANEE", "QUYEN", "PEARLY", "PALMIRA", "ONITA", "NISHA", "NIESHA", "NIDA", "NEVADA", "NAM", "MERLYN", "MAYOLA", "MARYLOUISE", "MARYLAND", "MARX", "MARTH", "MARGENE", "MADELAINE", "LONDA", "LEONTINE", "LEOMA", "LEIA", "LAWRENCE", "LAURALEE", "LANORA", "LAKITA", "KIYOKO", "KETURAH", "KATELIN", "KAREEN", "JONIE", "JOHNETTE", "JENEE", "JEANETT", "IZETTA", "HIEDI", "HEIKE", "HASSIE", "HAROLD", "GIUSEPPINA", "GEORGANN", "FIDELA", "FERNANDE", "ELWANDA", "ELLAMAE", "ELIZ", "DUSTI", "DOTTY", "CYNDY", "CORALIE", "CELESTA", "ARGENTINA", "ALVERTA", "XENIA", "WAVA", "VANETTA", "TORRIE", "TASHINA", "TANDY", "TAMBRA", "TAMA", "STEPANIE", "SHILA", "SHAUNTA", "SHARAN", "SHANIQUA", "SHAE", "SETSUKO", "SERAFINA", "SANDEE", "ROSAMARIA", "PRISCILA", "OLINDA", "NADENE", "MUOI", "MICHELINA", "MERCEDEZ", "MARYROSE", "MARIN", "MARCENE", "MAO", "MAGALI", "MAFALDA", "LOGAN", "LINN", "LANNIE", "KAYCE", "KAROLINE", "KAMILAH", "KAMALA", "JUSTA", "JOLINE", "JENNINE", "JACQUETTA", "IRAIDA", "GERALD", "GEORGEANNA", "FRANCHESCA", "FAIRY", "EMELINE", "ELANE", "EHTEL", "EARLIE", "DULCIE", "DALENE", "CRIS", "CLASSIE", "CHERE", "CHARIS", "CAROYLN", "CARMINA", "CARITA", "BRIAN", "BETHANIE", "AYAKO", "ARICA", "AN", "ALYSA", "ALESSANDRA", "AKILAH", "ADRIEN", "ZETTA", "YOULANDA", "YELENA", "YAHAIRA", "XUAN", "WENDOLYN", "VICTOR", "TIJUANA", "TERRELL", "TERINA", "TERESIA", "SUZI", "SUNDAY", "SHERELL", "SHAVONDA", "SHAUNTE", "SHARDA", "SHAKITA", "SENA", "RYANN", "RUBI", "RIVA", "REGINIA", "REA", "RACHAL", "PARTHENIA", "PAMULA", "MONNIE", "MONET", "MICHAELE", "MELIA", "MARINE", "MALKA", "MAISHA", "LISANDRA", "LEO", "LEKISHA", "LEAN", "LAURENCE", "LAKENDRA", "KRYSTIN", "KORTNEY", "KIZZIE", "KITTIE", "KERA", "KENDAL", "KEMBERLY", "KANISHA", "JULENE", "JULE", "JOSHUA", "JOHANNE", "JEFFREY", "JAMEE", "HAN", "HALLEY", "GIDGET", "GALINA", "FREDRICKA", "FLETA", "FATIMAH", "EUSEBIA", "ELZA", "ELEONORE", "DORTHEY", "DORIA", "DONELLA", "DINORAH", "DELORSE", "CLARETHA", "CHRISTINIA", "CHARLYN", "BONG", "BELKIS", "AZZIE", "ANDERA", "AIKO", "ADENA", "YER", "YAJAIRA", "WAN", "VANIA", "ULRIKE", "TOSHIA", "TIFANY", "STEFANY", "SHIZUE", "SHENIKA", "SHAWANNA", "SHAROLYN", "SHARILYN", "SHAQUANA", "SHANTAY", "SEE", "ROZANNE", "ROSELEE", "RICKIE", "REMONA", "REANNA", "RAELENE", "QUINN", "PHUNG", "PETRONILA", "NATACHA", "NANCEY", "MYRL", "MIYOKO", "MIESHA", "MERIDETH", "MARVELLA", "MARQUITTA", "MARHTA", "MARCHELLE", "LIZETH", "LIBBIE", "LAHOMA", "LADAWN", "KINA", "KATHELEEN", "KATHARYN", "KARISA", "KALEIGH", "JUNIE", "JULIEANN", "JOHNSIE", "JANEAN", "JAIMEE", "JACKQUELINE", "HISAKO", "HERMA", "HELAINE", "GWYNETH", "GLENN", "GITA", "EUSTOLIA", "EMELINA", "ELIN", "EDRIS", "DONNETTE", "DONNETTA", "DIERDRE", "DENAE", "DARCEL", "CLAUDE", "CLARISA", "CINDERELLA", "CHIA", "CHARLESETTA", "CHARITA", "CELSA", "CASSY", "CASSI", "CARLEE", "BRUNA", "BRITTANEY", "BRANDE", "BILLI", "BAO", "ANTONETTA", "ANGLA", "ANGELYN", "ANALISA", "ALANE", "WENONA", "WENDIE", "VERONIQUE", "VANNESA", "TOBIE", "TEMPIE", "SUMIKO", "SULEMA", "SPARKLE", "SOMER", "SHEBA", "SHAYNE", "SHARICE", "SHANEL", "SHALON", "SAGE", "ROY", "ROSIO", "ROSELIA", "RENAY", "REMA", "REENA", "PORSCHE", "PING", "PEG", "OZIE", "ORETHA", "ORALEE", "ODA", "NU", "NGAN", "NAKESHA", "MILLY", "MARYBELLE", "MARLIN", "MARIS", "MARGRETT", "MARAGARET", "MANIE", "LURLENE", "LILLIA", "LIESELOTTE", "LAVELLE", "LASHAUNDA", "LAKEESHA", "KEITH", "KAYCEE", "KALYN", "JOYA", "JOETTE", "JENAE", "JANIECE", "ILLA", "GRISEL", "GLAYDS", "GENEVIE", "GALA", "FREDDA", "FRED", "ELMER", "ELEONOR", "DEBERA", "DEANDREA", "DAN", "CORRINNE", "CORDIA", "CONTESSA", "COLENE", "CLEOTILDE", "CHARLOTT", "CHANTAY", "CECILLE", "BEATRIS", "AZALEE", "ARLEAN", "ARDATH", "ANJELICA", "ANJA", "ALFREDIA", "ALEISHA", "ADAM", "ZADA", "YUONNE", "XIAO", "WILLODEAN", "WHITLEY", "VENNIE", "VANNA", "TYISHA", "TOVA", "TORIE", "TONISHA", "TILDA", "TIEN", "TEMPLE", "SIRENA", "SHERRIL", "SHANTI", "SHAN", "SENAIDA", "SAMELLA", "ROBBYN", "RENDA", "REITA", "PHEBE", "PAULITA", "NOBUKO", "NGUYET", "NEOMI", "MOON", "MIKAELA", "MELANIA", "MAXIMINA", "MARG", "MAISIE", "LYNNA", "LILLI", "LAYNE", "LASHAUN", "LAKENYA", "LAEL", "KIRSTIE", "KATHLINE", "KASHA", "KARLYN", "KARIMA", "JOVAN", "JOSEFINE", "JENNELL", "JACQUI", "JACKELYN", "HYO", "HIEN", "GRAZYNA", "FLORRIE", "FLORIA", "ELEONORA", "DWANA", "DORLA", "DONG", "DELMY", "DEJA", "DEDE", "DANN", "CRYSTA", "CLELIA", "CLARIS", "CLARENCE", "CHIEKO", "CHERLYN", "CHERELLE", "CHARMAIN", "CHARA", "CAMMY", "BEE", "ARNETTE", "ARDELLE", "ANNIKA", "AMIEE", "AMEE", "ALLENA", "YVONE", "YUKI", "YOSHIE", "YEVETTE", "YAEL", "WILLETTA", "VONCILE", "VENETTA", "TULA", "TONETTE", "TIMIKA", "TEMIKA", "TELMA", "TEISHA", "TAREN", "TA", "STACEE", "SHIN", "SHAWNTA", "SATURNINA", "RICARDA", "POK", "PASTY", "ONIE", "NUBIA", "MORA", "MIKE", "MARIELLE", "MARIELLA", "MARIANELA", "MARDELL", "MANY", "LUANNA", "LOISE", "LISABETH", "LINDSY", "LILLIANA", "LILLIAM", "LELAH", "LEIGHA", "LEANORA", "LANG", "KRISTEEN", "KHALILAH", "KEELEY", "KANDRA", "JUNKO", "JOAQUINA", "JERLENE", "JANI", "JAMIKA", "JAME", "HSIU", "HERMILA", "GOLDEN", "GENEVIVE", "EVIA", "EUGENA", "EMMALINE", "ELFREDA", "ELENE", "DONETTE", "DELCIE", "DEEANNA", "DARCEY", "CUC", "CLARINDA", "CIRA", "CHAE", "CELINDA", "CATHERYN", "CATHERIN", "CASIMIRA", "CARMELIA", "CAMELLIA", "BREANA", "BOBETTE", "BERNARDINA", "BEBE", "BASILIA", "ARLYNE", "AMAL", "ALAYNA", "ZONIA", "ZENIA", "YURIKO", "YAEKO", "WYNELL", "WILLOW", "WILLENA", "VERNIA", "TU", "TRAVIS", "TORA", "TERRILYN", "TERICA", "TENESHA", "TAWNA", "TAJUANA", "TAINA", "STEPHNIE", "SONA", "SOL", "SINA", "SHONDRA", "SHIZUKO", "SHERLENE", "SHERICE", "SHARIKA", "ROSSIE", "ROSENA", "RORY", "RIMA", "RIA", "RHEBA", "RENNA", "PETER", "NATALYA", "NANCEE", "MELODI", "MEDA", "MAXIMA", "MATHA", "MARKETTA", "MARICRUZ", "MARCELENE", "MALVINA", "LUBA", "LOUETTA", "LEIDA", "LECIA", "LAURAN", "LASHAWNA", "LAINE", "KHADIJAH", "KATERINE", "KASI", "KALLIE", "JULIETTA", "JESUSITA", "JESTINE", "JESSIA", "JEREMY", "JEFFIE", "JANYCE", "ISADORA", "GEORGIANNE", "FIDELIA", "EVITA", "EURA", "EULAH", "ESTEFANA", "ELSY", "ELIZABET", "ELADIA", "DODIE", "DION", "DIA", "DENISSE", "DELORAS", "DELILA", "DAYSI", "DAKOTA", "CURTIS", "CRYSTLE", "CONCHA", "COLBY", "CLARETTA", "CHU", "CHRISTIA", "CHARLSIE", "CHARLENA", "CARYLON", "BETTYANN", "ASLEY", "ASHLEA", "AMIRA", "AI", "AGUEDA", "AGNUS", "YUETTE", "VINITA", "VICTORINA", "TYNISHA", "TREENA", "TOCCARA", "TISH", "THOMASENA", "TEGAN", "SOILA", "SHILOH", "SHENNA", "SHARMAINE", "SHANTAE", "SHANDI", "SEPTEMBER", "SARAN", "SARAI", "SANA", "SAMUEL", "SALLEY", "ROSETTE", "ROLANDE", "REGINE", "OTELIA", "OSCAR", "OLEVIA", "NICHOLLE", "NECOLE", "NAIDA", "MYRTA", "MYESHA", "MITSUE", "MINTA", "MERTIE", "MARGY", "MAHALIA", "MADALENE", "LOVE", "LOURA", "LOREAN", "LEWIS", "LESHA", "LEONIDA", "LENITA", "LAVONE", "LASHELL", "LASHANDRA", "LAMONICA", "KIMBRA", "KATHERINA", "KARRY", "KANESHA", "JULIO", "JONG", "JENEVA", "JAQUELYN", "HWA", "GILMA", "GHISLAINE", "GERTRUDIS", "FRANSISCA", "FERMINA", "ETTIE", "ETSUKO", "ELLIS", "ELLAN", "ELIDIA", "EDRA", "DORETHEA", "DOREATHA", "DENYSE", "DENNY", "DEETTA", "DAINE", "CYRSTAL", "CORRIN", "CAYLA", "CARLITA", "CAMILA", "BURMA", "BULA", "BUENA", "BLAKE", "BARABARA", "AVRIL", "AUSTIN", "ALAINE", "ZANA", "WILHEMINA", "WANETTA", "VIRGIL", "VI", "VERONIKA", "VERNON", "VERLINE", "VASILIKI", "TONITA", "TISA", "TEOFILA", "TAYNA", "TAUNYA", "TANDRA", "TAKAKO", "SUNNI", "SUANNE", "SIXTA", "SHARELL", "SEEMA", "RUSSELL", "ROSENDA", "ROBENA", "RAYMONDE", "PEI", "PAMILA", "OZELL", "NEIDA", "NEELY", "MISTIE", "MICHA", "MERISSA", "MAURITA", "MARYLN", "MARYETTA", "MARSHALL", "MARCELL", "MALENA", "MAKEDA", "MADDIE", "LOVETTA", "LOURIE", "LORRINE", "LORILEE", "LESTER", "LAURENA", "LASHAY", "LARRAINE", "LAREE", "LACRESHA", "KRISTLE", "KRISHNA", "KEVA", "KEIRA", "KAROLE", "JOIE", "JINNY", "JEANNETTA", "JAMA", "HEIDY", "GILBERTE", "GEMA", "FAVIOLA", "EVELYNN", "ENDA", "ELLI", "ELLENA", "DIVINA", "DAGNY", "COLLENE", "CODI", "CINDIE", "CHASSIDY", "CHASIDY", "CATRICE", "CATHERINA", "CASSEY", "CAROLL", "CARLENA", "CANDRA", "CALISTA", "BRYANNA", "BRITTENY", "BEULA", "BARI", "AUDRIE", "AUDRIA", "ARDELIA", "ANNELLE", "ANGILA", "ALONA", "ALLYN", "DOUGLAS", "ROGER", "JONATHAN", "RALPH", "NICHOLAS", "BENJAMIN", "BRUCE", "HARRY", "WAYNE", "STEVE", "HOWARD", "ERNEST", "PHILLIP", "TODD", "CRAIG", "ALAN", "PHILIP", "EARL", "DANNY", "BRYAN", "STANLEY", "LEONARD", "NATHAN", "MANUEL", "RODNEY", "MARVIN", "VINCENT", "JEFFERY", "JEFF", "CHAD", "JACOB", "ALFRED", "BRADLEY", "HERBERT", "FREDERICK", "EDWIN", "DON", "RICKY", "RANDALL", "BARRY", "BERNARD", "LEROY", "MARCUS", "THEODORE", "CLIFFORD", "MIGUEL", "JIM", "TOM", "CALVIN", "BILL", "LLOYD", "DEREK", "WARREN", "DARRELL", "JEROME", "FLOYD", "ALVIN", "TIM", "GORDON", "GREG", "JORGE", "DUSTIN", "PEDRO", "DERRICK", "ZACHARY", "HERMAN", "GLEN", "HECTOR", "RICARDO", "RICK", "BRENT", "RAMON", "GILBERT", "MARC", "REGINALD", "RUBEN", "NATHANIEL", "RAFAEL", "EDGAR", "MILTON", "RAUL", "BEN", "CHESTER", "DUANE", "FRANKLIN", "BRAD", "RON", "ROLAND", "ARNOLD", "HARVEY", "JARED", "ERIK", "DARRYL", "NEIL", "JAVIER", "FERNANDO", "CLINTON", "TED", "MATHEW", "TYRONE", "DARREN", "LANCE", "KURT", "ALLAN", "NELSON", "GUY", "CLAYTON", "HUGH", "MAX", "DWAYNE", "DWIGHT", "ARMANDO", "FELIX", "EVERETT", "IAN", "WALLACE", "KEN", "BOB", "ALFREDO", "ALBERTO", "DAVE", "IVAN", "BYRON", "ISAAC", "MORRIS", "CLIFTON", "WILLARD", "ROSS", "ANDY", "SALVADOR", "KIRK", "SERGIO", "SETH", "KENT", "TERRANCE", "EDUARDO", "TERRENCE", "ENRIQUE", "WADE", "STUART", "FREDRICK", "ARTURO", "ALEJANDRO", "NICK", "LUTHER", "WENDELL", "JEREMIAH", "JULIUS", "OTIS", "TREVOR", "OLIVER", "LUKE", "HOMER", "GERARD", "DOUG", "KENNY", "HUBERT", "LYLE", "MATT", "ALFONSO", "ORLANDO", "REX", "CARLTON", "ERNESTO", "NEAL", "PABLO", "LORENZO", "OMAR", "WILBUR", "GRANT", "HORACE", "RODERICK", "ABRAHAM", "WILLIS", "RICKEY", "ANDRES", "CESAR", "JOHNATHAN", "MALCOLM", "RUDOLPH", "DAMON", "KELVIN", "PRESTON", "ALTON", "ARCHIE", "MARCO", "WM", "PETE", "RANDOLPH", "GARRY", "GEOFFREY", "JONATHON", "FELIPE", "GERARDO", "ED", "DOMINIC", "DELBERT", "COLIN", "GUILLERMO", "EARNEST", "LUCAS", "BENNY", "SPENCER", "RODOLFO", "MYRON", "EDMUND", "GARRETT", "SALVATORE", "CEDRIC", "LOWELL", "GREGG", "SHERMAN", "WILSON", "SYLVESTER", "ROOSEVELT", "ISRAEL", "JERMAINE", "FORREST", "WILBERT", "LELAND", "SIMON", "CLARK", "IRVING", "BRYANT", "OWEN", "RUFUS", "WOODROW", "KRISTOPHER", "MACK", "LEVI", "MARCOS", "GUSTAVO", "JAKE", "LIONEL", "GILBERTO", "CLINT", "NICOLAS", "ISMAEL", "ORVILLE", "ERVIN", "DEWEY", "AL", "WILFRED", "JOSH", "HUGO", "IGNACIO", "CALEB", "TOMAS", "SHELDON", "ERICK", "STEWART", "DOYLE", "DARREL", "ROGELIO", "TERENCE", "SANTIAGO", "ALONZO", "ELIAS", "BERT", "ELBERT", "RAMIRO", "CONRAD", "NOAH", "GRADY", "PHIL", "CORNELIUS", "LAMAR", "ROLANDO", "CLAY", "PERCY", "DEXTER", "BRADFORD", "DARIN", "AMOS", "MOSES", "IRVIN", "SAUL", "ROMAN", "RANDAL", "TIMMY", "DARRIN", "WINSTON", "BRENDAN", "ABEL", "DOMINICK", "BOYD", "EMILIO", "ELIJAH", "DOMINGO", "EMMETT", "MARLON", "EMANUEL", "JERALD", "EDMOND", "EMIL", "DEWAYNE", "WILL", "OTTO", "TEDDY", "REYNALDO", "BRET", "JESS", "TRENT", "HUMBERTO", "EMMANUEL", "STEPHAN", "VICENTE", "LAMONT", "GARLAND", "MILES", "EFRAIN", "HEATH", "RODGER", "HARLEY", "ETHAN", "ELDON", "ROCKY", "PIERRE", "JUNIOR", "FREDDY", "ELI", "BRYCE", "ANTOINE", "STERLING", "CHASE", "GROVER", "ELTON", "CLEVELAND", "DYLAN", "CHUCK", "DAMIAN", "REUBEN", "STAN", "AUGUST", "LEONARDO", "JASPER", "RUSSEL", "ERWIN", "BENITO", "HANS", "MONTE", "BLAINE", "ERNIE", "CURT", "QUENTIN", "AGUSTIN", "MURRAY", "JAMAL", "ADOLFO", "HARRISON", "TYSON", "BURTON", "BRADY", "ELLIOTT", "WILFREDO", "BART", "JARROD", "VANCE", "DENIS", "DAMIEN", "JOAQUIN", "HARLAN", "DESMOND", "ELLIOT", "DARWIN", "GREGORIO", "BUDDY", "XAVIER", "KERMIT", "ROSCOE", "ESTEBAN", "ANTON", "SOLOMON", "SCOTTY", "NORBERT", "ELVIN", "WILLIAMS", "NOLAN", "ROD", "QUINTON", "HAL", "BRAIN", "ROB", "ELWOOD", "KENDRICK", "DARIUS", "MOISES", "FIDEL", "THADDEUS", "CLIFF", "MARCEL", "JACKSON", "RAPHAEL", "BRYON", "ARMAND", "ALVARO", "JEFFRY", "DANE", "JOESPH", "THURMAN", "NED", "RUSTY", "MONTY", "FABIAN", "REGGIE", "MASON", "GRAHAM", "ISAIAH", "VAUGHN", "GUS", "LOYD", "DIEGO", "ADOLPH", "NORRIS", "MILLARD", "ROCCO", "GONZALO", "DERICK", "RODRIGO", "WILEY", "RIGOBERTO", "ALPHONSO", "TY", "NOE", "VERN", "REED", "JEFFERSON", "ELVIS", "BERNARDO", "MAURICIO", "HIRAM", "DONOVAN", "BASIL", "RILEY", "NICKOLAS", "MAYNARD", "SCOT", "VINCE", "QUINCY", "EDDY", "SEBASTIAN", "FEDERICO", "ULYSSES", "HERIBERTO", "DONNELL", "COLE", "DAVIS", "GAVIN", "EMERY", "WARD", "ROMEO", "JAYSON", "DANTE", "CLEMENT", "COY", "MAXWELL", "JARVIS", "BRUNO", "ISSAC", "DUDLEY", "BROCK", "SANFORD", "CARMELO", "BARNEY", "NESTOR", "STEFAN", "DONNY", "ART", "LINWOOD", "BEAU", "WELDON", "GALEN", "ISIDRO", "TRUMAN", "DELMAR", "JOHNATHON", "SILAS", "FREDERIC", "DICK", "IRWIN", "MERLIN", "CHARLEY", "MARCELINO", "HARRIS", "CARLO", "TRENTON", "KURTIS", "HUNTER", "AURELIO", "WINFRED", "VITO", "COLLIN", "DENVER", "CARTER", "LEONEL", "EMORY", "PASQUALE", "MOHAMMAD", "MARIANO", "DANIAL", "LANDON", "DIRK", "BRANDEN", "ADAN", "BUFORD", "GERMAN", "WILMER", "EMERSON", "ZACHERY", "FLETCHER", "JACQUES", "ERROL", "DALTON", "MONROE", "JOSUE", "EDWARDO", "BOOKER", "WILFORD", "SONNY", "SHELTON", "CARSON", "THERON", "RAYMUNDO", "DAREN", "HOUSTON", "ROBBY", "LINCOLN", "GENARO", "BENNETT", "OCTAVIO", "CORNELL", "HUNG", "ARRON", "ANTONY", "HERSCHEL", "GIOVANNI", "GARTH", "CYRUS", "CYRIL", "RONNY", "LON", "FREEMAN", "DUNCAN", "KENNITH", "CARMINE", "ERICH", "CHADWICK", "WILBURN", "RUSS", "REID", "MYLES", "ANDERSON", "MORTON", "JONAS", "FOREST", "MITCHEL", "MERVIN", "ZANE", "RICH", "JAMEL", "LAZARO", "ALPHONSE", "RANDELL", "MAJOR", "JARRETT", "BROOKS", "ABDUL", "LUCIANO", "SEYMOUR", "EUGENIO", "MOHAMMED", "VALENTIN", "CHANCE", "ARNULFO", "LUCIEN", "FERDINAND", "THAD", "EZRA", "ALDO", "RUBIN", "ROYAL", "MITCH", "EARLE", "ABE", "WYATT", "MARQUIS", "LANNY", "KAREEM", "JAMAR", "BORIS", "ISIAH", "EMILE", "ELMO", "ARON", "LEOPOLDO", "EVERETTE", "JOSEF", "ELOY", "RODRICK", "REINALDO", "LUCIO", "JERROD", "WESTON", "HERSHEL", "BARTON", "PARKER", "LEMUEL", "BURT", "JULES", "GIL", "ELISEO", "AHMAD", "NIGEL", "EFREN", "ANTWAN", "ALDEN", "MARGARITO", "COLEMAN", "DINO", "OSVALDO", "LES", "DEANDRE", "NORMAND", "KIETH", "TREY", "NORBERTO", "NAPOLEON", "JEROLD", "FRITZ", "ROSENDO", "MILFORD", "CHRISTOPER", "ALFONZO", "LYMAN", "JOSIAH", "BRANT", "WILTON", "RICO", "JAMAAL", "DEWITT", "BRENTON", "OLIN", "FOSTER", "FAUSTINO", "CLAUDIO", "JUDSON", "GINO", "EDGARDO", "ALEC", "TANNER", "JARRED", "DONN", "TAD", "PRINCE", "PORFIRIO", "ODIS", "LENARD", "CHAUNCEY", "TOD", "MEL", "MARCELO", "KORY", "AUGUSTUS", "KEVEN", "HILARIO", "BUD", "SAL", "ORVAL", "MAURO", "ZACHARIAH", "OLEN", "ANIBAL", "MILO", "JED", "DILLON", "AMADO", "NEWTON", "LENNY", "RICHIE", "HORACIO", "BRICE", "MOHAMED", "DELMER", "DARIO", "REYES", "MAC", "JONAH", "JERROLD", "ROBT", "HANK", "RUPERT", "ROLLAND", "KENTON", "DAMION", "ANTONE", "WALDO", "FREDRIC", "BRADLY", "KIP", "BURL", "WALKER", "TYREE", "JEFFEREY", "AHMED", "WILLY", "STANFORD", "OREN", "NOBLE", "MOSHE", "MIKEL", "ENOCH", "BRENDON", "QUINTIN", "JAMISON", "FLORENCIO", "DARRICK", "TOBIAS", "HASSAN", "GIUSEPPE", "DEMARCUS", "CLETUS", "TYRELL", "LYNDON", "KEENAN", "WERNER", "GERALDO", "COLUMBUS", "CHET", "BERTRAM", "MARKUS", "HUEY", "HILTON", "DWAIN", "DONTE", "TYRON", "OMER", "ISAIAS", "HIPOLITO", "FERMIN", "ADALBERTO", "BO", "BARRETT", "TEODORO", "MCKINLEY", "MAXIMO", "GARFIELD", "RALEIGH", "LAWERENCE", "ABRAM", "RASHAD", "KING", "EMMITT", "DARON", "SAMUAL", "MIQUEL", "EUSEBIO", "DOMENIC", "DARRON", "BUSTER", "WILBER", "RENATO", "JC", "HOYT", "HAYWOOD", "EZEKIEL", "CHAS", "FLORENTINO", "ELROY", "CLEMENTE", "ARDEN", "NEVILLE", "EDISON", "DESHAWN", "NATHANIAL", "JORDON", "DANILO", "CLAUD", "SHERWOOD", "RAYMON", "RAYFORD", "CRISTOBAL", "AMBROSE", "TITUS", "HYMAN", "FELTON", "EZEQUIEL", "ERASMO", "STANTON", "LONNY", "LEN", "IKE", "MILAN", "LINO", "JAROD", "HERB", "ANDREAS", "WALTON", "RHETT", "PALMER", "DOUGLASS", "CORDELL", "OSWALDO", "ELLSWORTH", "VIRGILIO", "TONEY", "NATHANAEL", "DEL", "BENEDICT", "MOSE", "JOHNSON", "ISREAL", "GARRET", "FAUSTO", "ASA", "ARLEN", "ZACK", "WARNER", "MODESTO", "FRANCESCO", "MANUAL", "GAYLORD", "GASTON", "FILIBERTO", "DEANGELO", "MICHALE", "GRANVILLE", "WES", "MALIK", "ZACKARY", "TUAN", "ELDRIDGE", "CRISTOPHER", "CORTEZ", "ANTIONE", "MALCOM", "LONG", "KOREY", "JOSPEH", "COLTON", "WAYLON", "VON", "HOSEA", "SHAD", "SANTO", "RUDOLF", "ROLF", "REY", "RENALDO", "MARCELLUS", "LUCIUS", "KRISTOFER", "BOYCE", "BENTON", "HAYDEN", "HARLAND", "ARNOLDO", "RUEBEN", "LEANDRO", "KRAIG", "JERRELL", "JEROMY", "HOBERT", "CEDRICK", "ARLIE", "WINFORD", "WALLY", "LUIGI", "KENETH", "JACINTO", "GRAIG", "FRANKLYN", "EDMUNDO", "SID", "PORTER", "LEIF", "JERAMY", "BUCK", "WILLIAN", "VINCENZO", "SHON", "LYNWOOD", "JERE", "HAI", "ELDEN", "DORSEY", "DARELL", "BRODERICK", "ALONSO"]
names.sort()
alphabet = ["A",  "B",  "C",  "D",  "E",  "F",  "G",  "H",  "I",  "J",  "K",  "L",  "M",  "N",  "O",  "P",  "Q",  "R",  "S",  "T",  "U",  "V", 
            "W",  "X",  "Y",  "Z"]


def score():
    total = 0
    for n in names:
        ab = 0
        order = names.index(n) + 1
        for i in n:
            ab += alphabet.index(i) + 1
        total += order * ab
    return total,  time.time() - start


print(score())
# Great job boom.
# problem 23


def abundant():
    start = time.time()
    nums = []
    abundant_nums = []
    sums = []
    result = 0
    for n in range(1,  28124):
        nums += [n]
        abundant_n = 0
        for x in range(1,  n):
            if n % x == 0:
                abundant_n += x
        if abundant_n > n:
            abundant_nums += [n]
    for y in range(len(abundant_nums)):
        if y == len(abundant_nums) - 1:
            sums += [abundant_nums[-1] + abundant_nums[-2]]
        for i in range(y, len(abundant_nums)):
            sums += [(abundant_nums[y] + abundant_nums[i])]
    wanted_nums = list(set(nums) - set(sums))
    for i in wanted_nums:
        result += i
    return result,  time.time() - start


print(abundant())
# great great job !!!!!
# problem 24
# that's a very good solution which gives the answer within 0 second !!


def permutation(order):
    start = time.time()
    digits = [0,  1,  2,  3,  4,  5,  6,  7,  8,  9]  # our main list.
    original_digits = digits.copy()  # take a shallow copy of the list.
    i = 1
    result = 0
    wanted_num = ""
    while i <= len(original_digits):
        x = 0
        while True:
            result += factorial(len(original_digits) - i)  # removing the number of redundant possibilities.
            x += 1
            if result > order - 1:
                result -= factorial(len(original_digits) - i)
                x -= 1
                wanted_num += str(digits[x])
                digits.remove(digits[x])  # prevent repetition.
                break
        i += 1
        if result == order and len(digits) == 0:
            break
    return int(wanted_num),  time.time() - start


print(permutation(1000000))
# that's a bad one cause it takes about 1650 seconds !!


def permutation(order):
    start = time.time()
    original_order = order
    digits = "0123456789"
    x = 0
    result = 0
    while True:
        result += factorial(len(digits) - 1)
        if result > order:
            result -= factorial(len(digits) - 1)
            break
        x += 1
    nums = []
    list(digits).remove(str(x))
    for i in product(digits,  repeat=len(digits) - 1):
        result = ""
        if len(nums) > order:
            break
        if len(set(i)) == len(digits) - 1:
            for n in i:
                result += str(n)
            nums.append(int(result))
    nums.sort()
    return nums[order - 1],  time.time() - start


print(permutation(1000000))
# problem 25


def fibonacci(limit):
    start = time.time()
    result = 0
    num1 = 1
    num2 = 1
    counter = 2
    while len(str(result)) != limit:
        result = num1 + num2
        num1 = num2
        num2 = result
        counter += 1
    return counter,  time.time() - start


print(fibonacci(1000))

# problem 26







def biggest_recurring_cycle():
    start = time.time()
    biggest_recurring = 0
    longest_recurring = 0
    for i in range(1,  1000):
        if is_prime(i) and longest_recurring < len(set(str(1 / i))) and is_cycle(i) and \
                len(set(str(1 / i))) - 2 < (len(str(1 / i)) - 2) / 2:
            longest_recurring = len(set(str(1 / i)))
            biggest_recurring = i
    return biggest_recurring,  time.time() - start


print(biggest_recurring_cycle())


def division(num):
    result = ""
    divisor = 1
    while len(result) < 100 and divisor != 0:
        t_result = 0  # temporary result
        while divisor < num:
            divisor *= 10
        while divisor >= num:
            divisor -= num
            t_result += 1
        if num > divisor:
            result += str(t_result)

    return result


print(division(983))


def is_cycle(number):
    for i in range(len(division(number)) - 7):
        for n in range(i + 1,  len(division(number)) - 7):
            if division(number)[i] == division(number)[n] and division(number)[1 + i] == division(number)[n + 1] and\
                    division(number)[2 + i] == division(number)[2 + n] and division(number)[3 + i] == division(number)[n + 3] and\
                    division(number)[4 + i] == division(number)[n + 4] and division(number)[5 + i] == division(number)[n + 5]\
                    and division(number)[6 + i] == division(number)[n + 6] and division(number)[7 + i] == division(number)[n + 7]:
                return True





def cycle():
    start = time.time()
    longest_cycle = 0
    longest_num = 0
    for i in range(1,  1000):
        if is_prime(i) and is_cycle(i) and len(division(i)) > 60:
            for k in range(1,  len(division(i))):
                if division(i)[:k] == division(i)[k:2*k] == division(i)[2*k:3*k] and longest_cycle < k and len(set(division(i))) > 3:
                    longest_cycle = k
                    longest_num = i
    return longest_num,  time.time() - start


print(cycle())



def is_prime(num):
    if all(num % i != 0 for i in range(2,  int(sqrt(num)) + 1)):
        return True
# not my solution


def biggest_recur(limit):
    start = time.time()
    max_len = 0
    max_d = 1
    d = 0
    while d < limit:
        d += 1
        quotient = []  # Stores the decimal quotient
        cur_value = 1  # Variable used to perform division as if by hand # any number except 0 means True
        len_recur = 0  # Recurring length
        # Performing division as if by hand.
        while cur_value not in quotient and cur_value:
            len_recur += 1
            quotient.append(cur_value)
            cur_value = (cur_value % d) * 10
        if not cur_value:
            continue
    # Remove number of values that do not recur
    # len_recur -= quotient.index(cur_value) + 1  # it equals to (quotient.index(cur_value) + 1)
        if len_recur > max_len:
            max_len = len_recur
            max_d = d
    return max_d,  str(time.time() - start) + " seconds"


print(biggest_recur(1000))
# problem 27


def is_prime(num):
    if all(num % i != 0 for i in range(2,  int(sqrt(num)))):
        return True


def biggest_product(limit):
    start = time.time()
    a = -999  # the first coefficient.
    max_len = 0  # the maximum number of prime numbers.
    max_a = 0
    max_b = 0
    while a < limit:
        b = -1000  # the second coefficient.
        while b <= limit:
            n_values = []
            n = 0  # the variable
            while (n**2 + a*n + b) > 0 and is_prime(b) and is_prime(n**2 + a*n + b):
                n += 1
            if max_len < n:
                max_len = n
                max_a = a
                max_b = b
            b += 1
        a += 1
    return max_a * max_b,  "the time spent: " + str(time.time() - start) + " seconds."


print(biggest_product(1000))
# great jooooooooooob !!!

# problem 28
# right_up the pattern is n**2 + (n+2)**2 +..... n = 3
# left_down the pattern is (1 + n**2) + (1 + (n+2)**2)..... n = 2
# left_up the pattern is (n**2 - 2*b) n+=2,  b+=1 (b = 1,  n = 3
# right_down the pattern is (n**2 - a) a+=2 n+=2 (n = 2,  a = 1)


def spiral_diagonals(limit):
    start = time.time()
    n_up_right = 9
    n_up_left = 7
    n_down_right = 3
    n_down_left = 5
    n = 3
    b = 1
    result = 0
    while n <= limit:
        result += (n_up_right + n_up_left + n_down_left + n_down_right)
        n += 2
        b += 1
        n_up_right = n**2  # up_right pattern is n**2 + (n+2)**2 +..... n = 3
        n_up_left = n**2 - 2*b  # up_left pattern is (n**2 - 2*b) n+=2,  b+=1 (b = 1,  n = 3)
        n_down_right = (n - 1)**2 - (n - 1) + 1  # down_right pattern is (n**2 - n + 1) n+=2 (n = 2)
        n_down_left = (n - 1)**2 + 1  # down_left pattern is (1 + n**2) + (1 + (n+2)**2)..... n = 2
    return result + 1,  str(time.time() - start) + " seconds"


print(spiral_diagonals(1001))

# problem 29


def distinct_powers(limit):
    start = time.time()
    a = 2
    distinct_numbers = []
    while a <= limit:
        b = 2
        while b <= limit:
            distinct_numbers.append(a**b)
            b += 1
        a += 1
    return len(set(distinct_numbers)),  str(time.time() - start) + " seconds"


print(distinct_powers(100))

# problem 30


def digit_fifth(limit,  power):
    start = time.time()
    total = 0
    for i in range(2,  limit):
        t_result = 0
        for n in str(i):
            t_result += int(n)**power
        if t_result == i:
            total += i
    return total,  time.time() - start


print(digit_fifth(1000000,  5))

# problem 31


def sum_coins():
    start = time.time()
    counter = 1
    for i in range(3):
        for n in range(int(1+(200-100*i)/50)):  # n refers to the denomination of 50p and so on...
            for k in range(int(1+(200-100*i-50*n)/20)):
                for h in range(int(1+(200-100*i-50*n-20*k)/10)):
                    for j in range(int(1+(200-100*i-50*n-20*k-10*h)/5)):
                        for m in range(int(1+(200-100*i-50*n-20*k-10*h-5*j)/2)):
                            counter += 1
    return counter,  time.time() - start


print(sum_coins())

# problem 32


def pandigital():
    start = time.time()
    total = 0
    nums = {"1",  "2",  "3",  "4",  "5",  "6",  "7",  "8",  "9"}
    pandigital_nums = []
    for i in range(1233,  10000):
        check = True  # to see if the number makes sense with the first condition.
        if len(str(i)) == len(set(str(i))) and "0" not in str(i):
            the_rest = nums - set(str(i))  # the rest of unused numbers from the set nums
            for j in product(the_rest,  repeat=3):
                if len(set(j)) == 3 and i % int(str(j[0]) + str(j[1]) + str(j[2])) == 0:
                    t_sum = int(i / int(str(j[0]) + str(j[1]) + str(j[2])))
                    if "0" not in str(t_sum) and len(nums) ==\
                            len(set(str(i)).union(set(str(j[0]) + str(j[1]) + str(j[2]))).union(set(str(t_sum)))):
                        pandigital_nums += [i]
                        total += i
                        check = False
                        break
            if check:
                for n in product(the_rest,  repeat=4):
                    if len(set(n)) == 4 and i % int(str(n[0]) + str(n[1]) + str(n[2]) + str(n[3])) == 0:
                        t_sum = int(i / int(str(n[0]) + str(n[1]) + str(n[2]) + str(n[3])))
                        if "0" not in str(t_sum) and len(nums) == \
                                len(set(str(i)).union(set(str(n[0]) + str(n[1]) + str(n[2]) + str(n[3]))).union(set(str(t_sum)))):
                            pandigital_nums += [i]
                            total += i
                            break
    return total,  pandigital_nums,  time.time() - start


print(pandigital())

# problem 33


def digit_cancelling():
    start = time.time()
    denominator = 1
    numerator = 1
    for i in range(11,  100):
        for n in range(i + 1,  100):
            if "0" not in str(i) + str(n) and ((int(str(i)[1]) / int(str(n)[1]) == i / n and str(i)[0] == str(n)[0]) or
                    (int(str(i)[0]) / int(str(n)[1]) == i / n and str(i)[1] == str(n)[0]) or
                    (int(str(i)[1]) / int(str(n)[0]) == i / n and str(i)[0] == str(n)[1]) or
                    (int(str(i)[0]) / int(str(n)[0]) == i / n and str(i)[1] == str(n)[1])):
                denominator *= n
                numerator *= i
    #  before using Fraction function you must do that(from fractions import Fractions.
    return int(str(Fraction(numerator,  denominator))[2:]),  time.time() - start


print(digit_cancelling())

# problem 34


def digit_factorial():
    start = time.time()
    total = 0
    max_i = 0
    for i in range(10,  40586):
        t_result = 0
        for n in str(i):
            t_result += factorial(int(n))
        if i == t_result:
            total += i
            max_i = i
    return total,  max_i,  time.time() - start


print(digit_factorial())

# problem 35


def is_prime(num):
    if all(num % n != 0 for n in range(2,  int(num**0.5 + 1))):
        return True
    else:
        return False


def circular_prime(limit):
    nums = []
    start = time.time()
    counter = 0
    for i in range(2,  limit):
        check = True  # to see if it's circular
        if is_prime(i):
            for n in range(len(str(i))):
                i = (i % 10)*10**(len(str(i)) - 1)+i//10  # this gives you the permutations.
                if not is_prime(i):
                    check = False
                    break
            if check:
                counter += 1
                nums += [i]
    return counter,  nums,   time.time() - start


print(circular_prime(1000000))

# problem 36


def binary(num):
    binary_num = ""
    while num != 0:
        binary_num += str(num % 2)
        num //= 2
    return binary_num


def palindrome(limit):
    start = time.time()
    total = 0
    for i in range(1,  limit,  2):
        if str(i) == str(i)[::-1] and binary(i) == binary(i)[::-1]:
            total += i
    return total,  time.time() - start


print(palindrome(1000000))

# problem 37


def ideal_primes(limit):
    start = time.time()
    is_prime = [True] * limit
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    for i in range(int(len(is_prime) ** 0.5)):
        if is_prime[i]:
            index = i * 2
            while index < len(is_prime):
                is_prime[index] = False
                index += i
    total = 0
    for i in range(11,  limit,  2):
        check = True
        if is_prime[i]:
            for n in range(1,  len(str(i))):  # check from right to left.
                if not is_prime[int(str(i)[:n])]:
                    check = False
                    break
            if check:
                for n in range(1,  len(str(i))):  # check fro left to right.
                    if not is_prime[int(str(i)[n:])]:
                        check = False
                        break
            if check:
                total += i
    return total,  time.time() - start


print(ideal_primes(1000000))

# problem 38


def palindrome():
    start = time.time()
    max_result = 0
    for i in range(10000):
        result = ""
        for n in range(1, 20):
            result += str(i*n)
            if len(result) > len(set(result)) or "0" in result:
                break
            elif len(result) == 9 and int(result) > max_result:
                max_result = int(result)
    return max_result,  time.time() - start


print(palindrome())

# problem 39

# this solution is too slow.


def biggest_possibilities(limit):
    start = time.time()
    max_counter = 0
    max_p = 0
    for p in range(12,  limit + 1):
        counter = 0
        for tendon in range(1,  p//2-1):
            for f_rib in range(tendon//2-1,  tendon):
                for s_rib in range(1+tendon-f_rib,  f_rib + 1):
                    if p == tendon + f_rib + s_rib and tendon**2 == f_rib**2 + s_rib**2:
                        counter += 1
                    elif p < tendon + f_rib + s_rib:  # this condition makes it more slow.
                        break
        if max_counter < counter:
            max_counter = counter
            max_p = p
    return max_p,  time.time() - start


print(biggest_possibilities(1000))

# here is a better solution that gives you the solution within a 0.1 second.


def most_repeated(limit):
    start = time.time()
    perimeters = []
    for i in range(1,  limit//2):
        for b in range(i,  limit//2):
            c = (i**2+b**2)**0.5
            if c == int(c):
                perimeters += [i+b+c]
    return int(Counter(perimeters).most_common(1)[0][0]),  time.time() - start


print(most_repeated(1000))

# problem 40


def champernowne_constant(limit):
    start = time.time()
    result = ""
    wanted_num = 1
    n = 0
    i = 1
    while len(result) <= limit:  # when the length of the string reaches the limit it'll break.
        result += str(i)
        i += 1
    while n < limit:
        wanted_num *= int(result[n])
        n = n*10 + 9  # (9,  99,  999, .....)
    return wanted_num,  time.time() - start


print(champernowne_constant(1000000))

# problem 41


def is_prime(num):
    """
    all The Even Numbers achieves that (num+1)/6 != 0 and (num-1)/6 != 0 but not vice versa.
    """
    if (num+1)/6 != 0 and (num-1)/6 != 0 and \
            all(num % n != 0 for n in range(2,  int(num**0.5 + 1))):
            return True


def pandigital():
    start = time.time()
    max_pandigital = 0
    for i in range(5000001,  10000000,  2):
        if len(str(i)) == len(set(str(i))) and is_prime(i) and \
                all(n in "123456789"[:len(str(i))] for n in str(i)):
            max_pandigital = i
    return max_pandigital,  time.time() - start


print(pandigital())

# a faster solution


def is_prime(num):
    """
    all The Even Numbers achieves that (num+1)/6 != 0 and (num-1)/6 != 0 but not vice versa.
    """
    if all(num % n != 0 for n in range(2,  int(num**0.5 + 1))):
        return True


def pandigital():
    start = time.time()
    numbers = "123456789"
    r = 9  # r for range.
    while r != 0:
        p = list(permutations(numbers[:r]))[::-1]  # all possible permutation.
        for i in p:
            wanted_num = ""
            if int(i[-1]) % 2 != 0:
                wanted_num = ''.join(i)  # that's a more professional way.
                if int(wanted_num)+1 % 6 != 0 and int(wanted_num)-1 % 6 != 0 and \
                        is_prime(int(wanted_num)):
                    return int(wanted_num),  time.time() - start
        r -= 1


print(pandigital())

# problem 42


def triangle_words():
    start = time.time()
    words = ["A", "ABILITY", "ABLE", "ABOUT", "ABOVE", "ABSENCE", "ABSOLUTELY", "ACADEMIC", "ACCEPT", "ACCESS", "ACCIDENT",
             "ACCOMPANY", "ACCORDING", "ACCOUNT", "ACHIEVE", "ACHIEVEMENT", "ACID", "ACQUIRE", "ACROSS", "ACT", "ACTION",
             "ACTIVE", "ACTIVITY", "ACTUAL", "ACTUALLY", "ADD", "ADDITION", "ADDITIONAL", "ADDRESS", "ADMINISTRATION",
             "ADMIT", "ADOPT", "ADULT", "ADVANCE", "ADVANTAGE", "ADVICE", "ADVISE", "AFFAIR", "AFFECT", "AFFORD", "AFRAID",
             "AFTER", "AFTERNOON", "AFTERWARDS", "AGAIN", "AGAINST", "AGE", "AGENCY", "AGENT", "AGO", "AGREE", "AGREEMENT",
             "AHEAD", "AID", "AIM", "AIR", "AIRCRAFT", "ALL", "ALLOW", "ALMOST", "ALONE", "ALONG", "ALREADY", "ALRIGHT",
             "ALSO", "ALTERNATIVE", "ALTHOUGH", "ALWAYS", "AMONG", "AMONGST", "AMOUNT", "AN", "ANALYSIS", "ANCIENT", "AND",
             "ANIMAL", "ANNOUNCE", "ANNUAL", "ANOTHER", "ANSWER", "ANY", "ANYBODY", "ANYONE", "ANYTHING", "ANYWAY",
             "APART", "APPARENT", "APPARENTLY", "APPEAL", "APPEAR", "APPEARANCE", "APPLICATION", "APY", "APPOINT", "APPOINTMENT", "APPROACH", "APPROPRIATE", "APPROVE", "AREA", "ARGUE", "ARGUMENT", "ARISE", "ARM", "ARMY", "AROUND", "ARRANGE", "ARRANGEMENT", "ARRIVE", "ART", "ARTICLE", "ARTIST", "AS", "ASK", "ASPECT", "ASSEMBLY", "ASSESS", "ASSESSMENT", "ASSET", "ASSOCIATE", "ASSOCIATION", "ASSUME", "ASSUMPTION", "AT", "ATMOSPHERE", "ATTACH", "ATTACK", "ATTEMPT", "ATTEND", "ATTENTION", "ATTITUDE", "ATTRACT", "ATTRACTIVE", "AUDIENCE", "AUTHOR", "AUTHORITY", "AVAILABLE", "AVERAGE", "AVOID", "AWARD", "AWARE", "AWAY", "AYE", "BABY", "BACK", "BACKGROUND", "BAD", "BAG", "BALANCE", "BALL", "BAND", "BANK", "BAR", "BASE", "BASIC", "BASIS", "BATTLE", "BE", "BEAR", "BEAT", "BEAUTIFUL", "BECAUSE", "BECOME", "BED", "BEDROOM", "BEFORE", "BEGIN", "BEGINNING", "BEHAVIOUR", "BEHIND", "BELIEF", "BELIEVE", "BELONG", "BELOW", "BENEATH", "BENEFIT", "BESIDE", "BEST", "BETTER", "BETWEEN", "BEYOND", "BIG", "BILL", "BIND", "BIRD", "BIRTH", "BIT", "BLACK", "BLOCK", "BLOOD", "BLOODY", "BLOW", "BLUE", "BOARD", "BOAT", "BODY", "BONE", "BOOK", "BORDER", "BOTH", "BOTTLE", "BOTTOM", "BOX", "BOY", "BRAIN", "BRANCH", "BREAK", "BREATH", "BRIDGE", "BRIEF", "BRIGHT", "BRING", "BROAD", "BROTHER", "BUDGET", "BUILD", "BUILDING", "BURN", "BUS", "BUSINESS", "BUSY", "BUT", "BUY", "BY", "CABINET", "CALL", "CAMPAIGN", "CAN", "CANDIDATE", "CAPABLE", "CAPACITY", "CAPITAL", "CAR", "CARD", "CARE", "CAREER", "CAREFUL", "CAREFULLY", "CARRY", "CASE", "CASH", "CAT", "CATCH", "CATEGORY", "CAUSE", "CELL", "CENTRAL", "CENTRE", "CENTURY", "CERTAIN", "CERTAINLY", "CHAIN", "CHAIR", "CHAIRMAN", "CHALLENGE", "CHANCE", "CHANGE", "CHANNEL", "CHAPTER", "CHARACTER", "CHARACTERISTIC", "CHARGE", "CHEAP", "CHECK", "CHEMICAL", "CHIEF", "CHILD", "CHOICE", "CHOOSE", "CHURCH", "CIRCLE", "CIRCUMSTANCE", "CITIZEN", "CITY", "CIVIL", "CLAIM", "CLASS", "CLEAN", "CLEAR", "CLEARLY", "CLIENT", "CLIMB", "CLOSE", "CLOSELY", "CLOTHES", "CLUB", "COAL", "CODE", "COFFEE", "COLD", "COLLEAGUE", "COLLECT", "COLLECTION", "COLLEGE", "COLOUR", "COMBINATION", "COMBINE", "COME", "COMMENT", "COMMERCIAL", "COMMISSION", "COMMIT", "COMMITMENT", "COMMITTEE", "COMMON", "COMMUNICATION", "COMMUNITY", "COMPANY", "COMPARE", "COMPARISON", "COMPETITION", "COMPLETE", "COMPLETELY", "COMPLEX", "COMPONENT", "COMPUTER", "CONCENTRATE", "CONCENTRATION", "CONCEPT", "CONCERN", "CONCERNED", "CONCLUDE", "CONCLUSION", "CONDITION", "CONDUCT", "CONFERENCE", "CONFIDENCE", "CONFIRM", "CONFLICT", "CONGRESS", "CONNECT", "CONNECTION", "CONSEQUENCE", "CONSERVATIVE", "CONSIDER", "CONSIDERABLE", "CONSIDERATION", "CONSIST", "CONSTANT", "CONSTRUCTION", "CONSUMER", "CONTACT", "CONTAIN", "CONTENT", "CONTEXT", "CONTINUE", "CONTRACT", "CONTRAST", "CONTRIBUTE", "CONTRIBUTION", "CONTROL", "CONVENTION", "CONVERSATION", "COPY", "CORNER", "CORPORATE", "CORRECT", "COS", "COST", "COULD", "COUNCIL", "COUNT", "COUNTRY", "COUNTY", "COUPLE", "COURSE", "COURT", "COVER", "CREATE", "CREATION", "CREDIT", "CRIME", "CRIMINAL", "CRISIS", "CRITERION", "CRITICAL", "CRITICISM", "CROSS", "CROWD", "CRY", "CULTURAL", "CULTURE", "CUP", "CURRENT", "CURRENTLY", "CURRICULUM", "CUSTOMER", "CUT", "DAMAGE", "DANGER", "DANGEROUS", "DARK", "DATA", "DATE", "DAUGHTER", "DAY", "DEAD", "DEAL", "DEATH", "DEBATE", "DEBT", "DECADE", "DECIDE", "DECISION", "DECLARE", "DEEP", "DEFENCE", "DEFENDANT", "DEFINE", "DEFINITION", "DEGREE", "DELIVER", "DEMAND", "DEMOCRATIC", "DEMONSTRATE", "DENY", "DEPARTMENT", "DEPEND", "DEPUTY", "DERIVE", "DESCRIBE", "DESCRIPTION", "DESIGN", "DESIRE", "DESK", "DESPITE", "DESTROY", "DETAIL", "DETAILED", "DETERMINE", "DEVELOP", "DEVELOPMENT", "DEVICE", "DIE", "DIFFERENCE", "DIFFERENT", "DIFFICULT", "DIFFICULTY", "DINNER", "DIRECT", "DIRECTION", "DIRECTLY", "DIRECTOR", "DISAPPEAR", "DISCIPLINE", "DISCOVER", "DISCUSS", "DISCUSSION", "DISEASE", "DISPLAY", "DISTANCE", "DISTINCTION", "DISTRIBUTION", "DISTRICT", "DIVIDE", "DIVISION", "DO", "DOCTOR", "DOCUMENT", "DOG", "DOMESTIC", "DOOR", "DOUBLE", "DOUBT", "DOWN", "DRAW", "DRAWING", "DREAM", "DRESS", "DRINK", "DRIVE", "DRIVER", "DROP", "DRUG", "DRY", "DUE", "DURING", "DUTY", "EACH", "EAR", "EARLY", "EARN", "EARTH", "EASILY", "EAST", "EASY", "EAT", "ECONOMIC", "ECONOMY", "EDGE", "EDITOR", "EDUCATION", "EDUCATIONAL", "EFFECT", "EFFECTIVE", "EFFECTIVELY", "EFFORT", "EGG", "EITHER", "ELDERLY", "ELECTION", "ELEMENT", "ELSE", "ELSEWHERE", "EMERGE", "EMPHASIS", "EMPLOY", "EMPLOYEE", "EMPLOYER", "EMPLOYMENT", "EMPTY", "ENABLE", "ENCOURAGE", "END", "ENEMY", "ENERGY", "ENGINE", "ENGINEERING", "ENJOY", "ENOUGH", "ENSURE", "ENTER", "ENTERPRISE", "ENTIRE", "ENTIRELY", "ENTITLE", "ENTRY", "ENVIRONMENT", "ENVIRONMENTAL", "EQUAL", "EQUALLY", "EQUIPMENT", "ERROR", "ESCAPE", "ESPECIALLY", "ESSENTIAL", "ESTABLISH", "ESTABLISHMENT", "ESTATE", "ESTIMATE", "EVEN", "EVENING", "EVENT", "EVENTUALLY", "EVER", "EVERY", "EVERYBODY", "EVERYONE", "EVERYTHING", "EVIDENCE", "EXACTLY", "EXAMINATION", "EXAMINE", "EXAMPLE", "EXCELLENT", "EXCEPT", "EXCHANGE", "EXECUTIVE", "EXERCISE", "EXHIBITION", "EXIST", "EXISTENCE", "EXISTING", "EXPECT", "EXPECTATION", "EXPENDITURE", "EXPENSE", "EXPENSIVE", "EXPERIENCE", "EXPERIMENT", "EXPERT", "EXPLAIN", "EXPLANATION", "EXPLORE", "EXPRESS", "EXPRESSION", "EXTEND", "EXTENT", "EXTERNAL", "EXTRA", "EXTREMELY", "EYE", "FACE", "FACILITY", "FACT", "FACTOR", "FACTORY", "FAIL", "FAILURE", "FAIR", "FAIRLY", "FAITH", "FALL", "FAMILIAR", "FAMILY", "FAMOUS", "FAR", "FARM", "FARMER", "FASHION", "FAST", "FATHER", "FAVOUR", "FEAR", "FEATURE", "FEE", "FEEL", "FEELING", "FEMALE", "FEW", "FIELD", "FIGHT", "FIGURE", "FILE", "FILL", "FILM", "FINAL", "FINALLY", "FINANCE", "FINANCIAL", "FIND", "FINDING", "FINE", "FINGER", "FINISH", "FIRE", "FIRM", "FIRST", "FISH", "FIT", "FIX", "FLAT", "FLIGHT", "FLOOR", "FLOW", "FLOWER", "FLY", "FOCUS", "FOLLOW", "FOLLOWING", "FOOD", "FOOT", "FOOTBALL", "FOR", "FORCE", "FOREIGN", "FOREST", "FORGET", "FORM", "FORMAL", "FORMER", "FORWARD", "FOUNDATION", "FREE", "FREEDOM", "FREQUENTLY", "FRESH", "FRIEND", "FROM", "FRONT", "FRUIT", "FUEL", "FULL", "FULLY", "FUNCTION", "FUND", "FUNNY", "FURTHER", "FUTURE", "GAIN", "GAME", "GARDEN", "GAS", "GATE", "GATHER", "GENERAL", "GENERALLY", "GENERATE", "GENERATION", "GENTLEMAN", "GET", "GIRL", "GIVE", "GLASS", "GO", "GOAL", "GOD", "GOLD", "GOOD", "GOVERNMENT", "GRANT", "GREAT", "GREEN", "GREY", "GROUND", "GROUP", "GROW", "GROWING", "GROWTH", "GUEST", "GUIDE", "GUN", "HAIR", "HALF", "HALL", "HAND", "HANDLE", "HANG", "HAPPEN", "HAPPY", "HARD", "HARDLY", "HATE", "HAVE", "HE", "HEAD", "HEALTH", "HEAR", "HEART", "HEAT", "HEAVY", "HELL", "HELP", "HENCE", "HER", "HERE", "HERSELF", "HIDE", "HIGH", "HIGHLY", "HILL", "HIM", "HIMSELF", "HIS", "HISTORICAL", "HISTORY", "HIT", "HOLD", "HOLE", "HOLIDAY", "HOME", "HOPE", "HORSE", "HOSPITAL", "HOT", "HOTEL", "HOUR", "HOUSE", "HOUSEHOLD", "HOUSING", "HOW", "HOWEVER", "HUGE", "HUMAN", "HURT", "HUSBAND", "I", "IDEA", "IDENTIFY", "IF", "IGNORE", "ILLUSTRATE", "IMAGE", "IMAGINE", "IMMEDIATE", "IMMEDIATELY", "IMPACT", "IMPLICATION", "IMPLY", "IMPORTANCE", "IMPORTANT", "IMPOSE", "IMPOSSIBLE", "IMPRESSION", "IMPROVE", "IMPROVEMENT", "IN", "INCIDENT", "INCLUDE", "INCLUDING", "INCOME", "INCREASE", "INCREASED", "INCREASINGLY", "INDEED", "INDEPENDENT", "INDEX", "INDICATE", "INDIVIDUAL", "INDUSTRIAL", "INDUSTRY", "INFLUENCE", "INFORM", "INFORMATION", "INITIAL", "INITIATIVE", "INJURY", "INSIDE", "INSIST", "INSTANCE", "INSTEAD", "INSTITUTE", "INSTITUTION", "INSTRUCTION", "INSTRUMENT", "INSURANCE", "INTEND", "INTENTION", "INTEREST", "INTERESTED", "INTERESTING", "INTERNAL", "INTERNATIONAL", "INTERPRETATION", "INTERVIEW", "INTO", "INTRODUCE", "INTRODUCTION", "INVESTIGATE", "INVESTIGATION", "INVESTMENT", "INVITE", "INVOLVE", "IRON", "IS", "ISLAND", "ISSUE", "IT", "ITEM", "ITS", "ITSELF", "JOB", "JOIN", "JOINT", "JOURNEY", "JUDGE", "JUMP", "JUST", "JUSTICE", "KEEP", "KEY", "KID", "KILL", "KIND", "KING", "KITCHEN", "KNEE", "KNOW", "KNOWLEDGE", "LABOUR", "LACK", "LADY", "LAND", "LANGUAGE", "LARGE", "LARGELY", "LAST", "LATE", "LATER", "LATTER", "LAUGH", "LAUNCH", "LAW", "LAWYER", "LAY", "LEAD", "LEADER", "LEADERSHIP", "LEADING", "LEAF", "LEAGUE", "LEAN", "LEARN", "LEAST", "LEAVE", "LEFT", "LEG", "LEGAL", "LEGISLATION", "LENGTH", "LESS", "LET", "LETTER", "LEVEL", "LIABILITY", "LIBERAL", "LIBRARY", "LIE", "LIFE", "LIFT", "LIGHT", "LIKE", "LIKELY", "LIMIT", "LIMITED", "LINE", "LINK", "LIP", "LIST", "LISTEN", "LITERATURE", "LITTLE", "LIVE", "LIVING", "LOAN", "LOCAL", "LOCATION", "LONG", "LOOK", "LORD", "LOSE", "LOSS", "LOT", "LOVE", "LOVELY", "LOW", "LUNCH", "MACHINE", "MAGAZINE", "MAIN", "MAINLY", "MAINTAIN", "MAJOR", "MAJORITY", "MAKE", "MALE", "MAN", "MANAGE", "MANAGEMENT", "MANAGER", "MANNER", "MANY", "MAP", "MARK", "MARKET", "MARRIAGE", "MARRIED", "MARRY", "MASS", "MASTER", "MATCH", "MATERIAL", "MATTER", "MAY", "MAYBE", "ME", "MEAL", "MEAN", "MEANING", "MEANS", "MEANWHILE", "MEASURE", "MECHANISM", "MEDIA", "MEDICAL", "MEET", "MEETING", "MEMBER", "MEMBERSHIP", "MEMORY", "MENTAL", "MENTION", "MERELY", "MESSAGE", "METAL", "METHOD", "MIDDLE", "MIGHT", "MILE", "MILITARY", "MILK", "MIND", "MINE", "MINISTER", "MINISTRY", "MINUTE", "MISS", "MISTAKE", "MODEL", "MODERN", "MODULE", "MOMENT", "MONEY", "MONTH", "MORE", "MORNING", "MOST", "MOTHER", "MOTION", "MOTOR", "MOUNTAIN", "MOUTH", "MOVE", "MOVEMENT", "MUCH", "MURDER", "MUSEUM", "MUSIC", "MUST", "MY", "MYSELF", "NAME", "NARROW", "NATION", "NATIONAL", "NATURAL", "NATURE", "NEAR", "NEARLY", "NECESSARILY", "NECESSARY", "NECK", "NEED", "NEGOTIATION", "NEIGHBOUR", "NEITHER", "NETWORK", "NEVER", "NEVERTHELESS", "NEW", "NEWS", "NEWSPAPER", "NEXT", "NICE", "NIGHT", "NO", "NOBODY", "NOD", "NOISE", "NONE", "NOR", "NORMAL", "NORMALLY", "NORTH", "NORTHERN", "NOSE", "NOT", "NOTE", "NOTHING", "NOTICE", "NOTION", "NOW", "NUCLEAR", "NUMBER", "NURSE", "OBJECT", "OBJECTIVE", "OBSERVATION", "OBSERVE", "OBTAIN", "OBVIOUS", "OBVIOUSLY", "OCCASION", "OCCUR", "ODD", "OF", "OFF", "OFFENCE", "OFFER", "OFFICE", "OFFICER", "OFFICIAL", "OFTEN", "OIL", "OKAY", "OLD", "ON", "ONCE", "ONE", "ONLY", "ONTO", "OPEN", "OPERATE", "OPERATION", "OPINION", "OPPORTUNITY", "OPPOSITION", "OPTION", "OR", "ORDER", "ORDINARY", "ORGANISATION", "ORGANISE", "ORGANIZATION", "ORIGIN", "ORIGINAL", "OTHER", "OTHERWISE", "OUGHT", "OUR", "OURSELVES", "OUT", "OUTCOME", "OUTPUT", "OUTSIDE", "OVER", "OVERALL", "OWN", "OWNER", "PACKAGE", "PAGE", "PAIN", "PAINT", "PAINTING", "PAIR", "PANEL", "PAPER", "PARENT", "PARK", "PARLIAMENT", "PART", "PARTICULAR", "PARTICULARLY", "PARTLY", "PARTNER", "PARTY", "PASS", "PASSAGE", "PAST", "PATH", "PATIENT", "PATTERN", "PAY", "PAYMENT", "PEACE", "PENSION", "PEOPLE", "PER", "PERCENT", "PERFECT", "PERFORM", "PERFORMANCE", "PERHAPS", "PERIOD", "PERMANENT", "PERSON", "PERSONAL", "PERSUADE", "PHASE", "PHONE", "PHOTOGRAPH", "PHYSICAL", "PICK", "PICTURE", "PIECE", "PLACE", "PLAN", "PLANNING", "PLANT", "PLASTIC", "PLATE", "PLAY", "PLAYER", "PLEASE", "PLEASURE", "PLENTY", "PLUS", "POCKET", "POINT", "POLICE", "POLICY", "POLITICAL", "POLITICS", "POOL", "POOR", "POPULAR", "POPULATION", "POSITION", "POSITIVE", "POSSIBILITY", "POSSIBLE", "POSSIBLY", "POST", "POTENTIAL", "POUND", "POWER", "POWERFUL", "PRACTICAL", "PRACTICE", "PREFER", "PREPARE", "PRESENCE", "PRESENT", "PRESIDENT", "PRESS", "PRESSURE", "PRETTY", "PREVENT", "PREVIOUS", "PREVIOUSLY", "PRICE", "PRIMARY", "PRIME", "PRINCIPLE", "PRIORITY", "PRISON", "PRISONER", "PRIVATE", "PROBABLY", "PROBLEM", "PROCEDURE", "PROCESS", "PRODUCE", "PRODUCT", "PRODUCTION", "PROFESSIONAL", "PROFIT", "PROGRAM", "PROGRAMME", "PROGRESS", "PROJECT", "PROMISE", "PROMOTE", "PROPER", "PROPERLY", "PROPERTY", "PROPORTION", "PROPOSE", "PROPOSAL", "PROSPECT", "PROTECT", "PROTECTION", "PROVE", "PROVIDE", "PROVIDED", "PROVISION", "PUB", "PUBLIC", "PUBLICATION", "PUBLISH", "PULL", "PUPIL", "PURPOSE", "PUSH", "PUT", "QUALITY", "QUARTER", "QUESTION", "QUICK", "QUICKLY", "QUIET", "QUITE", "RACE", "RADIO", "RAILWAY", "RAIN", "RAISE", "RANGE", "RAPIDLY", "RARE", "RATE", "RATHER", "REACH", "REACTION", "READ", "READER", "READING", "READY", "REAL", "REALISE", "REALITY", "REALIZE", "REALLY", "REASON", "REASONABLE", "RECALL", "RECEIVE", "RECENT", "RECENTLY", "RECOGNISE", "RECOGNITION", "RECOGNIZE", "RECOMMEND", "RECORD", "RECOVER", "RED", "REDUCE", "REDUCTION", "REFER", "REFERENCE", "REFLECT", "REFORM", "REFUSE", "REGARD", "REGION", "REGIONAL", "REGULAR", "REGULATION", "REJECT", "RELATE", "RELATION", "RELATIONSHIP", "RELATIVE", "RELATIVELY", "RELEASE", "RELEVANT", "RELIEF", "RELIGION", "RELIGIOUS", "RELY", "REMAIN", "REMEMBER", "REMIND", "REMOVE", "REPEAT", "REPLACE", "REPLY", "REPORT", "REPRESENT", "REPRESENTATION", "REPRESENTATIVE", "REQUEST", "REQUIRE", "REQUIREMENT", "RESEARCH", "RESOURCE", "RESPECT", "RESPOND", "RESPONSE", "RESPONSIBILITY", "RESPONSIBLE", "REST", "RESTAURANT", "RESULT", "RETAIN", "RETURN", "REVEAL", "REVENUE", "REVIEW", "REVOLUTION", "RICH", "RIDE", "RIGHT", "RING", "RISE", "RISK", "RIVER", "ROAD", "ROCK", "ROLE", "ROLL", "ROOF", "ROOM", "ROUND", "ROUTE", "ROW", "ROYAL", "RULE", "RUN", "RURAL", "SAFE", "SAFETY", "SALE", "SAME", "SAMPLE", "SATISFY", "SAVE", "SAY", "SCALE", "SCENE", "SCHEME", "SCHOOL", "SCIENCE", "SCIENTIFIC", "SCIENTIST", "SCORE", "SCREEN", "SEA", "SEARCH", "SEASON", "SEAT", "SECOND", "SECONDARY", "SECRETARY", "SECTION", "SECTOR", "SECURE", "SECURITY", "SEE", "SEEK", "SEEM", "SELECT", "SELECTION", "SELL", "SEND", "SENIOR", "SENSE", "SENTENCE", "SEPARATE", "SEQUENCE", "SERIES", "SERIOUS", "SERIOUSLY", "SERVANT", "SERVE", "SERVICE", "SESSION", "SET", "SETTLE", "SETTLEMENT", "SEVERAL", "SEVERE", "SEX", "SEXUAL", "SHAKE", "SHALL", "SHAPE", "SHARE", "SHE", "SHEET", "SHIP", "SHOE", "SHOOT", "SHOP", "SHORT", "SHOT", "SHOULD", "SHOULDER", "SHOUT", "SHOW", "SHUT", "SIDE", "SIGHT", "SIGN", "SIGNAL", "SIGNIFICANCE", "SIGNIFICANT", "SILENCE", "SIMILAR", "SIMPLE", "SIMPLY", "SINCE", "SING", "SINGLE", "SIR", "SISTER", "SIT", "SITE", "SITUATION", "SIZE", "SKILL", "SKIN", "SKY", "SLEEP", "SLIGHTLY", "SLIP", "SLOW", "SLOWLY", "SMALL", "SMILE", "SO", "SOCIAL", "SOCIETY", "SOFT", "SOFTWARE", "SOIL", "SOLDIER", "SOLICITOR", "SOLUTION", "SOME", "SOMEBODY", "SOMEONE", "SOMETHING", "SOMETIMES", "SOMEWHAT", "SOMEWHERE", "SON", "SONG", "SOON", "SORRY", "SORT", "SOUND", "SOURCE", "SOUTH", "SOUTHERN", "SPACE", "SPEAK", "SPEAKER", "SPECIAL", "SPECIES", "SPECIFIC", "SPEECH", "SPEED", "SPEND", "SPIRIT", "SPORT", "SPOT", "SPREAD", "SPRING", "STAFF", "STAGE", "STAND", "STANDARD", "STAR", "START", "STATE", "STATEMENT", "STATION", "STATUS", "STAY", "STEAL", "STEP", "STICK", "STILL", "STOCK", "STONE", "STOP", "STORE", "STORY", "STRAIGHT", "STRANGE", "STRATEGY", "STREET", "STRENGTH", "STRIKE", "STRONG", "STRONGLY", "STRUCTURE", "STUDENT", "STUDIO", "STUDY", "STUFF", "STYLE", "SUBJECT", "SUBSTANTIAL", "SUCCEED", "SUCCESS", "SUCCESSFUL", "SUCH", "SUDDENLY", "SUFFER", "SUFFICIENT", "SUGGEST", "SUGGESTION", "SUITABLE", "SUM", "SUMMER", "SUN", "SUPPLY", "SUPPORT", "SUPPOSE", "SURE", "SURELY", "SURFACE", "SURPRISE", "SURROUND", "SURVEY", "SURVIVE", "SWITCH", "SYSTEM", "TABLE", "TAKE", "TALK", "TALL", "TAPE", "TARGET", "TASK", "TAX", "TEA", "TEACH", "TEACHER", "TEACHING", "TEAM", "TEAR", "TECHNICAL", "TECHNIQUE", "TECHNOLOGY", "TELEPHONE", "TELEVISION", "TELL", "TEMPERATURE", "TEND", "TERM", "TERMS", "TERRIBLE", "TEST", "TEXT", "THAN", "THANK", "THANKS", "THAT", "THE", "THEATRE", "THEIR", "THEM", "THEME", "THEMSELVES", "THEN", "THEORY", "THERE", "THEREFORE", "THESE", "THEY", "THIN", "THING", "THINK", "THIS", "THOSE", "THOUGH", "THOUGHT", "THREAT", "THREATEN", "THROUGH", "THROUGHOUT", "THROW", "THUS", "TICKET", "TIME", "TINY", "TITLE", "TO", "TODAY", "TOGETHER", "TOMORROW", "TONE", "TONIGHT", "TOO", "TOOL", "TOOTH", "TOP", "TOTAL", "TOTALLY", "TOUCH", "TOUR", "TOWARDS", "TOWN", "TRACK", "TRADE", "TRADITION", "TRADITIONAL", "TRAFFIC", "TRAIN", "TRAINING", "TRANSFER", "TRANSPORT", "TRAVEL", "TREAT", "TREATMENT", "TREATY", "TREE", "TREND", "TRIAL", "TRIP", "TROOP", "TROUBLE", "TRUE", "TRUST", "TRUTH", "TRY", "TURN", "TWICE", "TYPE", "TYPICAL", "UNABLE", "UNDER", "UNDERSTAND", "UNDERSTANDING", "UNDERTAKE", "UNEMPLOYMENT", "UNFORTUNATELY", "UNION", "UNIT", "UNITED", "UNIVERSITY", "UNLESS", "UNLIKELY", "UNTIL", "UP", "UPON", "UPPER", "URBAN", "US", "USE", "USED", "USEFUL", "USER", "USUAL", "USUALLY", "VALUE", "VARIATION", "VARIETY", "VARIOUS", "VARY", "VAST", "VEHICLE", "VERSION", "VERY", "VIA", "VICTIM", "VICTORY", "VIDEO", "VIEW", "VILLAGE", "VIOLENCE", "VISION", "VISIT", "VISITOR", "VITAL", "VOICE", "VOLUME", "VOTE", "WAGE", "WAIT", "WALK", "WALL", "WANT", "WAR", "WARM", "WARN", "WASH", "WATCH", "WATER", "WAVE", "WAY", "WE", "WEAK", "WEAPON", "WEAR", "WEATHER", "WEEK", "WEEKEND", "WEIGHT", "WELCOME", "WELFARE", "WELL", "WEST", "WESTERN", "WHAT", "WHATEVER", "WHEN", "WHERE", "WHEREAS", "WHETHER", "WHICH", "WHILE", "WHILST", "WHITE", "WHO", "WHOLE", "WHOM", "WHOSE", "WHY", "WIDE", "WIDELY", "WIFE", "WILD", "WILL", "WIN", "WIND", "WINDOW", "WINE", "WING", "WINNER", "WINTER", "WISH", "WITH", "WITHDRAW", "WITHIN", "WITHOUT", "WOMAN", "WONDER", "WONDERFUL", "WOOD", "WORD", "WORK", "WORKER", "WORKING", "WORKS", "WORLD", "WORRY", "WORTH", "WOULD", "WRITE", "WRITER", "WRITING", "WRONG", "YARD", "YEAH", "YEAR", "YES", "YESTERDAY", "YET", "YOU", "YOUNG", "YOUR", "YOURSELF", "YOUTH"]
    # alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    triangle_numbers = []
    counter = 0
    for i in range(1, 40):
        triangle_numbers += [0.5*i*(i+1)]
    for word in words:
        word_value = 0
        for letter in word:
            word_value += ord(letter) - 64  # alphabet.index(letter) + 1
        if word_value in triangle_numbers:
            counter += 1
    return counter, time.time() - start


print(triangle_words())

# another method using file operation.


def triangle_words():
    start = time.time()
    words = open("../p042_words.txt").read()
    open("../p042_words.txt").close()
    words = words.strip().split(",")
    # alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    triangle_numbers = []
    counter = 0
    for i in range(1, 40):
        triangle_numbers += [0.5 * i * (i + 1)]
    for word in words:
        word_value = 0
        for letter in word:
            if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                word_value += ord(letter) - 64  # alphabet.index(letter) + 1
        if word_value in triangle_numbers:
            counter += 1
    return counter, time.time() - start


print(triangle_words())

# problem 43


def sub_string_divisibility():
    start = time.time()
    p = permutations("0123456789")
    primes = [2, 3, 5, 7, 11, 13, 17]
    total = 0
    for num in p:
        if len(num) == len(set(num)) and \
                all(int(''.join(num[r:r+3])) % primes[r - 1] == 0 for r in range(1, 8)):  # r for range.
            total += int(''.join(num))
    return total, time.time() - start


print(sub_string_divisibility())

# problem 44


def is_pentagonal(num):
    if (1 + (24 * num + 1) ** 0.5) % 6 == 0:
        return True


def perfect_pentagonal_num(limit):
    start = time.time()
    for i in range(2, limit):
        for n in range(1, i):
            pentagonal_i = i*(3*i-1)//2
            pentagonal_n = n*(3*n-1)//2
            if is_pentagonal(pentagonal_i - pentagonal_n) and is_pentagonal(pentagonal_i + pentagonal_n):
                return pentagonal_i - pentagonal_n, time.time() - start


print(perfect_pentagonal_num(10000))

# problem 45

"""
these functions make the problem slower cuz it take some time to call them.
def is_pentagonal(num):
    if (1 + (24 * num + 1) ** 0.5) % 6 == 0:
        return True


def is_hexagonal(num):
    if ((8*num+1)**0.5 + 1) % 4 == 0:
        return True
"""


def t_p_h():  # they're an abbreviation.
    start = time.time()
    for i in range(286, 100000):
        triangle_i = i*(i+1) // 2
        if ((8*triangle_i+1)**0.5 + 1) % 4 == 0 and (1 + (24 * triangle_i + 1) ** 0.5) % 6 == 0:
            return triangle_i, time.time() - start


print(t_p_h())

# problem 46


def is_prime(num):
    """
    all The prime Numbers achieves that (num+1)/6 != 0 and (num-1)/6 != 0 but not vice versa.
    """
    if num % 2 != 0 and all(num % n != 0 for n in range(2,  int(num**0.5 + 1))):
        return True


def gold_bach_conjecture():
    start = time.time()
    """
    primes = [True] * 10000
    primes[0] = False
    primes[1] = False
    primes[2] = True
    for i in range(len(primes)):
        if primes[i]:
            index = 2*i
            while index < len(primes):
                primes[index] = False
                index += i
    for i in range(len(primes)):
        if primes[i]:
            primes[i] = i
    n = 0
    while n < len(primes):
        if not primes[n]:
            primes.remove(primes[n])
        else:
            n += 1
    """
    # primes.reverse()  # to make it ascendant.
    primes = [2]
    for odd_num in range(3, 10000, 2):
        if is_prime(odd_num):
            primes += [odd_num]
        else:
            """
            for i in range(len(primes)):
                if primes[i] < odd_num:
            """
            if all(int(((odd_num-n)/2)**0.5) != ((odd_num-n)/2)**0.5 for n in primes):
                return odd_num, time.time() - start


print(gold_bach_conjecture())

# problem 47


def is_prime(num):
    """
    all The prime Numbers achieves that (num+1)%6 != 0 and (num-1)%6 != 0 but not vice versa.
    """
    if num == 2 or \
            (num % 2 != 0 and ((num+1) % 6 != 0 or (num-1) % 6 != 0) and
             all(num % n != 0 for n in range(2,  int(num**0.5 + 1))) and num != 1):
        return True


def num_of_prime_factors(num):
    wanted_item = 0
    num_of_repetitions = 0
    factors = set()  # all the prime factors
    for n in range(2, int(num**0.5 + 1)):
        while is_prime(n) and num % n == 0:
            factors.add(n)
            num /= n
        if is_prime(num):
            factors.add(int(num))
            break
    """
    for item in factors:
        if factors.count(item) > 1:
            wanted_item = item
            num_of_repetitions = factors.count(item)
            for i in range(factors.count(item)):
                factors.remove(item)
            factors += [str(wanted_item) + "^" + str(num_of_repetitions)]
    """
    return len(factors)


def distinct_factors(num_of_factors, num_of_nums):
    start = time.time()
    for i in range(2, 200000):
        if all(num_of_prime_factors(num) == num_of_factors for num in range(i, i + num_of_nums)):
            return i, time.time() - start
        """
        for num in range(i, i + num_of_nums):
            if not is_prime(num):
                if len(prime_factors(num)) == num_of_factors:
                    all_prime_factors += prime_factors(num)
                    if len(all_prime_factors) != len(set(all_prime_factors)):
                        break
                    elif len(all_prime_factors) == num_of_nums * num_of_factors:
                        return i, time.time() - start
                else:
                    break

        """


print(distinct_factors(4, 4))

# problem 48


def self_powers(limit):
    start = time.time()
    result = 0
    for n in range(1, limit + 1):
        result += n**n
    return str(result)[-10:], time.time() - start


print(self_powers(1000))

# problem 49


def is_prime(num):
    """
    all The prime Numbers achieves that (num+1)%6 != 0 and (num-1)%6 != 0 but not vice versa.
    """
    if num == 2 or \
            (num % 2 != 0 and ((num+1) % 6 != 0 or (num-1) % 6 != 0) and
             all(num % n != 0 for n in range(2,  int(num**0.5 + 1))) and num != 1):
        return True



def sieve(limit):
    is_primes = [True] * limit
    is_primes[0] = False
    is_primes[1] = False
    is_primes[2] = True
    primes = []
    for i in range(3, limit, 2):
        if is_primes[i]:
            index = 2*i
            while index < limit:
                is_primes[index] = False
                index += i
    for i in range(3, limit, 2):
        if is_primes[i]:
            primes += [i]
    return primes


def special_sequence():
    start = time.time()
    primes = sieve(10000)
    for i in primes:
        if i == 1487:
            continue
        if i > 1000:
            for n in primes[primes.index(i) + 1:]:
                if all(digit in str(i) for digit in str(n)) and \
                        all(digit in str(n) for digit in str(i)):
                    if len(str(2*n - i)) == 4 and (2*n - i) in primes and all(digit in str(i) for digit in str(2*n - i)) and \
                            all(digit in str(2*n - i) for digit in str(i)):
                        return int(str(i) + str(n) + str(2*n - i)), time.time() - start


print(special_sequence())

# problem 50


def is_prime(num):
    if num == 2 or (num > 2 and num % 2 != 0 and all(num % i != 0 for i in range(3, int(num**0.5 + 1)))):
        return True


def prime_sum(limit):
    start = time.time()
    primes = [n for n in range(limit//100) if is_prime(n)]
    all_wanted_nums = []
    wanted_num = 0
    while primes:
        t_num = 0
        i = 0
        wanted_num = 0
        wanted_nums = []
        wanted_i = 0
        while t_num < limit and i < len(primes):
            t_num += primes[i]
            wanted_nums += [primes[i]]
            i += 1
            if is_prime(t_num) and t_num < limit:
                wanted_num = t_num
                wanted_i = i
        for n in range(wanted_i + 1, len(wanted_nums)):
            wanted_nums.remove(wanted_nums[wanted_i + 1])
        wanted_nums += [wanted_num]
        all_wanted_nums += [wanted_nums]
        primes.remove(primes[0])
    return max(all_wanted_nums, key=len)[-1], time.time() - start


print(prime_sum(1000000))

# another solution much faster only 0.01 seconds !!!


def is_prime(num):
    if num == 2 or (num > 2 and num % 2 != 0 and all(num % i != 0 for i in range(3, int(num**0.5 + 1)))):
        return True


def sieve(limit):
    is_primes = [True] * limit
    is_primes[0] = False
    is_primes[1] = False
    is_primes[2] = True
    primes = []
    for i in range(3, limit, 2):
        if is_primes[i]:
            index = 2*i
            while index < limit:
                is_primes[index] = False
                index += i
    for i in range(3, limit, 2):
        if is_primes[i]:
            primes += [i]
    return primes


def prime_sum(limit):
    start = time.time()
    max_len = 1
    wanted_num = 0
    primes = sieve(limit//100)  # [n for n in range(limit//10) if is_prime(n)]
    for i in range(len(primes) - 1):
        for n in range(i + max_len, len(primes)):
            t_num = sum(primes[i:n])
            if t_num < limit and is_prime(t_num):
                wanted_num = t_num
                max_len = n - i
            elif t_num > limit:
                break
    return wanted_num, time.time() - start


print(prime_sum(1000000))

# problem 51


def is_prime(num):
    if num == 2 or (num > 2 and num % 2 != 0 and all(num % i != 0 for i in range(3, int(num**0.5 + 1)))):
        return True


def sieve(limit):
    is_primes = [True] * limit
    is_primes[0] = False
    is_primes[1] = False
    primes = [2]
    for i in range(3, limit, 2):
        if is_primes[i]:
            index = 2*i
            while index < limit:
                is_primes[index] = False
                index += i
    for i in range(3, limit, 2):

        if is_primes[i]:
            primes += [i]
    return primes


def prime_replacement(num_of_primes):
    start = time.time()
    primes = sieve(1000000)
    wanted_num = 0
    wanted_digit = ""
    for prime in primes:
        checked_nums = []  # a list for prevent repetition.
        check = 0
        for digit in str(prime):
            check = 0
            if digit not in checked_nums:
                for new_digit in "0123456789":
                    if str(prime).replace(digit, new_digit)[0] != "0" and \
                            is_prime(int(str(prime).replace(digit, new_digit))):
                        check += 1
                if check == num_of_primes:
                    return prime, time.time() - start
            checked_nums += [digit]


print(prime_replacement(8))

# problem 52


def same_digits(num_of_multiplies):
    start = time.time()
    i = 10
    while True:
        n = 2
        check = 1
        while set(str(i)) == set(str(i*n)) and all(str(i).count(digit) == str(i*n).count(digit) for digit in str(i)):
            check += 1
            if check == num_of_multiplies:
                return i, time.time() - start
            n += 1
        i += 1


print(same_digits(6))

# problem 53


def combinatoric_selections(limit):
    start = time.time()
    counter = 0
    for n in range(1, limit 
    + 1):
        for r in range(1, n):
            if f(n) / (f(r)*f(n-r)) > 1000000:
                counter += 1
    return counter, time.time() - start


print(combinatoric_selections(100))

# problem 54
start = time.time()
counter = 0
possibilities = open("p054_poker.txt", "r").read()
possibilities = possibilities.strip().split(" ")
open("p054_poker.txt", "r").close()
for i in range(len(possibilities)+990):
    if len(possibilities[i]) > 2:
        possibilities.insert(i + 1, possibilities[i][3:])
        possibilities[i] = possibilities[i][:2]


def convertor(n):
    if n == "T":
        n = 10
    elif n == "J":
        n = 11
    elif n == "Q":
        n = 12
    elif n == "K":
        n = 13
    elif n == "A":
        n = 14
    return int(n)


def score_of_player(player):
    all_cards_in_order = list("23456789") + ["10", "11", "12", "13", "14"]
    wanted_num = ""
    wanted_num_2 = ""
    wanted_n = ""
    wanted_nums = []
    check_1 = [convertor(n[0]) for n in player]
    check_1.sort()
    for i in range(len(check_1)):
        check_1[i] = str(check_1[i])
    check_2 = [n[1] for n in player]
    # we put it first cuz of flush.
    if len(set(check_1)) == 2:
        for n in check_1:
            if check_1.count(n) == 4:
                wanted_num = n
            elif check_1.count(n) == 3:
                wanted_num_2 = n
        # four of a kind
        if wanted_num:
            return 80, convertor(wanted_num)
        # full house
        elif wanted_num_2:
            return 70, convertor(wanted_num_2)
    elif len(set(check_2)) == 1:
        # royal flush
        if set(check_1) == {"10", "11", "12", "13", "14"}:
            return [100]
        # straight flush
        elif check_1 == all_cards_in_order[all_cards_in_order.index(check_1[0]):all_cards_in_order.index(check_1[-1])+1]:
            return 90, max([convertor(n) for n in check_1])
        # flush
        else:
            return 60, max([convertor(n) for n in check_1])
    # straight
    elif check_1 == all_cards_in_order[all_cards_in_order.index(check_1[0]):all_cards_in_order.index(check_1[-1]) + 1]:
        return 50, max([convertor(n) for n in check_1])
    elif len(set(check_1)) == 3:
        for n in check_1:
            if check_1.count(n) == 3:
                wanted_n = n
                for i in range(3):
                    check_1.remove(n)
            elif check_1.count(n) == 2:
                wanted_nums += [n]
                for i in range(2):
                    check_1.remove(n)
        # three of a kind
        if wanted_n:
            return 40, convertor(wanted_n)
            # two pairs
        elif wanted_nums:
            return 30, max(wanted_nums)
    # one pair
    elif len(set(check_1)) == 4:
        for n in check_1:
            if check_1.count(n) == 2:
                return 20, convertor(n)
    # high card
    else:
        return [max([convertor(n) for n in check_1])]


i = 0
while i <= len(possibilities) - 10:
    score_1 = score_of_player(possibilities[i:i+5])
    score_2 = score_of_player(possibilities[i+5:i+10])
    if score_1[0] > score_2[0]:
        counter += 1
    elif score_1[0] == score_2[0] and len(score_1) > 1:
        if score_1[1] > score_2[1]:
            counter += 1
        elif score_1[1] == score_2[1] and len(score_1) > 2:
            if score_1[2] > score_2[2]:
                counter += 1
    i += 10
print(counter, time.time() - start)

# problem 55
start = time.time()


def is_lychrel(num):
    for i in range(50):
        num += int(str(num)[::-1])
        if num == int(str(num)[::-1]):
            return False
    return True


counter = 0
for i in range(10000):
    if is_lychrel(i):
        counter += 1
print(counter, time.time() - start)

# problem 56


def largest_digital_sum():
    start = time.time()
    max_sum = 0
    for a in range(1, 100):
        for b in range(1, 100):
            t_wanted_nums = list(str(int(a**b)))  # temporarily.
            wanted_nums = [int(n) for n in t_wanted_nums]
            if sum(wanted_nums) > max_sum:
                max_sum = sum(wanted_nums)
    return max_sum, time.time() - start


print(largest_digital_sum())

# problem 57
# a slow solution about 0.02 s


def sq_converges(limit):
    start = time.time()
    counter = 0
    initial_num = Fraction(1, 1)
    for i in range(limit):
        num = Fraction(initial_num.numerator+2*initial_num.denominator, initial_num.numerator+initial_num.denominator)
        initial_num = num
        if len(str(Fraction(num).numerator)) > len(str(Fraction(num).denominator)):
            counter += 1
    return counter, time.time() - start


print(sq_converges(1000))
# a much faster solution


def sqrt_converges(limit):
    start = time.time()
    counter = 0
    p = 1
    q = 1
    for i in range(limit):
        if len(str(p)) > len(str(q)):
            counter += 1
        previous_p = p  # to take the right value of p not the increased one.
        p += 2*q
        q += previous_p
    return counter, time.time() - start


print(sqrt_converges(1000))

# problem 58
"""
up_right the pattern is (n**2 - a) n = 2, 2 a = 1, 2
up_left the pattern is (n**2 + 1) n = 2, 2
down left the pattern is (n**2 + b) n = 2, 2 b = 3, 2
the down right is the squares so it will never be a prime
"""


def is_prime(num):
    if num == 2 or (num > 2 and num % 2 != 0 and ((num+1) % 6 != 0 or (num-1) % 6 != 0) and
                    all(num % n != 0 for n in range(3, int(num**0.5 + 1), 2))):
        return True


def spiral_primes(max_length):
    start = time.time()
    a = 7  # cuz we exceeded the numbers from 1 to 7.
    num_of_prime_items = 8
    all_nums = 13
    for i in range(8, max_length, 2):
        if is_prime(i**2 - a):  # up right the pattern is (n**2 - a) n = 2, 2 a = 1, 2 
            num_of_prime_items += 1
        if is_prime(i**2 + 1):  # up left the pattern is (n**2 + 1) n = 2, 2
            num_of_prime_items += 1
        if is_prime(i**2 + 2 + a):  # down left the pattern is (n**2 + b) n = 2, 2 b = 3, 2
            num_of_prime_items += 1
        a += 2
        all_nums += 4
        if num_of_prime_items / all_nums < 0.1:
            return i + 1, time.time() - start


print(spiral_primes(500000))

# problem 59
file = open("p059_cipher.txt", "r")
t_encrypted_text = file.read().split(",")
file.close()
encrypted_text = [int(n) for n in t_encrypted_text]


def check_english(ascii1, ascii2):
    if 31 < ascii1 ^ ascii2 < 91 or 96 < ascii1 ^ ascii2 < 123:
        return True
    return False


def the_key(encrypted):
    first_letter, second_letter, third_letter = "", "", ""
    for letter in range(97, 123):
        if all(check_english(encrypted[i], letter) for i in range(0, len(encrypted), 3)):
            first_letter = chr(letter)
        if all(check_english(encrypted[i], letter) for i in range(1, len(encrypted), 3)):
            second_letter = chr(letter)
        if all(check_english(encrypted[i], letter) for i in range(2, len(encrypted), 3)):
            third_letter = chr(letter)
    return first_letter + second_letter + third_letter


def ascii_sum():
    total = 0
    key = the_key(encrypted_text)
    """
    for i in range(len(encrypted_text)):
        total += ord(key[i % 3]) ^ encrypted_text[i]
    """
    return key, ''.join(chr(ord(key) ^ encrypted_text[i]) for i in range(0, len(encrypted_text), 3))


print(ascii_sum())

# problem 60
def is_prime(num):
    if num == 2 or (num > 2 and num % 2 != 0 and ((num+1) % 6 != 0 or (num-1) % 6 != 0) and
                    all(num % i != 0 for i in range(3, int(num**0.5 + 1), 2))):
        return True


def prime_sieve(limit):
    is_primes = [True] * limit
    is_primes[0] = False
    is_primes[1] = False
    primes = [2]
    for i in range(3, limit, 2):
        if is_primes[i]:
            index = 2*i
            while index < limit:
                is_primes[index] = False
                index += i
    primes += [i for i in range(3, limit, 2) if is_primes[i]]
    return primes


def smallest_sum():
    start = time.time()
    primes = prime_sieve(10000)[1:]
    for f_prime in primes:
        for s_prime in primes[primes.index(f_prime) + 1:]:
            if is_prime(int(str(f_prime) + str(s_prime))) and is_prime(int(str(s_prime) + str(f_prime))):
                for t_prime in primes[primes.index(s_prime) + 1:]:
                    if is_prime(int(str(f_prime) + str(t_prime))) and is_prime(int(str(t_prime) + str(f_prime))) and \
                       is_prime(int(str(t_prime) + str(s_prime))) and is_prime(int(str(s_prime) + str(t_prime))):
                        for fourth_prime in primes[primes.index(t_prime) + 1:]:
                                if is_prime(int(str(f_prime) + str(fourth_prime))) and \
                                        is_prime(int(str(fourth_prime) + str(f_prime))) and \
                                        is_prime(int(str(fourth_prime) + str(s_prime))) and \
                                        is_prime(int(str(s_prime) + str(fourth_prime))) and \
                                        is_prime(int(str(fourth_prime) + str(t_prime))) and \
                                        is_prime(int(str(t_prime) + str(fourth_prime))):
                                    for fifth_prime in primes[primes.index(fourth_prime) + 1:]:
                                        if is_prime(int(str(fifth_prime) + str(f_prime))) and \
                                                is_prime(int(str(f_prime) + str(fifth_prime))) and \
                                                is_prime(int(str(fifth_prime) + str(s_prime))) and \
                                                is_prime(int(str(s_prime) + str(fifth_prime))) and \
                                                is_prime(int(str(fifth_prime) + str(t_prime))) and \
                                                is_prime(int(str(t_prime) + str(fifth_prime))) and \
                                                is_prime(int(str(fifth_prime) + str(fourth_prime))) and \
                                                is_prime(int(str(fourth_prime) + str(fifth_prime))):
                                            return f_prime + s_prime + t_prime + fourth_prime + fifth_prime, time.time() - start


print(smallest_sum())

# problem 61


def cyclical_figurate_nums():
    start = time.time()
    triangle_nums = [int(n*(n+1)/2) for n in range(1, 150) if 1000 < int(n*(n+1)/2) < 10000]
    square_nums = [int(n**2) for n in range(150) if 1000 < int(n**2) < 10000]
    pentagonal_nums = [int(n*(3*n - 1)/2) for n in range(1, 150) if 1000 < int(n*(3*n - 1)/2) < 10000]
    hexagonal_nums = [int(n*(2*n-1)) for n in range(1, 150) if 1000 < int(n*(2*n-1)) < 10000]
    heptagonal_nums = [int(n*(5*n-3)/2) for n in range(1, 150) if 1000 < int(n*(5*n-3)/2) < 10000]
    octagonal_nums = [int(n*(3*n-2)) for n in range(1, 150) if 1000 < int(n*(3*n-2)) < 10000]
    t_s_p_h_h = [triangle_nums, square_nums, pentagonal_nums, hexagonal_nums, heptagonal_nums]
    for o in octagonal_nums:
        for i in t_s_p_h_h:
            for n in i:
                if str(o)[2:] == str(n)[:2]:
                    for i_2 in t_s_p_h_h:
                        if i_2 != i:
                            for n_2 in i_2:
                            
                                if str(n)[2:] == str(n_2)[:2]:
                                    for i_3 in t_s_p_h_h:
                                        if i_3 != i and i_3 != i_2:
                                            for n_3 in i_3:
                                                if str(n_2)[2:] == str(n_3)[:2]:
                                                    for i_4 in t_s_p_h_h:
                                                        if i_4 != i and i_4 != i_2 and i_3 != i_4:
                                                            for n_4 in i_4:
                                                                if str(n_3)[2:] == str(n_4)[:2]:
                                                                    for i_5 in t_s_p_h_h:
                                                                        if i_5 != i and i_5 != i_2 and i_5 != i_3 and \
                                                                                i_5 != i_4:
                                                                            for n_5 in i_5:
                                                                                if str(n_4)[2:] == str(n_5)[:2] and \
                                                                                        str(n_5)[2:] == str(o)[:2]:
                                                                                    return sum((o, n, n_2, n_3, n_4,
                                                                                                n_5)), \
                                                                                           time.time() - start


print(cyclical_figurate_nums())

# problem 62
# A very slow solution


def is_permuted(p_1, p_2):
    if len(str(p_1)) == len(str(p_2)) and all(str(p_2).count(n) == str(p_1).count(n) for n in str(p_1)):
        return True


def cyclic_permutations():
    start = time.time()
    all_cubes = [int(n**3) for n in range(300, 10000)]
    for i in range(len(all_cubes)):
        for n in range(i + 1, len(all_cubes)):
            if is_permuted(all_cubes[i], all_cubes[n]):
                for p in range(n + 1, len(all_cubes)):
                    if is_permuted(all_cubes[i], all_cubes[p]):
                        for j in range(p + 1, len(all_cubes)):
                            if is_permuted(all_cubes[i], all_cubes[j]):
                                for k in range(j + 1, len(all_cubes)):
                                    if is_permuted(all_cubes[i], all_cubes[k]):
                                        return all_cubes[i], time.time() - start


print(cyclic_permutations())

# A faster one
start = time.time()
i = 0
cubes = []
while True:
    cube = sorted(str(i**3))
    cubes.append(cube)
    if cubes.count(cube) == 5:
        print(cubes.index(cube)**3, time.time() - start)  # index returns the first position.
        break
    i += 1

# problem 63


def digit_powers():
    start = time.time()
    counter = 0
    for i in range(1, 10):
        for n in range(1, 100):
            if len(str(i**n)) == n:
                counter += 1
            elif n > len(str(i**n)):
                break
    return counter, time.time() - start


print(digit_powers())

# problem 64
"""
# this will return a wrong answer at some points above 100
def c_f(n):
    decimal = n**0.5
    integer = int(decimal)
    periods = []
    if integer != decimal:
        while integer != 2*int(n**0.5):
            decimal = 1 / (decimal - integer)
            integer = int(decimal)
            periods += [integer]
    return periods


print(c_f(23))
"""
start = time.time()


def cf(n):
    mn = 0.0
    dn = 1.0
    a0 = int(n**0.5)
    an = int(n**0.5)
    period = 0
    if a0 != n**0.5:
        while an != 2*a0:
            mn = dn*an - mn
            dn = (n - mn**2)/dn
            an = int((a0 + mn)/dn)
            period += 1
    return period


counter = 0
for i in range(10001):
    if cf(i) % 2 != 0:
        counter += 1
print(counter, time.time() - start)

# problem 65


def convergence_of_e(wanted_convergent):
    start = time.time()
    e = [2]
    i = 1
    while len(e) < wanted_convergent:
        e.extend([1, 2*i, 1])
        i += 1
    convergent = Fraction(1, e.pop())
    for i in e[::-1]:
        convergent = Fraction(1, convergent + i)
    convergent = Fraction(1, convergent)
    return sum([int(digit) for digit in str(convergent.numerator)], time.time() - start)


print(convergence_of_e(100))


# problem 17
start = time.time()
count = 11
for i in range(1000):
    o = int(str(i)[-1]) # o for ones. # be very careful 300 3 here is [0].
    
    if o == 1 or o == 2 or o == 6:
        count += 3
    elif o == 4 or o == 5 or o == 9:
        count += 4
    elif o != 0: 
        count += 5

    if i > 9 :
        if i <= 99 :
            t = int(str(i)[0]) # t for tens.
        else :
            t = int(str(i)[1]) # t for tens. 
        if t == 1 :
            if o == 0 or o == 1 or o == 2 or o == 3 or o == 5 or o == 8:
                count += 3
            else :
                count += 4
        elif t == 2 or t == 3 or t == 8 or t == 9 :
            count += 6
        elif t == 4 or t == 5 or t == 6 :
            count += 5
        elif t != 0 :  # as t can be zero in numbers like 100.
            count += 7
    
    if i > 99 :
        count += 7 # considering the word "hundred".
        if t != 0 or o != 0 :
            count += 3 # considering the word "and".
        h = int(str(i)[0]) # h for hunderds.
        if h == 1 or h == 2 or h == 6:
            count += 3
        elif h == 4 or h == 5 or h == 9:
            count += 4
        else: 
            count += 5

print(count, time.time() - start)

# problem 18

num = "75 95 64 17 47 82 18 35 87 10 20 4 82 47 65 19 1 23 75 3 34 88 2 77 73 7 63 67 99 65 4 28 6 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 4 68 89 53 67 30 73 16 69 87 40 31 4 62 98 27 23 9 70 98 73 93 38 53 60 4 23"
t_nums = num.split(" ") # t for temporary as it's just a place holder.
t_nums = [int(num) for num in t_nums]
nums = []

for i in range(1, 16):
    nums.extend([t_nums[0:i]])
    for j in range (0, i):
        t_nums.remove(t_nums[0]) # as the list is reducing so it's 15 then 14 ...13...12.

while (len(nums) > 1):
    j = -1
    while (len(nums[-1]) > -j):
        nums[-2][j] += max(nums[-1][j], nums[-1][j-1])
        j -= 1
    nums.pop()

print(nums[0][0])


# problem 19

def is_leap(year):
    if str(year)[-2:] == "00":
        if year % 400 == 0:
            return 1
    elif year % 4 == 0:
        return 1
    return 0

y = 1900
d = 1
n_d = 3 # stands for the name of the day.  
m = 1
counter = 0

while (y < 2001):
    if n_d > 7:
        n_d = 1
    if m == 2:
        if is_leap(y):
            if d > 29:
                m += 1
                d = 1
        else:
            if d > 28:
                m += 1
                d = 1
    elif m in [4, 6, 9, 11]:
        if d > 30:
            m += 1
            d = 1
    else:
        if d > 31:
            m += 1
            d = 1
    if m == 13 :
        y += 1
        m = 1
    if n_d == 2 and d == 1 and y > 1900:
        counter += 1
    d += 1
    n_d += 1
    
print (counter)

# problem 20

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result    
        
print(sum([int(d) for d in str(factorial(100))]))
'''
# problem 21

def d(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum


start = time.time() 
nums = set()
for i in range(2, 10000):
    if i == d(d(i)) and i != d(i):
        nums.add(i)
        nums.add(d(d(i)))


print(nums, time.time() - start)
