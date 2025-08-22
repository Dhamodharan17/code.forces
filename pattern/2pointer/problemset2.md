The two-pointer technique is a powerful algorithm for solving problems that involve searching, counting, or manipulating data in a linear data structure, like an array or string. It typically uses two pointers, often called "left" and "right," to traverse the data structure and find a solution efficiently. The problems listed below, arranged by increasing difficulty, can be solved using this technique.

### Easy Problems (Div2. A/B)

* **A. Berland National Library** (Problem 721A): A simple problem where you can use two pointers to find the number of ways to read a book from a sorted list of books within a given time.
* **B. BerSU Ball** (Problem 489B): Given two arrays of boys' and girls' dance skills, find the maximum number of pairs you can form where the skill difference is at most one. You can sort both arrays and use two pointers to solve this greedily.
* **C. Books** (Problem 279C): This problem asks for the longest contiguous segment of books that can be read within a given total time. A sliding window with two pointers is a perfect fit here.
* **C. They Are Everywhere** (Problem 701C): Find the minimum length of a substring that contains all unique characters of a given string. A sliding window (two pointers) is the key to solving this.
* **A. Alice, Bob and Chocolate** (Problem 6C): Two people eat chocolate from opposite ends of a bar. You need to find how many pieces each person eats. This is a classic two-pointer problem with two pointers moving towards each other.

***

### Medium Problems (Div2. C/D)

* **C. Hard Process** (Problem 660C): Given a binary array and a number *k*, find the longest contiguous subarray that you can make with at most *k* flips from 0 to 1. A sliding window with two pointers is a common approach.
* **D. Vasya and String** (Problem 676C): Similar to the "Hard Process" problem, you are given a string and can change at most *k* characters. The goal is to find the longest substring that consists of only one character. You can apply the two-pointer sliding window technique.
* **C. An impassioned circulation of affection** (Problem 814C): Given a string and a number of "free" changes, you need to find the longest substring of any character `c` that can be made. You can iterate through all possible characters (`a` to `z`) and for each character, use a sliding window with two pointers to find the answer.
* **A. Two Lands** (Problem 1166C): Given an array of integers, you need to count pairs of indices $(i, j)$ such that $abs(a_i) - abs(a_j) \le min(abs(a_i), abs(a_j))$. Sorting the array and using two pointers helps to efficiently count the pairs.
* **C. Another Problem on Strings** (Problem 165C): Count the number of substrings with exactly *k* ones. You can use two pointers to maintain a window and use a counting approach to find the number of such substrings.

This video provides a discussion of solutions to a recent Codeforces Div. 3 round.

[Codeforces Round 1016 (Div 3) — Solution Discussion](https://www.youtube.com/watch?v=xYL433xDbSY)
http://googleusercontent.com/youtube_content/0
