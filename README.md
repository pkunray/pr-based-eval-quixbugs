# pr-based-eval-quixbugs
A pull-request–based evaluation dataset built from QuixBugs. Each bug is introduced through PRs without merging, enabling PR-centric evaluation and analysis.

## Differences from the original QuixBugs dataset

### Python-only subset, without comments

Only Python subset of QuixBugs is included, and all code comments are removed.

This follows the same setting as in [An Analysis of the Automatic Bug Fixing Performance of ChatGPT](https://arxiv.org/abs/2205.10583)
, since this study needs to compare against their results.

### Buggy programs only

This dataset only contains buggy implementations, the correct (fixed) versions of programs are not included.

## Repository structure

Each buggy program is introduced as a separate Pull Request (PR).

PRs are left unmerged, to preserve the PR-based workflow for evaluation.

## The study uses this dataset

See: https://github.com/pkunray/octopusai
