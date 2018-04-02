#!/usr/bin/env python
"""
The server
"""

from http import HTTPStatus

from eve import Eve
from flask import jsonify, make_response

app = Eve()

@app.route('/_health', methods=['GET'])
def hello_world():
    return make_response(jsonify({'alive': 'true'}), HTTPStatus.OK)

def before_sms_insertion_callback(documents):
    """
    What we have to do before an sms resource insert is done
    """
    print("Doing some cool stuff before insertion")

def after_sms_insertion_callback(documents):
    """
    What we have to do after an sms resource insert is done
    """
    print("Doing some cool stuff after insertion")
 
def main():
    app.on_insert_sms += before_sms_insertion_callback
    app.on_inserted_sms += after_sms_insertion_callback
    app.run(port=8080)


if __name__ == '__main__':
    main()