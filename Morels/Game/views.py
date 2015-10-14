from django.shortcuts import render
from .models import *
from random import choice
from Game.models import Card
from Game.models import Deck
import random

# def test(request):
#     card = Card.objects.get()
#     return render(request, 'game.html')

def make_starting_decks(request):
    hand = []
    deck = []
    decay = []
    night = []
    deck = Deck()
    deck.save()
    # newdeck = Deck.forestCard
    # times = [10, 5, 4, 8, 5, 4, 6, 4, 3, 11, 5, 3, 8, 5, 3]

    # Honey_Fungus = Card.objects.get(type='Honey Fungus')
    # Shiitake = Card.objects.get(type='Shiitake')
    # Porcini = Card.objects.get(type='Porcini')
    # Tree_Ear = Card.objects.get(type='Tree Ear')
    # Hen_of_the_woods = Card.objects.get(type='Hen of the woods')
    # Chanterelle = Card.objects.get(type='Chanterelle')
    # Lawyer_Wig = Card.objects.get(type="Lawyer's Wig")
    # Fairy_Ring = Card.objects.get(type='Fairy Ring')
    # Morel = Card.objects.get(type='Morel')
    # Pan = Card.objects.get(type='Pan')
    # Destroying_Angel = Card.objects.get(type='Destroying Angel')
    # Butter = Card.objects.get(type='Butter')
    # Moon = Card.objects.get(type='Moon')
    # Basket = Card.objects.get(type='Basket')
    # Cider = Card.objects.get(type='Cider')
    #
    # lis = [
    #     Honey_Fungus,
    #     Shiitake,
    #     Porcini,
    #     Tree_Ear,
    #     Hen_of_the_woods,
    #     Chanterelle,
    #     Lawyer_Wig,
    #     Fairy_Ring,
    #     Morel,
    #     Pan,
    #     Destroying_Angel,
    #     Butter,
    #     Moon,
    #     Basket,
    #     Cider,
    # ]
    #
    # i = 0
    # for x in lis:
    #     temp = [x] * times[i]
    #     i += 1
    #     for y in temp:
    #         d.deckCard.add(y)
    #         deck.append(y)
    #         d.save()

    # random.shuffle(deck)

    # newdeck = deck[76:]

    make_night(night)

    # make_hand(deck, hand)

    print(deck)

    # d.deckCard.add()
    # print(d)

    return render(request, 'game.html', {'hand': hand})

def make_hand(deck, hand):

    i = 0
    while i < 4:
        hand.append(deck[i +1])
        deck.remove(deck[i +1])
        i += 1

def make_night(night):

    night += Card.objects.filter(type__in=[
        'Honey Fungus',
        'Shiitake',
        'Porcini',
        'Tree Ear',
        'Hen of the woods',
        'Chanterelle',
        "Lawyer's Wig",
        'Fairy Ring',
        'Morel',])

    for i in night:
        i.cardValue *= 2

    print(night)