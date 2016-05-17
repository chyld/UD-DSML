def odds(nums):
    fn = lambda x : x % 2
    return filter(fn, nums)

ns1 = range(1, 20)
ns2 = list(odds(ns1))

print('***> ns2: {0}'.format(ns2))
