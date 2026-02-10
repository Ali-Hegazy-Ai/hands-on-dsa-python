# Text Frequency Analyzer

Analyze word frequencies in text files using custom hash table and heap implementations.

## Goal

- Tokenize a text file into words.
- Count frequencies using `HashTableChaining`.
- Find top-k most frequent words using `MinHeap`.
- Compare results against `collections.Counter.most_common(k)`.

## Acceptance Criteria

- [ ] Output matches `Counter.most_common(k)` for all test inputs.
- [ ] Unit tests pass for tokenizer, frequency counter, and top-k extraction.
- [ ] Writeup (<200 words) on hash collision stats observed during analysis.

## Usage

```bash
python -m projects.text_frequency.main sample.txt --top 10
```
