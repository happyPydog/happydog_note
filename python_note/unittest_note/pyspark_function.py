from pyspark.sql import DataFrame
import pyspark.sql.functions as F


def filter_fact_sold_output_data(df: DataFrame, **kwargs) -> DataFrame:
    data_start_date = kwargs.get("data_start_date")
    data_end_date = kwargs.get("data_end_date")
    filter_df = (
        df.filter(
            (F.col("Data_Month") < F.to_date(F.lit(data_end_date)))
            & (F.col("Data_Month") >= F.to_date(F.lit(data_start_date)))
            & (F.col("License_Additional_Type") == "0#0#0")
            & (F.col("Licensing_Status_ID") == 1)
        )
        .select("Master_Account_Key", "Data_Month")
        .distinct()
    )
    return filter_df
