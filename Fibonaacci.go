//This is the implementation of a Numerical Fibonacci Serie in Golang
//Using Recursion

package numerical

func fib(num int)int{
  if num <= 1{
    return num
  }
  return fibo(num -1) + fibo(num - 2)
}
