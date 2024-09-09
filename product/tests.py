import pytest
from order.factories import CategoryFactory, ProductFactory
from order.models import Category, Product

@pytest.mark.django_db
def test_category_factory():
    category = CategoryFactory()
    assert category.id is not None
    assert category.title is not None
    assert category.slug is not None
    assert category.description is not None
    assert category.active in [True, False]

@pytest.mark.django_db
def test_product_factory():
    product = ProductFactory()
    assert product.id is not None
    assert product.title is not None
    assert product.price is not None
    assert product.category is not None

@pytest.mark.django_db
def test_product_factory_with_categories():
    categories = CategoryFactory.create_batch(3)
    product = ProductFactory(category=categories)
    assert product.category.count() == 3
    for category in categories:
        assert category in product.category.all()