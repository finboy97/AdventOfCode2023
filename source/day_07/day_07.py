from collections import Counter, defaultdict

test_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".splitlines()

test_input = open("/Users/finbar/PycharmProjects/AdventOfCode2023/source/day_07/input").read().splitlines()
test_input = [element.split() for element in test_input]

cards = "AKQT98765432J"
card_strength = defaultdict()
for i, element in enumerate(cards):
    card_strength[element] = i

hands = "five four full_house three two_pair pair high_card"
hands_list = defaultdict()
for hand in hands.split():
    hands_list[hand] = []


class CardHandAndBid:
    card = ""
    bid = 0
    next_card = None

    def __init__(self, x):
        self.card = x[0]
        self.bid = int(x[1])

    def get_next_card(self):
        return self.next_card

    def set_next_card(self, new_next):
        self.next_card = new_next


class OrderedHands():
    """Order a list of CardHandAndBid from weakest to strongest"""
    head = None
    length = 0

    def __init__(self):
        self.head = None
        length = 0
    def insert_hand(self, x):
        self.length += 1
        current = self.head
        added = False
        next_card = None
        while not added:
            # List is empty - insert at head
            if current is None:
                self.head = x
                added = True
                break
            elif self.is_hand_stronger_than_hand(x, self.head):
                x.set_next_card(self.head)
                self.head = x
                break
            else:
                next_card = current.get_next_card()
                if next_card is None:
                    current.set_next_card(x)
                    break
                elif self.is_hand_stronger_than_hand(x, next_card):
                    x.set_next_card(next_card)
                    current.set_next_card(x)
                    break
                else:
                    current = next_card

    def is_hand_stronger_than_hand(self, hand_1, hand_2):
        """Return True if hand 2 is stronger than 1"""
        for element_1, element_2 in zip(hand_1.card, hand_2.card):
            if card_strength[element_1] > card_strength[element_2]:
                return True
            elif card_strength[element_1] < card_strength[element_2]:
                return False
        return False


    def get_total_score(self, start_rank: int):
        total = 0
        rank = start_rank
        current = self.head
        while current is not None:
            total += (rank * current.bid)
            print(rank, current.bid, current.card)
            current = current.get_next_card()
            rank += 1

        return total, rank


for element in test_input:
    c = Counter(element[0])
    counts = c.most_common(3)
    print(counts)
    if len(counts) == 1:
        hands_list["five"].append(element)
    elif len(counts) == 2:
        if counts[1][0] == "J" or counts[0][0] == "J":
            hands_list["five"].append(element)
        elif counts[0][1] == 4:
            hands_list["four"].append(element)
        else:
            hands_list["full_house"].append(element)
    else:
        if ('J', 2) in counts or ('J', 3) in counts:
            hands_list["four"].append(element)
        else:
            if counts[0][1] == 3:
                hands_list["three"].append(element)
            elif counts[0][1] == 2:
                hands_list["two_pair"].append(element) if counts[1][1] == 2 else hands_list["pair"].append(element)
            else:
                hands_list["high_card"].append(element)

ordered_hands = defaultdict()
for key in hands_list.keys():
    ordered_hands[key] = OrderedHands()

for key in hands_list.keys():
    for element in hands_list[key]:
        ordered_hands[key].insert_hand(CardHandAndBid(element))

rank = 1
total_winnings = 0
for key in hands.split()[::-1]:
    print(key)
    money, last_rank = ordered_hands[f"{key}"].get_total_score(rank)
    rank = last_rank
    total_winnings += money
    print("\n")
print(total_winnings)
# 6440

# Part 2
# 253363044 too high