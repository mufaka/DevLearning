import csv
import itertools
import sys

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65, # 0.0065 
            False: 0.35 # 0.0035
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56, # 0.0168
            False: 0.44 # 0.0132
        },

        # Probability of trait given no gene
        0: {
            True: 0.01, # 0.0096
            False: 0.99 # 0.9504
        }
    }, # base trait dist with no evidence should be 0.0329, 0.9671

    # Mutation probability
    "mutation": 0.01
}

def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)

    # powerset gives all possible combinations but why do we need this?
    # can't we just construct a graph from the data and calculate probabilities
    # that way?
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.

    NOTE: family2.csv seems to have an error in that Rose has a mother named Ron and 
          a father named Hermione
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


# this method is called repeatedly with a different scenario for the family
def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """

    probability = 1

    """
    if the family consists of Harry, James, and Lily, then calling this function where one_gene = {"Harry"}, two_genes = {"James"}, 
    and trait = {"Harry", "James"} should calculate the probability that Lily has zero copies of the gene, Harry has one copy of 
    the gene, James has two copies of the gene, Harry exhibits the trait, James exhibits the trait, and Lily does not exhibit the trait.
    """
    for person in people:
        if people[person]["mother"] is not None: 
            probability *= get_parent_probability(
                person, people, one_gene, two_genes, have_trait
            )
        else:
            probability *= get_person_probability(
                person, one_gene, two_genes, have_trait
            )

    return probability


def get_person_probability(person, one_gene, two_genes, have_trait):
    probability = 1

    # use gene_count to index into PROBS for gene
    gene_count = 2 if person in two_genes else 1 if person in one_gene else 0

    # use True/False value from 'in have_trait' to index into PROBS for trait
    probability *= (
        PROBS["gene"][gene_count] * PROBS["trait"][gene_count][person in have_trait]
    )

    return probability 


def get_parent_probability(child, people, one_gene, two_genes, have_trait):
    # If a parent has two copies of the mutated gene, then they will pass the mutated gene on to the child; 
    # if a parent has no copies of the mutated gene, then they will not pass the mutated gene on to the child; 
    # and if a parent has one copy of the mutated gene, then the gene is passed on to the child with probability 0.5
    # After a gene is passed on, though, it has some probability of undergoing additional mutation: changing from a 
    # version of the gene that causes hearing impairment to a version that doesn’t, or vice versa.
    mother = people[child]["mother"]
    father = people[child]["father"]

    # these are inheritance probabilities with mutation probability
    probability = 1
    mother_gene_prob = (
        1.0 - PROBS["mutation"] 
        if mother in two_genes 
        else 0.5 
        if mother in one_gene 
        else PROBS["mutation"]
    )

    father_gene_prob = (
        1.0 - PROBS["mutation"] 
        if father in two_genes 
        else 0.5 
        if father in one_gene 
        else PROBS["mutation"]
    )
    gene_count = 2 if child in two_genes else 1 if child in one_gene else 0

    if gene_count == 2:
        probability *= mother_gene_prob * father_gene_prob
    elif gene_count == 1:
        # NOTE: style50 suggested this formatting:
        probability *= ((1 - father_gene_prob) * mother_gene_prob) + (
            (1 - mother_gene_prob) * father_gene_prob
        )
    else:
        probability *= (1 - father_gene_prob) * (1 - mother_gene_prob)

    return probability * PROBS["trait"][gene_count][child in have_trait]


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    for person in probabilities:
        gene_count = 2 if person in two_genes else 1 if person in one_gene else 0
        probabilities[person]["gene"][gene_count] += p
        probabilities[person]["trait"][person in have_trait] += p


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    for person in probabilities:
        sum = 0
        
        for probability in probabilities[person]["gene"].values():
            sum += probability

        for probability in probabilities[person]["gene"]:
            probabilities[person]["gene"][probability] = (
                probabilities[person]["gene"][probability] / sum
            )

        sum = 0

        for probability in probabilities[person]["trait"].values():
            sum += probability

        for probability in probabilities[person]["trait"]:
            probabilities[person]["trait"][probability] = (
                probabilities[person]["trait"][probability] / sum
            )


if __name__ == "__main__":
    main()
