---
title: The Pyflakes Bug
date: 2018-12-09
tags:
  - pyflakes
  - debugging
---

If I got a question, "What was your best task during GCI?", I would answer, "Fixing the Pyflakes Bug".
It was my last task of 2017 GCI. The task is to fix a bug of `pyflakes` that doesn't raise error for using global of undefined name:
```python
def main():
    global x
    print(x)

main()
```
If we run this code, python will spit out error that says `x` is undefined. However, `pyflakes` doesn't complain about this at all.
So, my job was to detect this kind of error and report it to user. However, it was really tough job. I've never experience such kind of
program and the codebase was really huge. I guess I spent a lot of time for reading the code and understanding. After reading the code,
I started debug. Tracing the variables, fixing the code, testing, trying again if it fails, and so on. I was quite nervous because 
I finished that job at the end of the deadline of GCI. Actually, the problem in the 
[task](https://codein.withgoogle.com/archive/2017/organization/5710453493727232/task/5059448926109696/) and the problem in the
[issue](https://codein.withgoogle.com/archive/2017/organization/5710453493727232/task/5059448926109696/) was different. And the problem
in issue was even easier than that of the task.

Anyway, I got a lot of thing from this task (even though I chose wrong problem). I've experienced debugging this huge codebase (yeah, it was
*huge* at least for me). I've never knew notions like AST or something like that, but, from this task, I knew a lot of concepts, and became
more interested in such kind of program. This task is one of the reason why I'm working on interpreters now. The experience from this task
was literally *great*.
