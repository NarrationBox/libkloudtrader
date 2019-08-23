'''Various methods to help you store, process, pipeline and manipulate your streams of data'''

from typing import Any
from collections.abc import Sequence
import numpy as np
from .exceptions import OverwriteError
import libkloudtrader.stocks as stocks
import pandas as pd


class Buffer(Sequence):
    '''A doubled sided/ended queue/buffer for internal data stream processing'''

    def __init__(self,
                 size: int,
                 dtype: Any = np.float32,
                 allow_overwrite: bool = True):
        '''Initilization'''
        self.arr = np.empty(size, dtype)
        self.left_index = 0
        self.right_index = 0
        self.size = size
        self.allow_overwrite = allow_overwrite

    def unwrap(self):
        '''copies the data from the buffer to an unwrapped form'''
        return np.concatenate(
            (self.arr[self.left_index:min(self.right_index, self.size)],
             self.arr[:max(self.right_index - self.size, 0)]))

    def fix_indices(self):
        """Enforce the invariant that 0 <= self.left_index < self.size"""
        if self.left_index >= self.size:
            self.left_index -= self.size
            self.right_index -= self.size
        elif self.left_index < 0:
            self.left_index += self.size
            self.right_index += self.size

    @property
    def check_if_full(self) -> bool:
        """Check if there is no more space in the buffer"""
        return len(self) == self.size

    def __array__(self):
        return self.unwrap()

    @property
    def dtype(self):
        return self.arr.dtype

    @property
    def shape(self):
        return (len(self), ) + self.arr.shape[1:]

    @property
    def maxlen(self):
        '''maxlen/size'''
        return self.size

    @property
    def buffer_size(self):
        '''size'''
        return self.size

    def __len__(self):
        return self.right_index - self.left_index

    def __getitem__(self, item):
        if not isinstance(item, tuple):
            item_arr = np.asarray(item)
            if issubclass(item_arr.dtype.type, np.integer):
                item_arr = (item_arr + self.left_index) % self.size
                return self.arr[item_arr]

        return self.unwrap()[item]

    def __iter__(self):
        return iter(self.unwrap())

    def __repr__(self):
        '''Stdouts the buffer and size'''
        return '<Buffer of {!r}>'.format(np.asarray(self))

    def append(self, value):
        '''Append element to the right like any other list/queue'''
        if self.check_if_full:
            if not self.allow_overwrite:
                raise OverwriteError(
                    'You are trying to append to a full Buffer with allow_overwrite=False'
                )
            elif not len(self):
                return
            else:
                self.left_index += 1

        self.arr[self.right_index % self.size] = value
        self.right_index += 1
        self.fix_indices()

    def append_left(self, value):
        '''append element to the left'''
        if self.check_if_full:
            if not self.allow_overwrite:
                raise OverwriteError(
                    'You are trying to append to a full Buffer with allow_overwrite=False'
                )
            elif not len(self):
                return
            else:
                self.right_index -= 1

        self.left_index -= 1
        self.fix_indices()
        self.arr[self.left_index] = value

    def pop(self):
        if len(self) == 0:
            raise IndexError()
        self.right_index -= 1
        self.fix_indices()
        res = self.arr[self.right_index % self.size]
        return res

    def popleft(self):
        if len(self) == 0:
            raise IndexError()
        res = self.arr[self.left_index]
        self.left_index += 1
        self.fix_indices()
        return res


from streamz import Stream
stream = Stream()
import libkloudtrader.crypto as crypto


def add_data_to_batch(batch_size, data):
    batch = Buffer(size=batch_size, dtype='f8')
    batch.append_left(data)
    #print(batch)

    if len(batch) == batch.maxlen:
        yield batch
        batch.pop()
    #source.buffer(upstream=data,n=20)
    '''while batch_size < batch.maxlen:
        batch.append(data)
        print(batch)
        if batch.maxlen == batch_size:
            return np.array(batch)'''
        #batch = Buffer(size=batch_size, dtype='f8')
