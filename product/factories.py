import pytest
from product.factories import CategoryFactory, ProductFactory
from product.models import Category, Product

@pytest.mark.django_db
def test_category_factory():
    # Teste para verificar se a fábrica de categorias cria uma categoria corretamente
    category = CategoryFactory()
    assert category.id is not None
    assert category.title is not None
    assert category.slug is not None
    assert category.description is not None
    assert category.active in [True, False]

@pytest.mark.django_db
def test_product_factory():
    # Teste para verificar se a fábrica de produtos cria um produto corretamente
    product = ProductFactory()
    assert product.id is not None
    assert product.title is not None
    assert product.price is not None
    assert product.category is not None

@pytest.mark.django_db
def test_product_factory_with_categories():
    # Teste para verificar se a fábrica de produtos pode adicionar categorias ao produto
    categories = CategoryFactory.create_batch(3)
    product = ProductFactory(category=categories)
    assert product.category.count() == 3
    for category in categories:
        assert category in product.category.all()