class Item:
    """ DO NOT CHANGE THIS CLASS!!! """
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class ItemUpdater:
    def __init__(self, item):
        self.item = item

    def update(self):
        pass


class NormalItemUpdater(ItemUpdater):
    def update(self):
        if self.item.quality > 0:
            self.item.quality -= 1
        self.item.sell_in -= 1
        if self.item.sell_in < 0:
            if self.item.quality > 0:
                self.item.quality -= 1


class AgedBrieItemUpdater(ItemUpdater):
    def update(self):
        if self.item.quality < 50:
            self.item.quality += 1
        self.item.sell_in -= 1


class SulfurasItemUpdater(ItemUpdater):
    def update(self):
        pass  # Sulfuras does not change


class BackstagePassItemUpdater(ItemUpdater):
    def update(self):
        if self.item.quality < 50:
            self.item.quality += 1
            if self.item.sell_in < 11 and self.item.quality < 50:
                self.item.quality += 1
            if self.item.sell_in < 6 and self.item.quality < 50:
                self.item.quality += 1
        self.item.sell_in -= 1
        if self.item.sell_in < 0:
            self.item.quality = 0


class ConjuredItemUpdater(ItemUpdater):
    def update(self):
        if self.item.quality > 1:
            self.item.quality -= 2
        else:
            self.item.quality = 0
        self.item.sell_in -= 1
        if self.item.sell_in < 0 and self.item.quality > 1:
            self.item.quality -= 2


class GildedRose:
    ITEM_UPDATERS = {
        "Aged Brie": AgedBrieItemUpdater,
        "Sulfuras, Hand of Ragnaros": SulfurasItemUpdater,
        "Backstage passes to a TAFKAL80ETC concert": BackstagePassItemUpdater,
        "Conjured Mana Cake": ConjuredItemUpdater,
    }

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            updater_class = self.ITEM_UPDATERS.get(item.name, NormalItemUpdater)
            updater = updater_class(item)
            updater.update()
