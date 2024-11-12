import unittest

from tap_google_ads.transform import AddFieldsRecordTransformation, SyncContext


class TestAddFieldsRecordTransformation(unittest.TestCase):

    def setUp(self):
        self.context = SyncContext(
            customer={"customerId": 123, "customerName": "Pattern Co."},
            config={"start_date": "2024-11-10"},
        )
        self.record = {"field1": "value1"}

    def test_transform_with_callable_fields(self):
        transformation = AddFieldsRecordTransformation(
            fields={
                "callable": lambda context: context.customer["customerId"],
                "callable_config": lambda context: context.config["start_date"],
                "country": "US",
            },
        )
        transformed_record = transformation.transform(self.record, self.context)
        assert transformed_record == {
            "field1": "value1",
            "callable": 123,
            "callable_config": "2024-11-10",
            "country": "US",
        }

    def test_transform_skips_missing_keys(self):
        transformation = AddFieldsRecordTransformation(
            fields={
                "callable": lambda context: context.customer["nonExistentKey"],
            },
        )
        transformed_record = transformation.transform(self.record, self.context)
        assert transformed_record == {"field1": "value1"}


if __name__ == "__main__":
    unittest.main()
