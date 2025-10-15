import hashlib
import time

def hesher(string_):

	# Mathing MD5 hash
	md5_hash = hashlib.md5(string_.encode()).hexdigest()
	return md5_hash

def start(target_hash, min_, max_):
	print(f"Breuteforce hash {target_hash} started.\nPress CTRL+C for stop it.")
	try:
		for i in range(min_, max_):
			if hesher(str(i)) == target_hash:
				print(f"Success! Result: {i}")
				return True # Success result
	except KeyboardInterrupt:
		print("Stoping!!"); return False # Not result
	return False # Not result


def main():
	while True:
		print("Please, input your hash for brouteforce (MD5)")
		target_hash = input(">> ").strip()
		if not target_hash:
			print("Hash cannot be empty!")
			continue
		while True:
			min_ = input("Input min. number for brouteforce: ").strip()
			try:
				min_ = int(min_)
				if min_ < 0:
					print("Error!The min. number cannot be less than zero")
					continue
			except Exception as e:
				print("Error! Incorrect number")
				continue
			max_ = input("Input max. number for brouteforce: ").strip()
			try:
				max_ = int(max_)
				if max_ > 1000000000:
					print("Error! The max. number cannot be more than 1,000,000,000.")
					continue
			except Exception as e:
				print("Error! Incorrect number")
				continue
			if not start(target_hash, min_, max_):
				print("The hash value could not be found.")
				break

if __name__ == '__main__':
	main()
