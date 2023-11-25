from heredity import *

def main_test():
    test_joint_probability()

def test_joint_probability():
    # test the sample shown in the spec
    people = load_data("data/family0.csv")

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

    names = set(people)

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

    normalize(probabilities)

    """
    Harry:
        Gene:
            2: 0.0092
            1: 0.4557
            0: 0.5351
        Trait:
            True: 0.2665
            False: 0.7335
    James:
        Gene:
            2: 0.1976
            1: 0.5106
            0: 0.2918
        Trait:
            True: 1.0000
            False: 0.0000
    Lily:
        Gene:
            2: 0.0036
            1: 0.0136
            0: 0.9827
        Trait:
            True: 0.0000
            False: 1.0000
    """
    assert round(probabilities["Harry"]["gene"][2], 4) == 0.0092
    assert round(probabilities["Harry"]["gene"][1], 4) == 0.4557
    assert round(probabilities["Harry"]["gene"][0], 4) == 0.5351
    assert round(probabilities["Harry"]["trait"][True], 4) == 0.2665
    assert round(probabilities["Harry"]["trait"][False], 4) == 0.7335

    assert round(probabilities["James"]["gene"][2], 4) == 0.1976
    assert round(probabilities["James"]["gene"][1], 4) == 0.5106
    assert round(probabilities["James"]["gene"][0], 4) == 0.2918
    assert round(probabilities["James"]["trait"][True], 4) == 1.0000
    assert round(probabilities["James"]["trait"][False], 4) == 0.0000

    assert round(probabilities["Lily"]["gene"][2], 4) == 0.0036
    assert round(probabilities["Lily"]["gene"][1], 4) == 0.0136
    assert round(probabilities["Lily"]["gene"][0], 4) == 0.9827
    assert round(probabilities["Lily"]["trait"][True], 4) == 0.0000
    assert round(probabilities["Lily"]["trait"][False], 4) == 1.0000

if __name__ == "__main__":
    main_test()