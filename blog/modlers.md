In our blog

Features
========
Blog will have the following features

1. Post(table in database)
2. Categories (table in database)
3. Tag (table in database)
4. Author (table in database)

Let us make a relation between our tables
=========================================
1. Post can have categories, and a categories can have many post (Relation between Post and Categories table)

2. A tag can have many post and a post can have many tag(ManytoMany ralation)

3. author can have many post and a post can have a single author (OnetoMany relations)[ no post can write by more than authors]

Attributes for table
====================
Post
====
1. title
2. created_date
3. body
4. tags
5. categories
6. author

Categories
==========
1. cat_name
2. cat_description

Author
======
1. Author name
2. Author email
3. Author bio

Tag
===
1. tag_name