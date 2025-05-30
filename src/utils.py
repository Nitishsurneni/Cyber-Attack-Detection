# src/utils.py
def load_data(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        print(f"Dataset loaded successfully with shape: {df.shape}")
        return df
    except Exception as e:
        from src.exception import CustomException
        import sys
        raise CustomException(e, sys)
