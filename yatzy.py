from operator import itemgetter

def chance(dice):
    """Score the given role in "Chance" Yatzy category

    >>> chance([5,5,5,5,5])
    25
    >>> chance([1,2,3,4,5])
    15
    """
    return sum(dice)

def small_straight(dice):
    """Score the given roll in the "small straight" yatzy category
    >>> small_straight([1,2,3,4,5])
    15
    >>> small_straight([1,2,3,5,5])
    0

    It also accepts sets, or unsorted lists
    >>> small_straight({1,2,3,4,5})
    15
    >>> small_straight([1,2,3,5,4])
    15
    """
    if sorted(dice) == [1,2,3,4,5]:
        return sum(dice)
    return 0

def four_of_a_kind(dice):
    """Score the given roll in the "Four of a kind" category
    >>> four_of_a_kind([1,6,6,6,6])
    24
    >>> four_of_a_kind([1,1,6,6,6])
    0
    """
    counts = dice_counts(dice)
    for i in [6,5,4,3,2,1]:
        if counts[i] >= 4:
            return 4*i
    return 0

def ones(dice):
    """Score the given roll in the "Ones" category

    >>> ones([1,1,3,4,5])
    2
    >>> ones([3,4,5,6])
    0
    """
    return dice_counts(dice)[1]

def dice_counts(dice):
    """Make a dictionary of how many of each value are in the dice

    
    """
    return {x:dice.count(x) for x in range(1,7)}

def scores_in_categories(dice, categories=(chance, small_straight, four_of_a_kind, ones)):
    """Score the dice in each category and return those with a non-zero score.

    Args:
        dice (list)
        categories (tuple, optional): Defaults to (chance, small_straight, four_of_a_kind, ones).
    >>> scores = scores_in_categories([1,1,2,2,2], 
    ... (ones, small_straight, four_of_a_kind, chance))
    >>> [(score, category.__name__) for (score, category) in scores]
    [(8, 'chance'), (2, 'ones'), (0, 'small_straight'), (0, 'four_of_a_kind')]
    """
    scores = [(category(dice), category) for category in categories]
    return sorted(scores, reverse=True, key=itemgetter(0))
