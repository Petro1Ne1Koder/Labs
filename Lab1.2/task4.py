import sys

class File:

	def __init__(self, file):
		try:
			open_file=open(file, 'rt')
		except (IOError,FileNotFoundError):
			open_file.close()
			sys.exit()
		self.number_of_charachters=self.number_of_words=self.number_of_sentences=0
		self.file=file

	def count_charachters(self):
		open_file=open(self.file, 'rt')
		for line in open_file:
			self.number_of_charachters+=len(line)
		open_file.close()
		return self.number_of_charachters

	def count_words(self):
		open_file=open(self.file, 'rt')
		index=''
		punctuation='.!?,;-()"	: '
		for line in open_file:
			for i in line:
				if i in punctuation and index not in punctuation:
					self.number_of_words+=1
				index=i
		open_file.close()
		return self.number_of_words

	def count_sentences(self):
		open_file=open(self.file, 'rt')
		index=0
		punctuation='.!?'
		for line in open_file:
			for i in line:
				if i in punctuation and index==0:
					index=1
					self.number_of_sentences+=1
				elif i not in punctuation and i!=' ' and i!='	':
					index=0
		open_file.close()
		return self.number_of_sentences

statistic=File('words.txt')
print('Number of charachters: ',statistic.count_charachters(),'\nNumber of words: ',
	statistic.count_words(),'\nNumber of sentences: ',statistic.count_sentences())