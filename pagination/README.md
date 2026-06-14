# Pagination

## Description

This project covers different ways to paginate a dataset, including simple pagination, hypermedia pagination, and deletion-resilient hypermedia pagination.

## Resources

- [REST API Design: Pagination](https://www.intercom.com/blog/pagination-rest-api/)
- [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS)

## Learning Objectives

At the end of this project, you should be able to explain:

- How to paginate a dataset with simple page and page_size parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate a dataset in a way that is resilient to deletions

## Requirements

- All files interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All files end with a new line
- The first line of all files is exactly `#!/usr/bin/env python3`
- A `README.md` file at the root of the project folder is mandatory
- Code uses the `pycodestyle` style (version 2.5)
- All files must be executable
- All modules, classes, and functions should have documentation

## Files

### 0-simple_helper_function.py

Contains the `index_range` function that takes `page` and `page_size` arguments and returns a tuple of start and end indexes for pagination.

### 1-simple_pagination.py

Contains the `Server` class with a `get_page` method that returns the appropriate page of the dataset based on `page` and `page_size` parameters.

### 2-hypermedia_pagination.py

Contains the `Server` class with a `get_hyper` method that returns a dictionary with pagination metadata (`page_size`, `page`, `data`, `next_page`, `prev_page`, `total_pages`).

### 3-hypermedia_del_pagination.py

Contains the `Server` class with a `get_hyper_index` method that returns pagination data resilient to deletions, using an indexed dataset.

## Data

This project uses the `Popular_Baby_Names.csv` dataset (NYC popular baby names). The file must be
