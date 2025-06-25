n, m, a, b = [int(i) for i in input().split(' ')]

general_cost_for_n_rides = n * a
special_cost_for_one_ride = b/m
general_cost_for_one_ride = a

if special_cost_for_one_ride >= a:
    print(general_cost_for_n_rides)
elif m==1 and a==b:
    print(b * n)
elif m*b < n*a and m>n:
    print(b)
else:
    if n % m == 0:
        print(b * n//m)
    else:
        rem = n % m
        _sum = (n // m) * b
        _sum += rem*a if a < b else b
        print(_sum)