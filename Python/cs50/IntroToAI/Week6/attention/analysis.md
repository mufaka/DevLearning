# Analysis
I chose to analyze the sentence "He bought a [MASK] from the grocery store." to see if
the model could infer appropriate nouns for sentences that include an action (verb) and
a location (noun). Additionally, I wanted to see if the model could distinguish between 
a word that could be either a noun or adjective. 

```
He bought a sandwich from the grocery store.
He bought a bag from the grocery store.
He bought a pizza from the grocery store.
```

The model did a really good job of picking up on the fact that "grocery" is an adjective 
in this context and using that information to suggest an appropriate noun for what was bought
there.

"She bought a [MASK] from the music store." produces the following suggestions:

```
She bought a cd from the music store.
She bought a guitar from the music store.
She bought a ticket from the music store.
```

## Layer 2, Head 2

Attention is paid to the relationship between grocery and store so it appears
the model is able to infer that the noun grocery actually an adjective that is 
the type of the store.

This is also demonstrated in Layer 10, Head 9 but within a much more noisy graph.

Example Sentences:
- He bought a [MASK] from the grocery store.
- She bought a [MASK] from the music store.

## Layer 8, Head 10

This graph very clearly shows the relationship of "from" to "the grocery store". Additionally,
it very clearly shows the relationship of "a [MASK] from" to "bought". This demonstrates an
ability to choose an appropriate noun based on a verb and a noun location.

Example Sentences:
- He bought a sandwich from the grocery store.
- She picked an [MASK] from the tree.

