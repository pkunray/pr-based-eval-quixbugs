# pr-based-eval-quixbugs
A pull-request–based evaluation dataset built from QuixBugs. Each bug is introduced through PRs without merging, enabling PR-centric evaluation and analysis.

## Differences from the original QuixBugs dataset

### Python-only subset, without comments

Only Python subset of QuixBugs is included, and all code comments that can reveal the solution are removed.

### Buggy programs only

This dataset only contains buggy implementations, the correct (fixed) versions of programs are not included.

## Repository structure

Each buggy program is introduced as a separate Pull Request (PR).

PRs are left unmerged, to preserve the PR-based workflow for evaluation.

## The study uses this dataset

See: https://github.com/pkunray/octopusai
