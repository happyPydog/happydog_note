import pytest
from unittest import mock

from pyspark.sql import functions as F
from pyspark.sql import DataFrame, Column
from pyspark.testing.sqlutils import ReusedSQLTestCase

from python_note.unittest_note.pyspark_function import filter_fact_sold_output_data


class TestTableFilterFunction(ReusedSQLTestCase):
    def test_filter_fact_sold_output_data(self):
        dataframe = mock.MagicMock(spec=DataFrame)
        data_start_date = "2020-01-01"
        data_end_date = "2024-01-01"

        filter_fact_sold_output_data(
            dataframe, data_start_date=data_start_date, data_end_date=data_end_date
        )

        dataframe.filter.assert_called_once()
        dataframe.filter().select.assert_called_once_with(
            "Master_Account_Key", "Data_Month"
        )
        dataframe.filter().select().distinct.assert_called_once_with()
