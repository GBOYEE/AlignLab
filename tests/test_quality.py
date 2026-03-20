from alignlab.quality import lexical_diversity, score_dataset

def test_lexical_diversity():
    assert lexical_diversity("hello world") == 1.0
    assert lexical_diversity("hello hello") == 0.5

def test_score_dataset():
    pairs = [{"prompt":"Q","chosen":"A","rejected":"B","domain":"edu"}]
    res = score_dataset(pairs)
    assert res["total_pairs"] == 1