
import pytest
import app


@pytest.fixture
def setup_database(tmp_path, monkeypatch):
    # Give every test its own temporary database.
    test_db = tmp_path / "test_orders.db"
    monkeypatch.setattr(app, "DB_NAME", str(test_db))
    app.create_table()


def test_add_and_get_order(setup_database):
    app.add_order("Anuska", 500)

    orders = app.get_orders()

    assert len(orders) == 1
    assert orders[0][1] == "Anuska"
    assert orders[0][2] == 500


def test_reject_empty_customer(setup_database):
    with pytest.raises(ValueError):
        app.add_order("", 500)


def test_reject_zero_amount(setup_database):
    with pytest.raises(ValueError):
        app.add_order("Anuska", 0)


def test_reject_negative_amount(setup_database):
    with pytest.raises(ValueError):
        app.add_order("Anuska", -100)


def test_empty_database(setup_database):
    assert app.get_orders() == []

def test_total_revenue(setup_database):
    app.add_order("Anuska", 500)
    app.add_order("Rahul", 750)

    assert app.get_total_revenue() == 1250