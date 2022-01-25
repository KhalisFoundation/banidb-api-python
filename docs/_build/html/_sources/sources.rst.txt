Sources
-----------

Provides available sources in the BaniDB API from which Bani can be
`search <searchdb.html>`__\ ed.

.. code:: python

    # Get all sources with ids
    print(banidb.sources())

Returns sources with their corresponding ids and names.

**Returns:**    Sources as dictionary(key-value pair).

**Return type:**    dict

| **All available Sources**

========= ========================================== =======================
Source ID Source                                     Source Unicode
========= ========================================== =======================
A         Amrit Keertan                              ਅੰਮ੍ਰਿਤ ਕੀਰਤਨ
B         Bhai Gurdas Ji Vaaran                      ਭਾਈ ਗੁਰਦਾਸ ਜੀ ਵਾਰਾਂ
D         Dasam Bani                                 ਦਸਮ ਬਾਣੀ
G         Sri Guru Granth Sahib Ji **[Default]**     ਸ੍ਰੀ ਗੁਰੂ ਗ੍ਰੰਥ ਸਾਹਿਬ ਜੀ
N         Bhai Nand Lal Ji Vaaran                    ਭਾਈ ਨੰਦ ਲਾਲ ਜੀ ਵਾਰਾਂ
R         Codes of Conduct and Other Panthic Sources ਰਹਿਤਨਾਮੇ ਅਤੇ ਪੰਥਕ ਲਿਖ਼ਤਾਂ
S         Bhai Gurdas Singh Ji Vaaran                ਭਾਈ ਗੁਰਦਾਸ ਸਿੰਘ ਜੀ ਵਾਰਾਂ
========= ========================================== =======================

The above provided ids can be used in `Search <searchdb.html>`__ function to
narrow exploration.
