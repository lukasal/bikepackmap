import unittest
import folium
import pandas as pd
from app.map.map_grand_depart import map_grand_depart
from unittest.mock import MagicMock


class TestMapGranddepart(unittest.TestCase):
    def setUp(self):
        # Sample data for activities
        self.activities1 = pd.DataFrame(
            {
                "end_date": ["2023-10-03", "2023-10-02"],
                "start_date": ["2023-10-03", "2023-10-02"],
                "map_polyline": [
                    [(45.0, 7.0), (46.0, 8.0)],
                    [(47.0, 9.0), (48.0, 10.0)],
                ],
                "start_location": ["Location A", "Location B"],
                "start_latlng": [(45.0, 7.0), (47.0, 9.0)],
                "end_latlng": [(46.0, 8.0), (48.0, 10.0)],
            }
        )
        self.activities2 = pd.DataFrame(
            {
                "end_date": [None, None],
                "start_date": [None, None],
                "map_polyline": [
                    [(45.0, 7.0), (46.0, 8.0)],
                    [(47.0, 9.0), (48.0, 10.0)],
                ],
                "start_location": ["Location A", "Location B"],
                "start_latlng": [(45.0, 7.0), (47.0, 9.0)],
                "end_latlng": [(46.0, 8.0), (48.0, 10.0)],
            }
        )
        # Convert end_date to datetime
        self.activities1["end_date"] = pd.to_datetime(self.activities1["end_date"])
        self.activities1["start_date"] = pd.to_datetime(self.activities1["start_date"])

        self.settings = MagicMock()
        self.settings.get_interactive_setting.side_effect = lambda x: {
            "depart_icon": "flag",
            "depart_icon_shape": "circle",
            "depart_border_transparent": False,
            "depart_border_color": "blue",
            "depart_symbol_color": "white",
            "depart_background_transparent": False,
            "depart_background_color": "red",
            "depart_icon_size": 20,
            "depart_icon_inner_size": 10,
        }[x]

    @unittest.skip("test obsolet and outdated")
    def test_map_grand_depart(self):
        # Test without final_popup
        result = map_grand_depart(self.activities1, self.settings)
        # Check the properties of the marker
        marker = list(result._children.values())[0]
        self.assertIsInstance(marker, folium.map.Marker)
        self.assertEqual(marker.location, [47.0, 9.0])
        self.assertEqual(marker.icon.options["id"], "grand_depart")

        self.assertIsInstance(result, folium.FeatureGroup)
        self.assertEqual(result.tile_name, "Grand depart")

    def test_map_grand_depart_no_dates(self):
        # Test without final_popup
        result = map_grand_depart(self.activities2, self.settings)
        # Check the properties of the marker
        marker = list(result._children.values())[0]
        self.assertIsInstance(marker, folium.map.Marker)
        self.assertEqual(marker.location, [45.0, 7.0])
        self.assertEqual(marker.icon.options["id"], "grand_depart")

        self.assertIsInstance(result, folium.FeatureGroup)
        self.assertEqual(result.tile_name, "Grand depart")


if __name__ == "__main__":
    unittest.main()
