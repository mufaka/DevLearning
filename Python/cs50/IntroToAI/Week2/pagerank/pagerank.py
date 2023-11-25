import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000
DEBUG = False 


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(link for link in pages[filename] if link in pages)

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    # The return value of the function should be a Python dictionary with one key for 
    # each page in the corpus. Each key should be mapped to a value representing the 
    # probability that a random surfer would choose that page next. The values in this 
    # returned probability distribution should sum to 1    
    model = {}

    # get the links for the given page
    if len(corpus[page]) > 0:
        # initialize with random page choice probability
        for page_choice in corpus.keys():
            model[page_choice] = round((1 - damping_factor) / len(corpus.keys()), 4)

        # get the probability of choosing each page
        damping_val = damping_factor / len(corpus[page])

        for linked_page in corpus[page]:
            model[linked_page] += damping_val
    else:
        # no links, each page is equally probable
        for page_choice in corpus.keys():
            model[page_choice] = 1 / len(corpus.keys())

    return model 


"""
One way to interpret this model is as a Markov Chain, where each page represents a state, and 
each page has a transition model that chooses among its links at random. At each time step, the 
state switches to one of the pages linked to by the current state.

By sampling states randomly from the Markov Chain, we can get an estimate for each page’s 
PageRank. We can start by choosing a page at random, then keep following links at random, 
keeping track of how many times we’ve visited each page. After we’ve gathered all of our samples 
(based on a number we choose in advance), the proportion of the time we were on each page might 
be an estimate for that page’s rank.

Not all pages may be linkable from one start path. Direct links are followed with a probability 
of the damping factor otherwise a random page will be chosen.
"""


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    if DEBUG:
        print("CORPUS:")
        print(corpus)

    # we need to dictionary to hold the values
    pagerank = {}

    # get initial page. NOTE: don't include in visits because spec says total of visits
    #                         should = n and we are looping a count of n below
    current_page = random.choice(list(corpus.keys()))

    # normalize n to 1, round to 4 decimal places
    normalized_increment = round(1 / n, 4)

    # loop through n times picking a linked paged at random
    # or a random page (based on damping_factor)
    for i in range(n): 
        transition = transition_model(corpus, current_page, damping_factor)

        # we can use random.choices here because we have a list of probabilites in the transition model
        current_page = random.choices(list(transition.keys()), weights = list(transition.values()), k = 1)[0]

        if current_page in pagerank.keys():
            pagerank[current_page] = round(
                pagerank[current_page] + normalized_increment, 4
            )
        else:
            pagerank[current_page] = normalized_increment

    if DEBUG:
        print(pagerank)

    return pagerank 


"""
With probability 1 - d, the surfer chose a page at random and ended up on page p.
With probability d, the surfer followed a link from a page i to page p.
"""


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pagerank = {}
    n = len(corpus.keys())
    convergence_threshold = 0.0001

    # set an initial value for pagerank; all are equally probable at this point
    for key in corpus.keys():
        pagerank[key] = round(1 / n, 4)

    # initialize convergence sum for while loop
    convergence_sum = convergence_threshold + 1

    while convergence_sum > convergence_threshold:
        convergence_sum = 0
        for page in corpus.keys():
            # get pages linking to the current page (get keys where key isn't current page and current page is in set of values)
            linking_pages = [
                other_page 
                for other_page in corpus.keys() 
                if other_page != page and page in corpus[other_page]
            ]

            # sum up PR(i) / NumLinks(i) where i is inclusive of all linking pages
            link_sum = 0
            for linking_page in linking_pages:
                link_sum += pagerank[linking_page] / len(corpus[linking_page])

            # capture old pagerank for use in calculating delta for convergence
            old_pagerank = pagerank[page]

            # apply page rank formula
            new_pagerank = ((1 - damping_factor) / n) + damping_factor * link_sum 
            pagerank[page] = round(new_pagerank, 4)

            convergence_sum = convergence_sum + round(
                abs(old_pagerank - new_pagerank), 4
            )

    return pagerank 


if __name__ == "__main__":
    main()
