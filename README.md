# ARAMIS documentation tutorial

Last update: July 2025.

The current version of the tutorial is available [here](https://www.aramislab.fr/tuto-doc/tutorial/index.html).

## How to maintain this repository?

There are three branches:
- `code` that contains the Python code of the toy library `neuroplot`, that we
use here for the tutorial. There is nothing related to documentation here.
- `doc` that contains the checkpoints of the tutorial.
- `main` that contains the final result of the tutorial, as well as the tutorial itself (in `docs/tutorial`).

Three key points:
- `main` contains `doc` that contains `code`. **Never merge `main` in `doc`, and `doc` in `code`**.
- As `doc` contains the checkpoints in a sequential way, **commit history is essential in `doc`**. When you make changes to this branch, take care to preserve the story as much as possible.
- In the tutorial, we refer to checkpoints via commit hashes of the `doc` branch. So, if you change the history of `doc`, you must update the hashes in the tutorial.

### If you want add a new step to the tutorial

1. Do the step on `doc`, to add a new checkpoint corresponding to this step.
2. Merge `doc` in `main`. It will update the finale result of the tutorial, that now
takes into account the new step.
3. Update `docs/tutorial` on `main` to add a page describing the new step.
4. Push `doc` and `main`. Here you don't change the history, so a simple `git pull` + `git push` is enough.

### If you want to make a modification to the Python code

1. Make your changes on `code`, then rebase `doc` on `code`. The history of code will then be rewritten, taking into account the modifications made on the initial code.
2. Then, merge `doc` in `main` is enough.
3. Update the commit hashes in the tutorial (`docs/tutorial` on `main`). This is necessary, because
history of `doc` was overwritten.
4. Use `git push --force` to also rewrite the history of `origin/doc`.
5. Push `main` and `code` (here a simple `git pull` + `git push` is enough).

### If you want to modify a checkpoint

Try not to, but if you really need to modify old checkpoints in `doc`.

1. Start an interactive rebase with `git rebase -i <commit-hash>`.
2. In the editor, change "pick" to "edit" for the commit you can't to modify.
3. Make your modifications, and commit.
4. `git rebase --continue` to continue the rebase (if there are conflicts with the following
commits).
5. Once the rebase is done, `git push --force` the `doc` branch.
6. Merge `doc` in `main`, and `push` `main`.

### To check that `doc` and `main` did not diverge

Main should contain the result of the tutorial. And `doc` contains the last checkpoint of the tutorial.
So `doc` and `main` should be very close. The only differences should be in `docs/tutorial` and `docs/index.rst`.

To make sure that they have not diverged, use: `git diff --name-only main doc 