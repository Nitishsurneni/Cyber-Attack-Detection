import pandas as pd
from pipeline.prediction_pipeline import predict_attack

# Create a test input row — ensure the columns match your trained model
sample = pd.DataFrame([{
    'network_packet_size': 620,
    'login_attempts': 3,
    'session_duration': 230.5,
    'ip_reputation_score': 0.8,
    'failed_logins': 1,
    'unusual_time_access': 0,
    'protocol_type_TCP': 1,
    'encryption_used_AES': 1,
    'browser_type_Chrome': 1,
    # Add other one-hot encoded features used in training here...
}])

# Predict
prediction = predict_attack(sample)
print("Prediction (0=Normal, 1=Attack):", prediction[0])
