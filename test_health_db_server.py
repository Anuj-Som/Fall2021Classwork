from health_db_server import add_database_entry
from health_db_server import initialize_server

initialize_server()


def test_add_database_entry():
    from health_db_server import add_database_entry
    expected_name = "David"
    answer = add_database_entry(expected_name, 5, "0+")
    print(answer)
    assert answer.name == expected_name