class IterClass(object):
	def __init__(self, values):
		self.values = values
		self.index = -1
		pass

	def next(self):
		self.index += 1
		if self.index >= len(self.values):
			raise StopIteration
		
		return self.values[self.index]

	def __iter__(self):
		return self


if __name__ == "__main__":
	l = [1,2, 3]
	ic = iter(IerClass(l))
	for i in ic:
		print i


