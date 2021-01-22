def Sum(n):
    odd_sum = 0
    even_sum =  0
    
    for i in range(len(n)):
        if i%2 ==0:
            even_sum += int(n[i])
        else:
            odd_sum += int(n[i])
    ans = odd_sum + even_sum
    return ans

if __name__ == "__main__":
    t = int(input())
    for j in range(0,t):
        n = [int(x) for x in input()]
        
        print(Sum(n))