# # 178p 위에서 아래로
# n=int(input())
# num=[]
# for i in range(n):
#     num.append(int(input()))
# num.sort(reverse=True)
# for i in (num):
#     print(i,end=" ")

# # 180p 성적이 낮은 순서로 학생 출력하기
# n=int(input())
# array=[]
# for i in range(n):
#     input_data=input().split()
#     array.append((input_data[0],int(input_data[1])))
    
# array=sorted(array,key=lambda student: student[1])

# for student in array:
#     print(student[0], end=' ')

# # 182p 두 배열의 원소 교체
# n,k=map(int,input().split())
# a=list(map(int,input().split()))
# b=list(map(int,input().split()))
# a.sort(reverse=True)
# b.sort(reverse=True)
# a_result=a[:n-k]
# b_result=b[:k]
# print(sum(a_result)+sum(b_result))