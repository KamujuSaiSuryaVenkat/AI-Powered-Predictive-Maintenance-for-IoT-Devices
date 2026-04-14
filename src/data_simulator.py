import pandas as pd
import time
import os
import joblib

def generate_sensor_data():
    col_names = ['id', 'cycle', 'setting1', 'setting2', 'setting3'] + [f's{i}' for i in range(1, 22)]
    
    # Base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # File paths
    data_path = os.path.join(BASE_DIR, "data", "train_FD001.txt")
    model_path = os.path.join(BASE_DIR, "models", "features.pkl")

    # Load data
    df = pd.read_csv(data_path, sep='\s+', header=None, names=col_names)
    
    # Load features
    features = joblib.load(model_path)

    # Filter engine 1
    engine_data = df[df['id'] == 1]

    # Generate streaming data
    for _, row in engine_data.iterrows():
        data_packet = row[features].to_dict()
        data_packet['cycle'] = int(row['cycle'])
        data_packet['id'] = int(row['id'])
        
        yield data_packet
        time.sleep(0.8)