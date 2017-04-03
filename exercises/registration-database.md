---
layout: exercise
title: Registration Database Exercise
---

# Registration Database

## Introduction

In this exercise you will practice

- basic relational data modeling,
- writing SQL create table statements,
- writing SQL schema and data insertion scripts, and
- writing basic SQL queries.

## Problem Description

You work for the registrar of a major university and have been tasked with creating a database to hold courses and semester schedules.

## Solution Description

### Part 1

Write a SQL script named `registration.sql` that creates a database with the following tables:

- `dept` - with `dept_id`, `name`, and `dean`
- `course` - with `course_id`, `number` (like `CS 2316`), `name`, and `dept_id`, where `dept_id` is a foreign key to the `dept` table.

Choose appropriate primary keys for your tables.

Write a SQL script that populates the `dept` and `course` tables with sample data of your choosing.

### Part 2

Write a sql script with queries that answer the following questions:

- What are all the departments?
- What are the names of all the department deans?
- What are all the courses?
- What are all the first-year courses?
- What are all the CS courses?
- What are all the IE courses?
- What are all the CS and IE courses?
