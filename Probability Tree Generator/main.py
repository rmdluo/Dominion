from ete3 import Tree
import compute
import display

# startDeck - Dictionary in which the keys are String card types and the values are Integer # of cards
# startTop - List of cards on the top of the deck, starting with the top card and working downward
def generateTree(numOfTurns,startDeck,startTop):  
  t = Tree()
  t.add_features(deck=startDeck,top=startTop,hand={},discard={},prob=1)

  # Loop through each turn
  for turnNum in range(0,numOfTurns):  
    leafList = t.get_leaves()
    # Loop through each leaf
    for leaf in leafList:
      updatedDiscard = leaf.discard.copy()

      # Discard old hand
      for cardType in leaf.hand:
        if cardType in leaf.discard:
          updatedDiscard[cardType] = leaf.discard[cardType] + leaf.hand[cardType]
        else:
          updatedDiscard[cardType] = leaf.hand[cardType]

      # "Shuffle" if necessary
      updatedDeck = leaf.deck.copy()
      updatedTop = leaf.top.copy()

      deckSize = compute.nCards(leaf.deck)
      if deckSize < 5:
        for cardType in updatedDiscard:
          updatedDeck[cardType] = updatedDeck[cardType] + updatedDiscard[cardType]
          updatedDiscard[cardType] = 0
        handList = compute.possDraws(updatedDeck,base=leaf.deck)
      else:
        handList = compute.possDraws(updatedDeck)

      # Loop through each possible hand
      for i in range(len(handList)):
        child = leaf.add_child(name="D"+leaf.name[1:]+"."+str(i))
        if deckSize < 5:
          uncertainCards = handList[i].copy()
          for cardType in leaf.deck:
            uncertainCards[cardType] = uncertainCards[cardType] - leaf.deck[cardType]
          prob = compute.probDraw(uncertainCards,updatedDeck)
        else:
          prob = compute.probDraw(handList[i],updatedDeck)
        
        # Note: we have to update the deck twice--once when shuffling, and once when drawing
        updatedDeck2 = updatedDeck.copy() 
        for cardType in handList[i]:
          updatedDeck2[cardType] = updatedDeck2[cardType] - handList[i][cardType]
        child.add_features(deck=updatedDeck2,top=updatedTop,hand=handList[i],discard=updatedDiscard,prob=prob)
  
  # Add deckStr, handStr, and discardStr feature to nodes
  for node in t.traverse():
    node.add_feature("deckStr",str(node.deck))
    node.add_feature("handStr",str(node.hand))
    node.add_feature("discardStr",str(node.discard))
  
  print(t.write(features=["name","deckStr","handStr","prob"]))
  display.showTree(t.write(features=["name","deckStr","handStr","discardStr","prob"]))

generateTree(4,{"copper":7,"estate":3},["copper","estate","estate","copper"])
