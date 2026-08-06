# TfIdfVectorizer

```c
REG_OP(TfIdfVectorizer)
    .INPUT(input, TensorType({DT_INT32, DT_INT64, DT_STRING}))
    .OUTPUT(output, TensorType({DT_FLOAT}))
    .REQUIRED_ATTR(max_gram_length, Int)
    .REQUIRED_ATTR(max_skip_count, Int)
    .REQUIRED_ATTR(min_gram_length, Int)
    .REQUIRED_ATTR(mode, String)
    .REQUIRED_ATTR(ngram_counts, ListInt)
    .REQUIRED_ATTR(ngram_indexes, ListInt)
    .ATTR(pool_int64s, ListInt, {})
    .ATTR(pool_strings, ListString, {})
    .ATTR(weights, ListFloat, {})
    .OP_END_FACTORY_REG(TfIdfVectorizer)
```

## Brief

This transform extracts n-grams from the input sequence and save them as a
vector. 

## Inputs

- input: can be either a 1-D or 2-D tensor for n-gram extraction, It is ether string UTF-8 or int32/int64 .

## Outputs

- output: tensor(float)
For 1-D input, output is the n-gram representation of that input. For 2-D input, the output is also a 2-D tensor
whose i-th row is the n-gram representation of the i-th input row. More specifically, if input shape is [C], the corresponding
output shape would be [max(ngram_indexes) + 1]. If input shape is [N, C], this operator produces a [N, max(ngram_indexes) + 1]-tensor. 

## Attributes

- max_gram_length : int (required)
Maximum n-gram length. If this value is 3, 3-grams will be used to generate the output .
- max_skip_count : int (required)
Maximum number of items (integers/strings) to be skipped when constructing an n-gram from X.
If max_skip_count=1, min_gram_length=2, max_gram_length=3, this operator may generate 2-grams
with skip_count=0 and skip_count=1, and 3-grams with skip_count=0 and skip_count=1.
- min_gram_length : int (required)
Minimum n-gram length. If this value is 2 and max_gram_length is 3, output may contain counts of
2-grams and 3-grams.
- mode : string (required)
The weighting criteria. It can be one of "TF" (term frequency), "IDF" (inverse document frequency),
and "TFIDF" (the combination of TF and IDF).
- ngram_counts : list of ints (required)
The starting indexes of 1-grams, 2-grams, and so on in pool. It is useful when determining the boundary
between two consecutive collections of n-grams. For example, if ngram_counts is [0, 17, 36],
the first index (zero-based) of 1-gram/2-gram/3-gram in pool are 0/17/36. This format is essentially identical
to CSR (or CSC) sparse matrix format, and we choose to use this due to its popularity.
- ngram_indexes : list of ints (required)
list of int64s (type: AttributeProto::INTS). This list is parallel to the specified 'pool_*' attribute. The i-th element
in ngram_indexes indicate the coordinate of the i-th n-gram in the output tensor.
- pool_int64s : list of ints
List of int64 n-grams learned from the training set. Either this or pool_strings attributes must be present but not both.
It's an 1-D tensor starting with the collections of all 1-grams and ending with the collections of n-grams. The i-th element
in pool stores the n-gram that should be mapped to coordinate ngram_indexes[i] in the output vector.
- pool_strings : list of strings
List of strings n-grams learned from the training set. Either this or pool_int64s attributes must be present but not both.
It's an 1-D tensor starting with the collections of all 1-grams and ending with the collections of n-grams. The i-th element
in pool stores the n-gram that should be mapped to coordinate ngram_indexes[i] in the output vector.
- weights : list of floats
list of floats. This attribute stores the weight of each n-gram in pool. The i-th element in weights is the weight of
the i-th n-gram in pool. Its length equals to the size of ngram_indexes. By default, weights is an all-one tensor.This attribute
is used when mode is "IDF" or "TFIDF" to scale the associated word counts. 

## Attention Constraints

- input can be either a 1-D or 2-D tensor, shape is [C] or [N, C].
- max(ngram_indexes) + 1 == len(weights), len(y) == len(weights).
- ngram_counts and pool(pool_int64s or pool_strings) must match.
- either pool_strings or pool_int64s attributes must be present but not both.


---

[Back to Operator Specifications (Atlas 200&500 A2 Inference Product)](../README.md)
