from src.ingestion.loadData import loadData
from src.processing.cleanData import cleanData
from src.processing.featureEndineering import createFeatures
from src.analysis.detectAnomalies import detectAnomalies
from src.config.sentting import DATA_PATH, OUTPUT_PATH


def main():
    path = DATA_PATH

    df =loadData(path)

    df = cleanData(df)

    df = createFeatures(df)

    suspicious  = detectAnomalies(df)

    print(suspicious[['Label']].head())

    suspicious.to_csv("data/processed/anomalies.csv", index=False)


if __name__ == "__main__":
     main()

