import pytest

from pyspark.sql import SparkSession
from pyspark.testing.utils import assertDataFrameEqual

from python_note.unittest_note.pyspark_function import filter_fact_sold_output_data


@pytest.fixture
def spark():
    spark = SparkSession.builder.appName("Testing PySpark Example").getOrCreate()
    yield spark
    spark.stop()


def test_filter_fact_sold_output_dataspark_fixture(spark):
    data_start_date = "2020-01-01"
    data_end_date = "2024-01-01"
    sample_data = [
        {
            "Master_Account_Key": "test_mak_1",
            "Data_Month": "2020-01-01",
            "License_Additional_Type": "0#0#0",
            "Licensing_Status_ID": 1,
        },
        {
            "Master_Account_Key": "test_mak_2",
            "Data_Month": "2020-01-01",
            "License_Additional_Type": "1#0#0",
            "Licensing_Status_ID": 0,
        },
        {
            "Master_Account_Key": "test_mak_3",
            "Data_Month": "2023-12-31",
            "License_Additional_Type": "0#0#0",
            "Licensing_Status_ID": 1,
        },
    ]
    dataframe = spark.createDataFrame(sample_data)

    expected_data = [
        {"Master_Account_Key": "test_mak_1", "Data_Month": "2020-01-01"},
        {"Master_Account_Key": "test_mak_3", "Data_Month": "2023-12-31"},
    ]
    expected_dataframe = spark.createDataFrame(expected_data).select(
        "Master_Account_Key", "Data_Month"
    )

    result_dataframe = filter_fact_sold_output_data(
        dataframe, data_start_date=data_start_date, data_end_date=data_end_date
    )

    assertDataFrameEqual(result_dataframe, expected_dataframe)
