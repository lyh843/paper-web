"""Recompute the reading's real-data illustration, NOT a LoCalPFN reproduction.

Input: iris.data, downloaded from the UCI URL below, beside this script.
Output: iris-example.json, with training-only standardization and exact distances.
No model weights, forward pass, fine-tuning, or test score are computed.
"""

import csv
import hashlib
import json
import math
from pathlib import Path
import random


ROOT = Path(__file__).resolve().parent
SOURCE = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"


def main():
    raw = (ROOT / "iris.data").read_bytes()
    rows = [row for row in csv.reader(raw.decode().splitlines()) if row]
    assert len(rows) == 150
    features = [[float(value) for value in row[:4]] for row in rows]
    train = [i for c in range(3) for i in range(c * 50, c * 50 + 40)]
    validation = [i for c in range(3) for i in range(c * 50 + 40, c * 50 + 45)]
    test = [i for c in range(3) for i in range(c * 50 + 45, c * 50 + 50)]
    assert not (set(train) & set(validation) or set(train) & set(test))
    means = [sum(features[i][j] for i in train) / len(train) for j in range(4)]
    stds = [
        math.sqrt(sum((features[i][j] - means[j]) ** 2 for i in train) / len(train))
        for j in range(4)
    ]

    def standardized(i):
        return [(features[i][j] - means[j]) / stds[j] for j in range(4)]

    def nearest(query, k):
        candidates = [
            {
                "row": i + 1,
                "features": features[i],
                "label": rows[i][4],
                "distance": math.dist(standardized(query), standardized(i)),
            }
            for i in train
            if i != query
        ]
        return sorted(candidates, key=lambda row: (row["distance"], row["row"]))[:k]

    query = 149
    anchor = nearest(query, 1)[0]["row"] - 1
    neighbors = nearest(anchor, 6)
    permutation = list(range(6))
    random.Random(20261018).shuffle(permutation)
    output = {
        "source": SOURCE,
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "split": "Each class: first 40 train, next 5 validation, last 5 test; NOT the paper's TabZilla fold",
        "row_numbering": "1-based, nonempty rows of the UCI iris.data file",
        "training_rows": [i + 1 for i in train],
        "validation_rows": [i + 1 for i in validation],
        "test_rows": [i + 1 for i in test],
        "means": means,
        "population_stds": stds,
        "query": {
            "row": query + 1,
            "features": features[query],
            "withheld_label": rows[query][4],
            "standardized_features": standardized(query),
        },
        "nearest_k4": nearest(query, 4),
        "training_anchor_row": anchor + 1,
        "training_anchor_selection": "Chosen for pedagogy; actual training randomly samples anchors",
        "anchor_neighbors6": neighbors,
        "shuffle_seed": 20261018,
        "training_context_rows": [neighbors[i]["row"] for i in permutation[:4]],
        "training_query_rows": [neighbors[i]["row"] for i in permutation[4:]],
        "model_forward_executed": False,
        "fine_tuning_executed": False,
    }
    assert [row["row"] for row in output["nearest_k4"]] == [139, 128, 71, 79]
    assert output["training_context_rows"] == [62, 127, 64, 128]
    assert output["training_query_rows"] == [79, 71]
    (ROOT / "iris-example.json").write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n")
    print("Verified Iris illustration: k4 neighbors, training-only normalization, and a shared-context split")


if __name__ == "__main__":
    main()
