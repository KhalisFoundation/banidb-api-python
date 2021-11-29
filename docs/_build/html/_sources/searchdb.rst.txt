Search
======

Search for any shabad in the BaniDB API

.. code:: python

    banidb.search(query, searchtype=1, source='all', larivaar=False,
               ang=None, raag=None, writer='all', page=1, results=None)

Parameters
~~~~~~~~~~

-  **query**: what you want to search.
-  `searchtype <searchtype.html>`__: how you want to search (first
   letter, word, ang, etc).
-  `source <sources.html>`__: from where you want to search (by default,
   Guru Granth Sahib Ji).
-  **larivaar**: you want it to be in larivaar or not.
-  **ang**: specify the ang to search from, for more precise results.
-  **raag**: specify the raag for your search.
-  `writer <writers.html>`__: specify the banikaar, writer of the
   specific bani.
-  **page**: specify page of search results.
-  **results**: specify number of results you want.

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

