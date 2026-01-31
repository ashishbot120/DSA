
def fibonacci(n):
    Fn={0:0,1:1}
    if n in Fn:
        return Fn[n]
    else:
        Fn[n]=fibonacci(n-1) + fibonacci(n-2)
        return Fn[n]
            
# Example usage:
n = 10
result = fibonacci(n)
print(result)
# Output: 55
#time complexity: O(n) due to memoization storing previously computed Fibonacci numbers
#space complexity: O(n) for the memoization dictionary storing Fibonacci numbers up to n