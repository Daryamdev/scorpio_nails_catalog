import pytest
from catalog.models import Product, Category

@pytest.mark.django_db
def test_product():
    cat = Category.objects.create(title="Gels", slug="gels")
    
    prod = Product.objects.create(
        title="Shimmer Pink Hard Gel",
        category=cat,
        price=22.00,
        in_stock=True,
        description="Structural pink builder gel loaded with micro-shimmer particles for a glowing, dimensional finish. Combines extreme durability with a gentle pink sparkle."
    )

    assert prod.title == "Shimmer Pink Hard Gel"
    assert prod.category.title == "Gels"
    assert str(prod) == "Shimmer Pink Hard Gel"
    assert str(cat) == "Gels"



@pytest.mark.django_db
def test_product2():
        cat=Category.objects.create(title="Top-Coats",slug="top-coats")

        prod=Product.objects.create(
            title="Milky Way Top (no wipe)",
            category=cat,
            price=17.00,
            in_stock=True,
            description="Non-tacky top coat infused with a soft milky hue and tiny galactic micro-shimmers. Instantly transforms any color into a dreamy, space-inspired design."
        )



        assert prod.title == "Milky Way Top (no wipe)"
        assert prod.category.title== "Top-Coats"
        assert str(prod)== "Milky Way Top (no wipe)"
        assert str(cat)== "Top-Coats"