from collections import defaultdict
from typing import List
from sortedcontainers import SortedList


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_cuisine = defaultdict(str)
        self.food_to_rating = defaultdict(str)
        self.mpp = defaultdict(SortedList)

        for f, c, r in zip(foods, cuisines, ratings):
            self.food_to_cuisine[f] = c
            self.food_to_rating[f] = r
            self.mpp[c].add((-r, f))


    def changeRating(self, food: str, newRating: int) -> None:
        cuisine_of_food = self.food_to_cuisine[food]
        old_rating = self.food_to_rating[food]

        self.mpp[cuisine_of_food].remove((-old_rating, food))
        self.mpp[cuisine_of_food].add((-newRating, food))
        self.food_to_rating[food] = newRating
        

    def highestRated(self, cuisine: str) -> str:
        return self.mpp[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)