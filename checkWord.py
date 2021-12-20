from uzwords import words
from difflib import get_close_matches

def checkWord(word,words=words):
	word = word.lower()
	matches = set(get_close_matches(word, words))
	available = False 

	if word in matches:
		available = True
		matches = word
	

	return {"available": available, "matches":matches}

if __name__ == "__main__":


	print(checkWord("вабо" ))
	print(checkWord("садф"))
	print(checkWord("алас-алак"))
	print(checkWord("пат" ))