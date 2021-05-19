def order(items):
	print(sorted(items, key=lambda x:(x[0],int(x[1:]))))




order(['a1', 'b20', 'c1', 'd5', 'a3', 'b1', 'd11', 'b3'])