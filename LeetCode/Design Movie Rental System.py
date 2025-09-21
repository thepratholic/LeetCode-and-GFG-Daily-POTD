from collections import defaultdict
from sortedcontainers import SortedSet

class MovieRentingSystem:

    def __init__(self, n: int, entries: list[list[int]]):
        self.available = defaultdict(SortedSet) 
        self.movie_to_price = defaultdict(SortedSet) 
        self.rented = SortedSet() 

        for shop, movie, price in entries:
            self.available[movie].add((price, shop))
            self.movie_to_price[movie].add((shop, price))

    def search(self, movie: int) -> list[int]:
        res = []
        cnt = 0

        if movie in self.available:
            for price, shop in self.available[movie]:
                res.append(shop)
                cnt += 1
                if cnt == 5:
                    break

        return res

    def rent(self, shop: int, movie: int) -> None:
        it_index = self.movie_to_price[movie].bisect_left((shop, -1))
        if it_index < len(self.movie_to_price[movie]):
            shop_key, price = self.movie_to_price[movie][it_index]
            if shop_key == shop: 
                self.available[movie].discard((price, shop))
                self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        it_index = self.movie_to_price[movie].bisect_left((shop, -1))
        if it_index < len(self.movie_to_price[movie]):
            shop_key, price = self.movie_to_price[movie][it_index]
            if shop_key == shop:
                self.available[movie].add((price, shop))
                self.rented.discard((price, shop, movie))

    def report(self) -> list[list[int]]:
        res = []
        cnt = 0
        for price, shop, movie in self.rented:
            res.append([shop, movie])
            cnt += 1
            if cnt == 5:
                break
        return res
