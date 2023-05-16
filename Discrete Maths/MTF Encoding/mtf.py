from typing import List
from string import ascii_lowercase
import treap

SYMBOLTABLE = list(ascii_lowercase)


def binary_search(arr, low, high, x):
	if high >= low:
		mid = (high + low) // 2
		if arr[mid] == x:
			return mid
		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)
		else:
			return binary_search(arr, mid + 1, high, x)
	else:
		return -1


def move2front_encode(strng, symboltable):
	sequence, pad = [], symboltable[::]
	help_pad = [ord(x) for x in pad]
	for char in strng:
		indx = pad.index(char)
		sequence.append(indx)
		pad = [pad.pop(indx)] + pad
	return sequence


def move2front_decode(sequence, symboltable):
	chars, pad = [], symboltable[::]
	for indx in sequence:
		char = pad[indx]
		chars.append(char)
		pad = [pad.pop(indx)] + pad
	return ''.join(chars)


def m2f_e(strng: str):
	t = treap.treap()
	result = []

	for i in range(len(strng)):
		t[i] = ord(s[i])

	for i in range(len(strng)):
		result.append(str(t.find_node(i)))


if __name__ == '__main__':
	for s in ['broood', 'bananaaa', 'hiphophiphop']:
		encode = move2front_encode(s, SYMBOLTABLE)
		print('%14r encodes to %r' % (s, encode), end=', ')
		decode = move2front_decode(encode, SYMBOLTABLE)
		print('which decodes back to %r' % decode)
		assert s == decode, 'Whoops!'
