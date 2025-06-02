import pickle
from xgboost import XGBClassifier

# Load your training data if available, or skip training if already done
model = XGBClassifier()
# model.fit(X_train, y_train)  # only if training needed

# Save the model again
with open("models/xgboost_model.pkl", "wb") as f:
    pickle.dump(model, f)
