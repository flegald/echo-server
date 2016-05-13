# _*_ coding utf-8 _*_
"""Test to make sure the correct response is given."""


def test_ok():
    """Test to get correct server response."""
    from server import response_ok
    msg = response_ok()
    msg = msg.split()
    HTTP = msg[0]
    status_code = msg[1]
    content_type = msg[4]
    charset = msg[5]
    body = (str(msg[15] + msg[16]))

    assert HTTP == 'HTTP/1.1'
    assert status_code == '200'
    assert content_type == 'text/plain;'
    assert charset == 'charset=utf-8'
    assert body == "HelloWorld"


def test_error():
    """Test to get an error response."""
    from server import response_error
    msg = response_error()
    msg = msg.split()
    HTTP = msg[0]
    status_code = msg[1]
    content_type = msg[6]
    charset = msg[7]
    body = (str(msg[17] + msg[18]))

    assert HTTP == 'HTTP/1.1'
    assert status_code == '500'
    assert content_type == 'text/plain;'
    assert charset == 'charset=utf-8'
    assert body == "ServerError"
