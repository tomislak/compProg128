#!/usr/bin/python3

from ourQueue import OurQueue

red = OurQueue()

red.push('1')
red.push('2')
red.push('3')
print(red.pop())
red.push('4')
red.push('5')
print(red.pop())
red.push('6')
print(red.pop())
