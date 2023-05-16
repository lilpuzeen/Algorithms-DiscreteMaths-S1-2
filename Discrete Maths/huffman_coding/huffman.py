from PIL import Image
from huff import *
from pprint import pprint

if __name__ == '__main__':
	penguin = Image.open("dig10k_penguin.bmp")
	penguin_colors = list(penguin.getcolors())
	penguin_hash = {str(penguin_colors[i][1]): penguin_colors[i][0] for i in range(len(penguin_colors))}

	fish = Image.open("dig10k_penguin.bmp")
	fish_colors = list(fish.getcolors())
	fish_hash = {str(fish_colors[i][1]): fish_colors[i][0] for i in range(len(fish_colors))}

	penguin_hash_sorted = sorted(penguin_hash.items(), key=lambda x: x[1], reverse=True)
	node = make_tree(penguin_hash_sorted)
	encoding = huffman_code_tree(node)
	print("Penguin Picture")
	for i in encoding:
		print(f'{i} : {encoding[i]}')

	print()

	fish_hash_sorted = sorted(fish_hash.items(), key=lambda x: x[1], reverse=True)
	node = make_tree(fish_hash_sorted)
	encoding = huffman_code_tree(node)
	print("Fish Picture")
	for i in encoding:
		print(f'{i} : {encoding[i]}')

	print()
	pprint(f"Frequencies Penguin: {penguin_hash}")
	print()
	pprint(f"Frequencies Fish: {fish_hash}")
