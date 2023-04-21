import tkinter as tk
import random

class Game21:
    def __init__(self, master):
        self.master = master
        master.title("Игра 21")

        self.cards = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 10,
            "Q": 10,
            "K": 10,
            "A": 11
        }

        self.deck = list(self.cards.keys()) * 4
        self.hand = []
        self.points = 0

        self.label = tk.Label(master, text="Начните игру!")
        self.label.pack()

        self.deal_button = tk.Button(master, text="Раздать карту", command=self.deal_card)
        self.deal_button.pack()

        self.stand_button = tk.Button(master, text="Хватит", command=self.stand)
        self.stand_button.pack()

    def deal_card(self):
        """Выдает игроку новую карту"""
        card = random.choice(self.deck)
        self.hand.append(card)
        self.deck.remove(card)
        self.points += self.cards[card]

        if self.points > 21:
            self.label.config(text=f"Вы проиграли! Ваш счет: {self.points}")
            self.deal_button.config(state="disabled")
            self.stand_button.config(state="disabled")
        elif len(self.hand) == 5:
            self.label.config(text=f"Пять карт! Вы выиграли! Ваш счет: {self.points}")
            self.deal_button.config(state="disabled")
            self.stand_button.config(state="disabled")
        else:
            self.label.config(text=f"Вы получили карту {card}. Ваш счет: {self.points}")

    def stand(self):
        """Завершает игру и сравнивает очки игрока и дилера"""
        dealer_points = random.randint(17, 21)

        if self.points > dealer_points or dealer_points > 21:
            self.label.config(text=f"Вы выиграли! Ваш счет: {self.points}, счет дилера: {dealer_points}")
        elif self.points < dealer_points:
            self.label.config(text=f"Вы проиграли! Ваш счет: {self.points}, счет дилера: {dealer_points}")
        else:
            self.label.config(text=f"Ничья! Ваш счет: {self.points}, счет дилера: {dealer_points}")

        self.deal_button.config(state="disabled")
        self.stand_button.config(state="disabled")

root = tk.Tk()
game = Game21(root)
root.mainloop()