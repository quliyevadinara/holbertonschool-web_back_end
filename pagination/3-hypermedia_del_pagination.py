#!/usr/bin/env python3
"""
3-hypermedia_del_pagination.py
"""

import csv
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) \
            -> Dict:
        """Return a dictionary with pagination metadata resilient to
        deletions.
        """
        data = self.indexed_dataset()
        assert index is None or 0 <= index <= max(data.keys())

        if index is None:
            index = 0

        page_data = []
        data_count = 0
        next_index = index

        for i in range(index, max(data.keys()) + 1):
            if data_count == page_size:
                break
            if i in data:
                page_data.append(data[i])
                data_count += 1
            next_index += 1

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(page_data),
            "data": page_data,
        }
