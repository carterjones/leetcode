package main

import (
	"fmt"
	"reflect"
)

func twoSum(nums []int, target int) []int {
	nums_set := make(map[int]int)
	for i, v := range nums {
		complement := target - v
		if val, ok := nums_set[complement]; ok {
			return []int{val, i}
		}
		nums_set[v] = i
	}

	return nil
}

func print_result(name string, res, exp []int) {
	fmt.Printf("%v: ", name)
	if reflect.DeepEqual(res, exp) {
		fmt.Println("success")
	} else {
		fmt.Println("failed")
	}
}

func main() {
	var testCases = []struct {
		in     []int
		target int
		exp    []int
		name   string
	}{
		{
			[]int{2, 7, 11, 15},
			9,
			[]int{0, 1},
			"case 1",
		},
		{
			[]int{3, 2, 4},
			6,
			[]int{1, 2},
			"case 2",
		},
		{
			[]int{3, 3},
			6,
			[]int{0, 1},
			"case 3",
		},
	}

	for _, v := range testCases {
		res := twoSum(v.in, v.target)
		print_result(v.name, res, v.exp)
	}
}
