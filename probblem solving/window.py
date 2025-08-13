def maximum_sum(arr,k):
    max_window_count=0
    current_window_count=0
    back_window_count=0
#used two pointer method to reduce loop counts

    j=len(arr)
    loop_count=0
    for i in range(0,j):
        loop_count+=1
        j-=1
        print(f"i[{i}]:",arr[i])
        print(f"j[{j}]:",arr[j])
        print()
        current_window_count+=arr[i]
        back_window_count+=arr[j]
        if i>j+1:
            break
        if i>=k-1 or j<=j-k+1:
            max_window_count=max(max_window_count,current_window_count,back_window_count)
            print("arr[i-k+1]: ",arr[i-k+1])
            print("arr[j+k-1]: ",arr[j+k-1])
            print("front_window_count : ",current_window_count)
            print("back_window_count : ",back_window_count)
            current_window_count-=arr[i-k+1]
            back_window_count-=arr[j+k-1]
    return f"RESULT :  *****************      (  {max_window_count},{loop_count}   )******************\n\n"

print(maximum_sum([10,12,40,8,9,9,3,4,5,9,0,20,20,3,4,5,9,3,4,10,11],4))
print(maximum_sum([10,12,1,10,12],2))