---
layout: default
title: CS 2316 - Final Project
---

# Final Project

In lieu of a written final exam you may do a final project demonstrating a range of course topics. You may work alone or in groups of up to five students -- the larger the group the greater the expectation.

## Requirements

Your project must employ most of the following features:

- Data aquisition, either through a (set of) large data file(s) in CSV, XML, or JSON format, or from a network source using web scraping or web services.
- Transformation of the data or synthesis of information from the data, such as summarizing or correlating data.
- Display of information through a web or GUI interface.

## Timeline

- **Proposal**: no later than two weeks before the final exam by email to me. Your brief proposal should describe:

    - the application you want to write,
    - the data you will use,
    - how you will acquire your data,
    - the format of the data you will consume,
    - what sort of transformation or use of the data you will implement, and
    - the kind of user interface your application will employ.

- **Demonstration**: sign up on T-Square for a demo time slot during the last week of class and finals week.
- **Final Deliverable**: submit your program code and data files (if applicable) on T-square by midnight on the day of the class's scheduled final exam.

## Project Ideas

If you're having trouble coming up with project ideas you may use these directly or as inspiration for your own ideas.

### Verb Usage Analysis

Verbs play a central role in any language, so mastering a language requires mastering its verbs. In addition to conjugations and imperative forms, French has 14 tenses to convey time and mood, making mastery of French verbs a daunting task. Often a learner wants to know which verbs to learn first. The central idea of this project is to develop a quantitative answer to that question by analyzing French texts and counting the occurences of French verbs so that French verbs can be ranked in order of frequecy of use.

There is a free XML data file containing over 25,000 French verbs called [LVF+1](http://rali.iro.umontreal.ca/rali/?q=en/node/1238) (Les verves français) and various databases of French texts. A challenge of this project will be recognizing conjugations and tenses of verbs in texts.

### French Language Trainer

The [Écho](http://www.nathan.fr/webapps/cpg2-0/default.asp?idcpg=1000) series of books is designed for French as a foreign language training programs and is used by Alliance Française in the U.S. The A1 level book comes with a DVD that contains MP3 files for all the audio exercises in the book, and a [French-English vocabulary](http://www.nathan.fr/upload/doccpg/038563_lexique-franco-anglais.pdf) is available online.

There are many opportunities for exploiting these data to aid in learning French. One idea is to create a training program that plays an audio file and quizses the user on comprehension and vocabulary. Such a program would need data structures mapping audio files to quiz questions and to vocbulary.

### Google Music Utilities

[Google Music API](https://github.com/simon-weber/gmusicapi)

### Social Media Sentiment Analysis

[Twitter APIs](https://dev.twitter.com/overview/documentation)
