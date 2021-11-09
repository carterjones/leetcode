package main

import (
	"fmt"
	"log"
	"math/big"
	"strconv"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

func arrToListNode(arr []int) *ListNode {
	var current, next *ListNode
	for i := len(arr) - 1; i >= 0; i-- {
		v := arr[i]
		current = &ListNode{v, next}
		next = current
	}
	return current
}

func listNodeToBigInt(node *ListNode) *big.Int {
	if node == nil {
		return nil
	}
	val := big.NewInt(int64(node.Val))
	next := listNodeToBigInt(node.Next)
	if next == nil {
		return val
	} else {
		// Multiply the next value by 10, since it is in the next tens place.
		next.Mul(big.NewInt(10), next)

		// Add the result to the current value.
		val.Add(val, next)

		// Pass along the final value.
		return val
	}
}

func Reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func bigIntToListNode(bi *big.Int) *ListNode {
	s := bi.String()
	reversed := Reverse(s)
	arr := []int{}
	for _, c := range reversed {
		digit, err := strconv.Atoi(string(c))
		if err != nil {
			log.Fatal(err)
		}
		arr = append(arr, digit)
	}
	return arrToListNode(arr)
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	n1 := listNodeToBigInt(l1)
	n2 := listNodeToBigInt(l2)
	val := new(big.Int)
	val.Add(n1, n2)
	return bigIntToListNode(val)
}

func nodesEqual(n1, n2 *ListNode) bool {
	if n1 == nil && n2 == nil {
		return true
	}
	if n1 == nil || n2 == nil {
		return false
	}
	if n1.Val != n2.Val {
		return false
	}
	return nodesEqual(n1.Next, n2.Next)
}

func print_result(name string, res, exp *ListNode) {
	fmt.Printf("%v: ", name)
	if nodesEqual(res, exp) {
		fmt.Println("success")
	} else {
		fmt.Println("failed")
	}
}

func main() {
	var testCases = []struct {
		l1   []int
		l2   []int
		exp  []int
		name string
	}{
		{
			[]int{2, 4, 3},
			[]int{5, 6, 4},
			[]int{7, 0, 8},
			"case 1",
		},
		{
			[]int{0},
			[]int{0},
			[]int{0},
			"case 2",
		},
		{
			[]int{9, 9, 9, 9, 9, 9, 9},
			[]int{9, 9, 9, 9},
			[]int{8, 9, 9, 9, 0, 0, 0, 1},
			"case 3",
		},
	}

	for _, v := range testCases {
		l1 := arrToListNode(v.l1)
		l2 := arrToListNode(v.l2)
		res := addTwoNumbers(l1, l2)
		exp := arrToListNode(v.exp)
		print_result(v.name, res, exp)
	}
}
