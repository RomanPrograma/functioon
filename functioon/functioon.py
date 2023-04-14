
try:
   import statistics
   list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   list_avarange = statistics.mean(list)
   print(f'avarange: {list_avarange}')
except Exception as e:
    print(f'error: {e}')

try:
    def list_av(list):
        var = int(input())
        l = list(range(1, var + 1))
        for x in l:
            x = int(input('['+ str(x) + ']: '))
        return l
except Exception as e:
    print(f'error: {e}')

