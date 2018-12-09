---
title: Making branch
date: 2018-12-09
tags:
  - git
  - branch
---

One of useful tip I got from Google Code-in was making branch. Mentors told me to
make a branch in your forked repository and send PR from that branch. Yeah, you can think this is
very basic job or what benefit does it have? Well, I could tell some reasons.

First, you can split your job with other jobs. If you just work on master, there is no way
to switch from job to job unless you use stash (but there is no way to commit!).
On the other hand, if you do you job in individual branch, you can switch the job with simple command:
`git checkout <branch-name>`.

Second, you can avoid effecting `master` branch. `master` branch is quite important because it's branch
for public use. Others can clone from your `master` branch. So if you manipulate history of `master` branch,
Ones who cloned your `master` branch will get conflict and they may have to go through a complex process to
apply their local changes. And this process is tough job for git beginners to do and it's also a annoying job
for people who are familiar with git. However, individual branch is private. There's no one (or few) who would fetch your
working branch. Therfore, you can do any job you wants to do. It's like a sandbox, safe place to work.

Making branch is not a rule, you can do you're job at `master` branch if you want so. You can feel nothing bad now but
if you starts to work as a team, this will be needed. Also, there are some benefits even you work as alone. So,
start making branches from now!
