import random
import sys


class Suit:
    Club = 0
    Diamond = 1
    Heart = 2
    Spade = 3

    def __init__(self):
        pass

    def get_suit(self):
        value = random.randint(0, 4)
        return self.get_suit_from_value(value)

    def get_suit_from_value(self, value):
        if value == 0:
            return Suit.Club
        elif value == 1:
            return Suit.Diamond
        if value == 2:
            return Suit.Heart
        if value == 3:
            return Suit.Spade


class Card:
    """
    Card
    """
    def __init__(self, c, s):
        """
        number or face that's on card - a number 2 through 10, or 11 for Jack, 12 for Queen, 13 for King, or 1 for Ace

        :param c:
        :param s:
        """
        self.__face_value = c
        self.__suit = s
        self.__available = True

    def get_face_value(self):
        return self.__face_value

    def get_suit(self):
        return self.__suit

    def is_available(self):
        """
        returns whether or not the card is available to be given out to someone

        :return:
        """
        return self.__available

    def mark_unavailable(self):
        self.__available = False

    def mark_available(self):
        self.__available = True

    def print_card(self):
        face_values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        print("face value: %s" % face_values[self.get_face_value()])
        if self.get_suit() == Suit.Club:
            print("suit: c")
        elif self.get_suit() == Suit.Heart:
            print("suit: h")
        if self.get_suit() == Suit.Diamond:
            print("suit: d")
        if self.get_suit() == Suit.Spade:
            print("suit: s")
        print()


class Hand:
    """
    Hand
    """
    def __init__(self):
        self._cards = []

    def get_score(self):
        """
        Get score to calculate win or lose

        :return:
        """
        score = 0
        for card in self._cards:
            score += card.get_face_value()
        return score

    def add_card(self, card):
        self._cards.append(card)

    def print_hand_cards(self):
        for card in self._cards:
            card.print_card()


class Deck:
    """
    Deck
    """
    def __init__(self):
        self.__cards = []
        self.__deal_index = 0  # marks first undealt card

    def set_deck_of_cards(self, deck_of_cards):
        self.__cards = deck_of_cards

    def shuffle_cards(self):
        cards_size = len(self.__cards)
        for i in range(cards_size):
            j = random.randint(i, cards_size - i - 1)
            card_1 = self.__cards[i]
            card_2 = self.__cards[j]
            self.__cards[j] = card_1
            self.__cards[i] = card_2

    def remaining_cards(self):
        return len(self.__cards) - self.__deal_index

    def deal_hand(self, number):
        if self.remaining_cards() < number:
            return None
        else:
            hand = [Card(random.randint(1,  14), Suit.get_suit()) for _ in range(number)]
            count = 0
            while count < number:
                card = self.deal_card()
                if card is not None:
                    hand[count] = card
                    count += 1
            return hand

    def deal_card(self):
        if self.remaining_cards() == 0:
            return None
        else:
            card = self.__cards[self.__deal_index]
            card.mark_unavailable()
            self.__deal_index += 1
            return card

    def print_cards(self):
        for card in self.__cards:
            card.print_card()


class BlackJackCard(Card):
    """
    Black Jack Card
    """
    def __init__(self, c, s):
        super(BlackJackCard, self).__init__(c, s)

    def get_value(self):
        if self.is_ace():
            return 1
        elif self.is_face_card():
            return 10
        else:
            return self.get_face_value()

    def get_min_value(self):
        if self.is_ace():
            return 1
        else:
            return self.get_value()

    def get_max_value(self):
        if self.is_ace():
            return 11
        else:
            return self.get_value()

    def is_ace(self):
        return self.get_face_value() == 1

    def is_face_card(self):
        return 10 < self.get_face_value() < 14


class BlackJackHand(Hand):
    """
    Black Jack Hand
    """
    def __init__(self):
        pass

    def get_score(self):
        scores = self.possible_scores()
        max_under = -sys.maxsize - 1
        min_over = sys.maxsize
        for score in scores:
            if 21 < score < min_over:
                min_over = score
            elif max_under < score <= 21:
                max_under = score

        return min_over if (max_under == -sys.maxsize - 1) else max_under

    def possible_scores(self):
        scores = []
        if len(self._cards) == 0:
            return scores
        for card in self._cards:
            self.add_card_to_score_list(card, scores)
        return scores

    def add_card_to_score_list(self, card, scores):
        if len(scores) == 0:
            scores.append(0)

        length = len(scores)
        for i in range(length):
            score = scores[i]
            scores[i] = score + card.get_min_value()
            if card.get_min_value() != card.get_max_value():
                scores.append(score + card.get_max_value())

    def is_busted(self):
        return self.get_score() > 21

    def is_21(self):
        return self.get_score() == 21

    def is_black_jack(self):
        if len(self._cards) != 2:
            return False
        first = self._cards[0]
        second = self._cards[1]
        return (first.is_ace() and second.is_face_card()) or (second.is_ace() and first.is_face_card())


class BlackJackGameAutomator:
    """
    Black Jack Game Automator
    """
    hit_until = 16

    def __init__(self, num_players):
        self.__hands = [BlackJackHand() for _ in num_players]
        self.__deck = Deck()

    def deal_initial(self):
        for hand in self.__hands:
            card1 = self.__deck.deal_card()
            card2 = self.__deck.deal_card()
            if card1 is None and card2 is None:
                return False
            hand.add_card(card1)
            hand.add_card(card2)
        return True

    def get_black_jacks(self):
        winners = []
        for i in range(len(self.__hands)):
            if self.__hands[i].is_black_jack():
                winners.append(i)
        return winners

    def play_hand_with_index(self, i):
        hand = self.__hands[i]
        return self.play_hand(hand)

    def play_hand(self, hand):
        while hand.get_score() < self.hit_until:
            card = self.__deck.deal_card()
            if card is None:
                return False
            hand.add_card(card)
        return True

    def play_all_hands(self):
        for hand in self.__hands:
            if not self.play_hand(hand):
                return False
        return True

    def get_winners(self):
        winners = []
        winning_score = 0
        for i, hand in enumerate(self.__hands):
            if not hand.is_busted():
                if hand.get_score() > winning_score:
                    winning_score = hand.get_score()
                    winners.clear()
                    winners.append(i)
                elif hand.get_score() == winning_score:
                    winners.append(i)
        return winners

    def initialize_deck(self):
        cards = []
        for i in range(1, 14):
            for j in range(0, 4):
                suit = Suit.get_suit_from_value(j)
                card = BlackJackCard(i, suit)
                cards.append(card)

        self.__deck = Deck()
        self.__deck.set_deck_of_cards(cards)
        self.__deck.shuffle_cards()

    def print_hands_and_score(self):
        for i, hand in enumerate(self.__hands):
            print("Hand %d (%d): " % (i, hand.get_score()))
            hand.print_hand_cards()


class CardSystem:
    """
    Card System
    """
    def __init__(self):
        num_hands = 5
        automator = BlackJackGameAutomator(num_hands)
        automator.initialize_deck()
        success = automator.deal_initial()
        if not success:
            print("Error. Out of cards.")
        else:
            print("--- Initial ---")
            automator.print_hands_and_score()
            black_jacks = automator.get_black_jacks()
            if len(black_jacks) > 0:
                print("Blackjack at ")
                for i in black_jacks:
                    print("%d, " % i)
                print()
            else:
                success = automator.play_all_hands()
                if not success:
                    print("Error. Out of cards.")
                else:
                    print("--- Completed Game ---")
                    automator.print_hands_and_score()
                    winners = automator.get_winners()
                    if len(winners) > 0:
                        print("Winners: ")
                        for i in winners:
                            print("%d, " % i)
                        print()
                    else:
                        print("Draw. All players have busted.")
