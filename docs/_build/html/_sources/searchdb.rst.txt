Search
======

Search for any shabad in the BaniDB API

.. code:: python

    banidb.search(query, searchtype=1, source='all', larivaar=False,
               ang=None, raag=None, writer='all', page=1, results=None)

Return a dictionary of search results.

**Parameters:** 
    - **query** *(str or int)* – what you want to search.

    - `searchtype <searchtype.html>`__ *(int)* – how you want to search (first letter, word, ang, etc).

    - `source <sources.html>`__ *(str)* – from where you want to search (by default, Guru Granth Sahib Ji).

    - **larivaar** *(bool)* – you want it to be in larivaar or not.

    - **ang** *(int)* – specify the ang to search from, for more precise results.

    - **raag** *(int)* – specify the raag for your search.

    - `writer <writers.html>`__ *(int)* – specify the banikaar, writer of the specific bani.

    - **page** *(int)* – specify page of search results.

    - **results** *(int)* – specify number of results you want.

**Returns:**    Search Results as dictionary(key-value pair).

**Return type:**    dict

Example
^^^^^^^

.. code:: python

    # Searching Bandhana Har Bandhana Gun Gaavo Gopal Rai....
    shabad_data = banidb.search("bhbgggr")
    print(shabad_data)

**Output**

.. code:: 

    {
        'total_results': 1,
        'total_pages': 1,
        'pages_data': 
            {'page_1': 
              [{
                'shabad_id': 2610,
                'verse': 'ਬੰਦਨਾ ਹਰਿ ਬੰਦਨਾ ਗੁਣ ਗਾਵਹੁ ਗੋਪਾਲ ਰਾਇ ॥ ਰਹਾਉ ॥',
                'steek': {
                    'en': 'I bow in reverence to the Lord, I bow in reverence. I sing the Glorious Praises of the Lord, my King. ||Pause||',
                    'pu': 'ਹੇ ਭਾਈ! ਪਰਮਾਤਮਾ ਨੂੰ ਸਦਾ ਨਮਸਕਾਰ ਕਰਿਆ ਕਰੋ, ਪ੍ਰਭੂ ਪਾਤਿਸ਼ਾਹ ਦੇ ਗੁਣ ਗਾਂਦੇ ਰਹੋ ।ਰਹਾਉ।'
                }, 
                'source': {
                    'pu': 'ਸ੍ਰੀ ਗੁਰੂ ਗ੍ਰੰਥ ਸਾਹਿਬ ਜੀ',
                    'en': 'Sri Guru Granth Sahib Ji', 
                    'ang': 683, 'raagpu': 'ਰਾਗੁ ਧਨਾਸਰੀ', 
                    'raagen': 'Raag Dhanaasree', 
                    'writer': 'Guru Arjan Dev Ji'
                }
              }]
            }
    }

