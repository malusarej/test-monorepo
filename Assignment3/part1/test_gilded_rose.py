import unittest
from gilded_rose import GildedRose, Item

class TestGildedRose(unittest.TestCase):
    def test_normal_item_quality_degradation(self):
        # Arrange
        items = [Item("Normal Item", 10, 20)]
        gr = GildedRose(items)

        # Act
        gr.update_quality()

        # Assert
        self.assertEqual(items[0].quality, 19)

    def test_normal_item_sell_in_degradation(self):
        # Arrange
        items = [Item("Normal Item", 10, 20)]
        gr = GildedRose(items)

        # Act
        gr.update_quality()

        # Assert
        self.assertEqual(items[0].sell_in, 9)

    def test_normal_item_quality_never_negative(self):
        # Arrange
        items = [Item("Normal Item", 10, 0)]
        gr = GildedRose(items)

        # Act
        gr.update_quality()

        # Assert
        self.assertEqual(items[0].quality, 0)

    def test_aged_brie_quality_increases(self):
        # Arrange
        items = [Item("Aged Brie", 10, 20)]
        gr = GildedRose(items)

        # Act
        gr.update_quality()

        # Assert
        self.assertEqual(items[0].quality, 21)

    def test_sulfuras_quality_never_changes(self):
        # Arrange
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gr = GildedRose(items)

        # Act
        gr.update_quality()

        # Assert
        self.assertEqual(items[0].quality, 80)

    def test_backstage_passes_quality_increase(self):
        # Arrange
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gr = GildedRose(items)

        # Act
        gr.update_quality()

        # Assert
        self.assertEqual(items[0].quality, 21)

    def test_backstage_passes_quality_increase_more(self):
        # Arrange
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gr = GildedRose(items)

        # Act
        gr.update_quality()

        # Assert
        self.assertEqual(items[0].quality, 22)

    def test_backstage_passes_quality_increase_max(self):
        # Arrange
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)]
        gr = GildedRose(items)

        # Act
        gr.update_quality()

        # Assert
        self.assertEqual(items[0].quality, 50)

    def test_backstage_passes_quality_drop_after_concert(self):
        # Arrange
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gr = GildedRose(items)

        # Act
        gr.update_quality()

        # Assert
        self.assertEqual(items[0].quality, 0)

    def test_conjured_item_quality_degradation(self):
        # Arrange
        items = [Item("Conjured Mana Cake", 5, 20)]
        gr = GildedRose(items)

        # Act
        gr.update_quality()

        # Assert
        self.assertEqual(items[0].quality, 18)

if __name__ == '__main__':
    unittest.main()

