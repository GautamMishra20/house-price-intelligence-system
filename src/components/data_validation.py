import pandas as pd
from pathlib import Path
from src.entity.config_entity import DataValidationConfig
from src.logger import logger


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        validation_status = True
        reasons = []

        df = pd.read_csv(self.config.data_path)
        actual_columns = list(df.columns)
        expected_columns = list(self.config.all_schema.COLUMNS.keys())

        # 1. Check all expected columns are present
        missing_columns = set(expected_columns) - set(actual_columns)
        if missing_columns:
            validation_status = False
            reasons.append(f"Missing columns: {missing_columns}")

        unexpected_columns = set(actual_columns) - set(expected_columns)
        if unexpected_columns:
            validation_status = False
            reasons.append(f"Unexpected columns found: {unexpected_columns}")

        # 2. Check dtypes match schema (only for columns that exist)
        for col in set(expected_columns) & set(actual_columns):
            expected_dtype = self.config.all_schema.COLUMNS[col]
            actual_dtype = str(df[col].dtype)
            if actual_dtype != expected_dtype:
                validation_status = False
                reasons.append(
                    f"Column '{col}' dtype mismatch: "
                    f"expected {expected_dtype}, got {actual_dtype}"
                )

        # 3. Check shape matches expectation
        expected_shape = self.config.all_schema.EXPECTED_SHAPE
        if df.shape[0] != expected_shape.rows or df.shape[1] != expected_shape.columns:
            validation_status = False
            reasons.append(
                f"Shape mismatch: expected {expected_shape.rows} rows x "
                f"{expected_shape.columns} cols, got {df.shape[0]} x {df.shape[1]}"
            )

        # 4. Check non-nullable columns have zero nulls
        non_nullable = self.config.all_schema.NON_NULLABLE_COLUMNS
        for col in non_nullable:
            if col in df.columns and df[col].isnull().sum() > 0:
                validation_status = False
                reasons.append(
                    f"Column '{col}' expected zero nulls but found "
                    f"{df[col].isnull().sum()}"
                )

        # Write status file
        with open(self.config.status_file, "w") as f:
            f.write(f"Validation status: {validation_status}\n")
            if reasons:
                f.write("Reasons:\n")
                for r in reasons:
                    f.write(f"  - {r}\n")

        if validation_status:
            logger.info("Data validation passed.")
        else:
            logger.warning(f"Data validation failed. Reasons: {reasons}")

        return validation_status