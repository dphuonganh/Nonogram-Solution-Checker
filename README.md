# Nonogram Solution Checker


## Nonogram Solution Checker

A nonogram is a puzzle game in which you fill in pixels to complete a picture.

Along the edge of the puzzle grid, there are numbers which give you the clues about that column or row. These numbers show how many pixels on that particular line will be filled in.

Let’s solve this example!

```
    ║ 2 | 4 | 4 | 4 | 2 ║
====+===+===+===+===+===+
1 1 ║   |   |   |   |   ║
5 ║   |   |   |   |   ║
5 ║   |   |   |   |   ║
3 ║   |   |   |   |   ║
1 ║   |   |   |   |   ║
====+===+===+===+===+===+
```

We can also mark squares with an `**0**` which indicates that no pixels can be placed there. With the information we have now we can play several 0s in the first and last columns. We know there are no more than two pixels in each column. They are finished:

```
    ║ 2 | 4 | 4 | 4 | 2 ║
====+===+===+===+===+===+
1 1 ║ 0 |   |   |   | 0 ║
5 | 1 | 1 | 1 | 1 | 1 ║
5 ║ 1 | 1 | 1 | 1 | 1 ║
3 ║ 0 |   |   |   | 0 ║
1 ║ 0 |   |   |   | 0 ║
====+===+===+===+===+===+
```

Now with this information we can solve several more rows. The first row has two clues. This means that the pixels must be separated by at least one location. The only way they fit now is by placing a `**1**`, a `**0**`, and an `**1**`:

```
    ║ 2 | 4 | 4 | 4 | 2 ║
====+===+===+===+===+===+
1 1 ║ 0 | 1 | 0 | 1 | 0 ║
5 ║ 1 | 1 | 1 | 1 | 1 ║
5 ║ 1 | 1 | 1 | 1 | 1 ║
3 ║ 0 |   |   |   | 0 ║
1 ║ 0 |   |   |   | 0 ║
====+===+===+===+===+===+
```

The fourth row can also be solved because the clue says three pixels and there are only three spaces left:

```
    ║ 2 | 4 | 4 | 4 | 2 ║
====+===+===+===+===+===+
1 1 ║ 0 | 1 | 0 | 1 | 0 ║
5 ║ 1 | 1 | 1 | 1 | 1 ║
5 ║ 1 | 1 | 1 | 1 | 1 ║
3 ║ 0 | 1 | 1 | 1 | 0 ║
1 ║ 0 |   |   |   | 0 ║
====+===+===+===+===+===+
```

We are nearly complete! Only the middle column and bottom row remain unsolved. But it is quite easy to see that there is only one location a pixel can be placed. The middle column must be 4 pixels long, so . . . 

```
    ║ 2 | 4 | 4 | 4 | 2 ║
====+===+===+===+===+===+
1 1 ║ 0 | 1 | 0 | 1 | 0 ║
5 ║ 1 | 1 | 1 | 1 | 1 ║
5 ║ 1 | 1 | 1 | 1 | 1 ║
3 ║ 0 | 1 | 1 | 1 | 0 ║
1 ║ 0 | 0 | 1 | 0 | 0 ║
====+===+===+===+===+===+
```

The columns and the rows specification of the nonogram can be written with two tuples as follows:

```
>>> specifications = (
...     ((2,), (4,), (4,), (4,), (2,)),
...     ((1, 1), (5,), (5,), (3,), (1,))
... )
```

The solution to this nonogram can be written as follows:

```
>>> solution = (
...     (0, 1, 0, 1, 0),
...     (1, 1, 1, 1, 1),
...     (1, 1, 1, 1, 1),
...     (0, 1, 1, 1, 0),
...     (0, 0, 1, 0, 1)
... )
```

Write a function `**is_nonogram_resolved**` that takes two arguments `**specifications**` and `**solution**` which respectively corresponds to the specifications of a nonogram and a proposed solution, and returns `**True**` if the suggested solution successfully matches the nonogram's specifications, `**False**` otherwise.

For example:

```
>>> is_nonogram_resolved(specifications, solution)
True
```

Another example. Providing another nonogram:

```
   ║ 2 | 4 | 4 ║
===+===+===+===+
1 ║ 0 | 1 | 0 ║
3 ║ 1 | 1 | 1 ║
3 ║ 1 | 1 | 1 ║
2 ║ 0 | 1 | 1 ║
1 ║ 0 | 0 | 1 ║
===+===+===+===+
>>> specifications = (
...     ((2,), (4,), (4,)),
...     ((1,), (3,), (3,), (2,), (1,))
... )
>>> solution = (
...     (0, 1, 0),
...     (1, 1, 1),
...     (1, 1, 1),
...     (0, 1, 1),
...     (1, 1, 1)
... )
>>> is_nonogram_resolved(specifications, solution)
False
>>> solution = (
...     (0, 1, 0),
...     (1, 1, 1),
...     (1, 1, 1),
...     (0, 1, 1),
...     (0, 0, 1)
... )
>>> is_nonogram_resolved(specifications, solution)
True
```
