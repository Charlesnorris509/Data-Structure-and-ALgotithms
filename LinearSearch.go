//This is the implementation of a Searching Algorithm
// IN GOLANG - LinearSearch


package main

import "fmt"

func LinSearch(arr []int, key int)int {
  for i := 0; i < len(arr); i++{
    if arr[i] == key{
      return i
    }
  }
  return -1
}
