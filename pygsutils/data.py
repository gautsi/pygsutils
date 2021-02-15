import pandas as pd


def fmt_field_names(df: pd.DataFrame) -> pd.DataFrame:
    def fmt_field_name(name: str) -> str:
        return name.replace("\n", "_").replace(" ", "_").lower()

    return df.rename(columns={f: fmt_field_name(f) for f in df.columns})

def nonnull_unq_str(l):
    return "|".join(set([str(i) for i in l if not l is None]))
