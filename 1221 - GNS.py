dic = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}
dic2 = {0:'ZRO', 1:'ONE', 2:'TWO', 3:'THR', 4:'FOR', 5:'FIV', 6:'SIX', 7:'SVN', 8:'EGT', 9:'NIN'}
T = int(input())
for tc in range(1, T+1):
  num, length = map(str, input().split())
  length = int(length)
  test_str = list(map(str, input().split()))
  result = []
  for t in test_str:
    result.append(dic[t])
  result.sort()
  print(num)
  for r in result:
    print(dic2[r], end=' ')