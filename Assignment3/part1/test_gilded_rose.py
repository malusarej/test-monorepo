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

    def test_multiple_normal_items_quality_degradation(self):
        # Arrange
        items = [Item("Normal Item", 10, 20), Item("Normal Item", 5, 10)]
        gr = GildedRose(items)

        # Act
        gr.update_quality()

        # Assert
        self.assertEqual(items[0].quality, 19)
        self.assertEqual(items[1].quality, 9)

    def test_aged_brie_quality_increases_multiple_items(self):
        # Arrange
        items = [Item("Aged Brie", 10, 20), Item("Aged Brie", 5, 10)]
        gr = GildedRose(items)

        # Act
        gr.update_quality()

        # Assert
        self.assertEqual(items[0].quality, 21)
        self.assertEqual(items[1].quality, 11)

    def test_backstage_passes_quality_increase_multiple_items(self):
        # Arrange
        items = [
            Item("Backstage passes to a TAFKAL80ETC concert", 15, 20),
            Item("Backstage passes to a TAFKAL80ETC concert", 10, 30)
        ]
        gr = GildedRose(items)

        # Act
        gr.update_quality()

        # Assert
        self.assertEqual(items[0].quality, 21)
        self.assertEqual(items[1].quality, 32)

    def test_conjured_item_quality_degradation_multiple_items(self):
        # Arrange
        items = [Item("Conjured Mana Cake", 5, 20), Item("Conjured Mana Cake", 3, 15)]
        gr = GildedRose(items)

        # Act
        gr.update_quality()

        # Assert
        self.assertEqual(items[0].quality, 18)
        self.assertEqual(items[1].quality, 13)

    def test_items_change_over_multiple_days(self):
        # Arrange
        items = [Item("Normal Item", 10, 20), Item("Aged Brie", 5, 10), Item("Backstage passes to a TAFKAL80ETC concert", 15, 30)]
        gr = GildedRose(items)

        # Define expected sell-in and quality values for each day
        expected_sell_in = [
            [9, 4, 14],
            [8, 3, 13],
            [7, 2, 12]
            # Add more days as needed
        ]

        expected_quality = [
            [19, 11, 31],
            [18, 12, 32],
            [17, 13, 33]
            # Add more days as needed
        ]

        # Act and Assert
        for day in range(len(expected_sell_in)):
            gr.update_quality()
            for i in range(len(items)):
                self.assertEqual(items[i].sell_in, expected_sell_in[day][i], f"Day {day + 1}, Item {i + 1}")
                self.assertEqual(items[i].quality, expected_quality[day][i], f"Day {day + 1}, Item {i + 1}")


if __name__ == '__main__':
    unittest.main()

