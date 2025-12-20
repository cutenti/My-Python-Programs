
from reTest.hash_table import HashTable


def test_hash_table_functions():
    hash_table = HashTable()

    hash_table.put("fiona", 4)
    hash_table.put("belle", 2)
    hash_table.put("aurora", 4)
    hash_table.put("ariel", 1)
    hash_table.put("cinderella", 3)

    hash_table.remove("fiona")

    assert hash_table.get("fiona") is None

    assert hash_table.get("aurora") == 4

    assert hash_table._hash("ariel") == 525 % 128


def test_empty():
    hash_table = HashTable()

    assert hash_table.get("aurora") is None
