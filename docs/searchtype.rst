Search Types
------------

.. code:: python

    # Get searchtype indices to be used for custom search
    print(banidb.search_type())

| **All available Search Types**

===== ===========
Index Search Type
===== ===========
0     First letter each word from start (Gurmukhi)
1     First letter each word anywhere (Gurmukhi) **[Default]**
2     Full Word (Gurmukhi)
3     Full Word Translation (English)
4     Romanized Gurmukhi (English)
5     Ang
6     Main Letter (Gurmukhi)
7     Romanized first letter anywhere (English)
===== ===========

The above provided indices can be used in `Search <searchdb.html>`__ function
to narrow exploration.
