import unittest

from pyhocon import ConfigFactory  # noqa: F401

from databuilder import Scoped
from databuilder.extractor.csv_extractor import CsvExtractor


class TestCsvExtractor(unittest.TestCase):

    def setUp(self):
        # type: () -> None
        config_dict = {
            'extractor.csv.{}'.format(CsvExtractor.FILE_LOCATION): 'example/sample_data/sample_table.csv',
            'extractor.csv.model_class': 'databuilder.models.table_metadata.TableMetadata',
        }
        self.conf = ConfigFactory.from_dict(config_dict)

    def test_extraction_with_model_class(self):
        # type: () -> None
        """
        Test Extraction using model class
        """
        extractor = CsvExtractor()
        extractor.init(Scoped.get_scoped_conf(conf=self.conf,
                                              scope=extractor.get_scope()))

        result = extractor.extract()
        self.assertEquals(result.name, 'test_table1')
        self.assertEquals(result.description, '1st test table')
        self.assertEquals(result.database, 'hive')
        self.assertEquals(result.cluster, 'gold')
        self.assertEquals(result.schema_name, 'test_schema')
