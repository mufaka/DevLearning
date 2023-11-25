from pagerank import *
    
def main():
    test_sample_pagerank()
    test_transition_model()

def test_sample_pagerank():
    # sum of ranks should be 1.0, just use corpus1 for test (no reason, just picking one)
    corpus = crawl('corpus1')
    pagerank = sample_pagerank(corpus, DAMPING, SAMPLES)
    sum_of_rank = 0

    for key in pagerank.keys():
        sum_of_rank += pagerank[key]

    assert round(sum_of_rank, 4) == 1.0

def test_transition_model():
    # define the example pages
    corpus = {}
    corpus["1.html"] = { "2.html", "3.html" }
    corpus["2.html"] = { "3.html" }
    corpus["3.html"] = { "2.html" }

    transition = transition_model(corpus, "1.html", 0.85)

    sum_of_rank = 0

    for key in transition.keys():
        sum_of_rank += transition[key]

    # print(transition)
    assert round(sum_of_rank, 4) == 1.0

if __name__ == "__main__":
    main()