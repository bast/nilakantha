[![License](https://img.shields.io/badge/license-%20BSD--3-blue.svg)](../master/LICENSE)


# nilakantha

Primitive script that creates a git bisect exercise using the Nilakantha series
to compute pi in order to create a mistake which is difficult to track down
without `git bisect`.

Bogus comments are added to make error hard to track with `git blame` run on
latest commit.
