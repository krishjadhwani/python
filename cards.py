from enum import Enum 
import itertools, random

class Suite(Enum):
	CLUBS = 1
	DIAMONDS = 2
	HEARTS = 3 
	SPADES = 4

class CardGame:
	def __init__(self):
		self.deck = list(itertools.product(range(1, 14), list(Suite)))
	def deal(self, numCards):
		cards = []
		i = 0
		while(i < numCards):
			cards.append(self.deck.pop())
			i+=1
		return cards

	def shuffle(self):
		random.shuffle(self.deck)

	def printDeck(self):
		for card in self.deck:
			print(card)
	def deckType(self):
		print(type(self.deck))

def getHighCard(cards):
	print(cards)
	cards = sorted(cards, key=lambda card: card[1].value)
	cards = sorted(cards, key=lambda card: card[0])
	return cards[-1]

if __name__ == '__main__':
	cardGame = CardGame()
	cardGame.shuffle()
	hand = cardGame.deal(7)
	hand2 = cardGame.deal(7)
	high = getHighCard(hand)
	high2 = getHighCard(hand2)
	highest = getHighCard([high, high2])
	if highest == high:
		print('hand 1 wins: ', high, high2)
	else:
		print('hand 2 wins,', high, high2)