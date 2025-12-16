import csv
import os

from storage import (
    get_latest_return,
    baseline_volatility
)

ALERT_THRESHOLD = 4.0
ALERT_LOG_FILE = "alerts_log.csv"


def check_alert(asset: str):
    current_return = get_latest_return()

    # guards
    if current_return is None:
        return
    if baseline_volatility is None or baseline_volatility == 0:
        return

    # abnormality calc
    abnormality_score = abs(current_return) / baseline_volatility

    if current_return < 0:
        abnormality_score *= 1.2
        direction = "bearish"
    else:
        direction = "bullish"

    # alert trigger
    if abnormality_score >= ALERT_THRESHOLD:
        alert_dict = {
            "asset": asset,
            "current_move_pct": current_return,
            "baseline_move_pct": baseline_volatility,
            "abnormality_score": round(abnormality_score, 2),
            "direction": direction
        }

        log_alert(alert_dict)


def log_alert(alert_dict: dict):
    file_exists = os.path.isfile(ALERT_LOG_FILE)

    with open(ALERT_LOG_FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=alert_dict.keys())

        if not file_exists:
            writer.writeheader()

        writer.writerow(alert_dict)
