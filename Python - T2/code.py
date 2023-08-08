"""
get_sum(x) gibt die summe der beiden vorherigen zahlen aus
(außer wenn x kleiner als 1 ist, dann wird x ausgegeben (0 oder 1))
z.b.
get_sum(3) 
-> get_sum(2)                + get_sum(1) 
-> (get_sum(1) + get_sum(0)) + 1 
-> (1 + 0)                   + 1 
-> 2

get_fibo_nrs(n) wendet get_sum auf jedes element von 0 ... n+2 an 
(n+2 weil die ersten beiden fibonacci zahlen 0 und 1 sind)
zurückgegeben wird eine liste mit allen zahlen die höchstens n sind
(= alle fibonacci zahlen bis n)
"""
get_sum = lambda x: x if x <= 1 else get_sum(x-1) + get_sum(x-2)
get_fibo_nrs = lambda n: [i for i in map(get_sum, range(n+2)) if i <= n]


print(get_fibo_nrs(0))  # [0]
print(get_fibo_nrs(1))  # [0, 1, 1]
print(get_fibo_nrs(3))  # [0, 1, 1, 2, 3]
print(get_fibo_nrs(10)) # [0, 1, 1, 2, 3, 5, 8]
print(get_fibo_nrs(13)) # [0, 1, 1, 2, 3, 5, 8, 13]