import pytest
from django.urls import reverse
from catalog.models import Product,Category


@pytest.mark.django_db
def test_home(client):
    response=client.get(reverse('home'))
    assert response.status_code == 200



@pytest.mark.django_db
def category_pages(client):
    assert client.get(reverse('bases')) == 200
    assert client.get(reverse('tops')) == 200
    assert client.get(reverse('gels')) == 200
    assert client.get(reverse('gelpolish')) == 200



@pytest.mark.django_db
def test_prod_detail(client):
    cat=Category.objects.create(title="Gels",slug="gels")
    prod=Product.objects.create(
        title="Milky Hard Builder Gel",
        category=cat,
        price=20.00,
        in_stock=True
    )
    url=reverse('description',kwargs={'pk':prod.pk})
    response=client.get(url)

    assert response.status_code == 200
    assert "Milky Hard Builder Gel" in response.content.decode('utf-8')




@pytest.mark.django_db
def test_product_detail_not_found(client):
    url = reverse('description', kwargs={'pk': 9999})
    response = client.get(url)
    assert response.status_code == 404