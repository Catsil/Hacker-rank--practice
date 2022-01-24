n=int(input('enter cant scores'))
arr=map(int,input('valores').split())

arr=set(arr)
arr=list(arr)

#arr.sort(reverse=True)

score=max(arr)
arr.remove(score)

h_run=max(arr)

print(h_run)



