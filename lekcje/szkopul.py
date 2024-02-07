# Zadanie 8WST – Wstawianie liczb
# Dane jest 10 liczb. Wstaw pierwszą liczbę przed najwcześniejszą większą od niej.
# Wejście
# W wierszu 10 liczb z zakresu od 1 do 1000.
# Wyjście
# 10 liczb, gdzie pierwsza jest przestawiona i wstawiona przed pierwszą większą od niej.
# Przykład
# Dla danych
# 10 1 8 5 7 11 8 2 12 8
#  poprawna odpowiedź to
# 1 8 5 7 10 11 8 2 12 8
# n = [10, 1, 8, 5, 7, 11, 8, 2, 12, 8]
# first_num = n[0]
# greater_index = next((i for i, num in enumerate(numbers) if num > first_num), None)
# if greater_index is not None:
#     n.insert(greater_index, n.pop(0))
# print(n)


# Napisz program, który dla podanej na standardowym wejściu liczby całkowitej n, narysuje
# szachownicę z cyfr 0 i 1 o boku n.
# Wejście
# Jedyny wiersz danych zawiera liczbę całkowitą n (1 ≤ n ≤ 200).
# Wyjście
# Program powinien wypisać szachownicę o wielkości n. 
def draw_chessboard(n):
	for i in range(n):
		row = ''
		for j in range(n):
			if (i + j) % 2 == 0:
				row += '1'
			else:
				row += '0'
		print(row)
print(draw_chessboard(6))




    