from hiregraph.nodes.scoring import aggregate_scores

def test_aggregate():
    result = aggregate_scores(
        {
            "scores": [5, 10]
        }
    )

    assert result["final_score"] == 7.5