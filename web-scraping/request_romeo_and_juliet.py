import requests

try:
    res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
    # print(type(res)) # <class 'requests.models.Response'>
    res.raise_for_status() # Always call raise_for_status() after calling requests.get(). 
                           # This will raise an exception if there was an error downloading the file and will do nothing if the download succeeded
                           # It ensures that the download has actually worked before your program continues.
                           # ensure that a program halts if a bad download occurs
    romeo_and_juliet_file = open('romeo_and_juliet.txt', 'wb')
    for chunk in res.iter_content(100000): # iter_content() method returns “chunks” of the content on each iteration through the loop
                                           # Each chunk is of the bytes data type,
                                           # (100000) specifies how many bytes each chunk will contain.
                                           # it ensures that the requests module doesn’t eat up too much memory when downloading massive files
        romeo_and_juliet_file.write(chunk)
    romeo_and_juliet_file.close()
except Exception as exc:
    print('There was a problem: %s' % (exc))

# print(res.status_code) # 200
# print(requests.codes.ok) # 200

# print(len(res.text)) # 178978

# print(res.text[:250])
# The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare

# This eBook is for the use of anyone anywhere at no cost and with
# almost no restrictions whatsoever.  You may copy it, give it away or
# re-use it under the terms of the Projec



res_with_error = requests.get('https://inventwithpython.com/page_that_does_not_exist')
try:
    res_with_error.raise_for_status()
    # Traceback (most recent call last):
    #   File "/Users/minkyunglee/Desktop/code/python-tutorial/requests_module.py", line 20, in <module>
    #     res_with_error.raise_for_status()
    #   File "/Users/minkyunglee/Library/Caches/pypoetry/virtualenvs/python-tutorial-FI68zB4L-py3.9/lib/python3.9/site-packages/requests/models.py", line 1021, in raise_for_status
    #     raise HTTPError(http_error_msg, response=self)
    # requests.exceptions.HTTPError: 404 Client Error: Not Found for url: https://inventwithpython.com/page_that_does_not_exist
except Exception as exc:
    print('There was a problem: %s' % (exc)) # There was a problem: 404 Client Error: Not Found for url: https://inventwithpython.com/page_that_does_not_exist