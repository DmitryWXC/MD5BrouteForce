import hashlib
import time

def hesher(string_):

	# Вычисление MD5-хеша
	md5_hash = hashlib.md5(string_.encode()).hexdigest()
	return md5_hash

print(hesher("1234567"))

def start(target_hash, min_, max_):
	print(f"Брутфорс хеша {target_hash} начат.\nДля остановки нажмите CTRL+C")
	try:
		for i in range(min_, max_):
			if hesher(str(i)) == target_hash:
				print(f"Хеш найден! Значение: {i}")
				return True
	except KeyboardInterrupt:
		print("Остановлено!"); return False
	return False


def main():
	while True:
		print("Укажите хеш для брутфорса")
		target_hash = input(">> ").strip()
		if not target_hash:
			print("Хеш не может быть пустым!")
			continue
		while True:
			min_ = input("Укажите минимальное число для начала брутфорса: ").strip()
			try:
				min_ = int(min_)
				if min_ < 0:
					print("Ошибка! Минимальное число не может быть меньше нуля.")
					continue
			except Exception as e:
				print("Ошибка! Неверно указано число.")
				continue
			max_ = input("Укажите максимальное число для брутфорса: ").strip()
			try:
				max_ = int(max_)
				if max_ > 1000000000:
					print("Ошибка! Максимальное число не может быть больше 1.000.000.000.")
					continue
			except Exception as e:
				print("Ошибка! Неверно указано число.")
				continue
			if not start(target_hash, min_, max_):
				print("Не удалось найти значение хеша.")
				break

if __name__ == '__main__':
	main()
