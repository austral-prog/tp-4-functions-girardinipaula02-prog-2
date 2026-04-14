# ---- Funciones provistas (NO modificar) ----
def apply_discount(price, discount_pct):
    """Dado un precio y un porcentaje de descuento, retorna el precio con el descuento aplicado."""
    return price * (1 - discount_pct / 100)


def apply_tax(price, tax_pct):
    """Dado un precio y un porcentaje de impuesto, retorna el precio con el impuesto aplicado."""
    return price * (1 + tax_pct / 100)


def final_price(price, quantity, discount_pct, tax_pct):
    # 1. subtotal
    subtotal = price * quantity

    # 2. aplicar descuento
    con_descuento = apply_discount(subtotal, discount_pct)

    # 3. aplicar impuesto
    con_impuesto = apply_tax(con_descuento, tax_pct)

    # 4. redondear
    return round(con_impuesto, 2)


def best_deal(price_a, qty_a, disc_a, price_b, qty_b, disc_b, tax_pct):
    total_a = final_price(price_a, qty_a, disc_a, tax_pct)
    total_b = final_price(price_b, qty_b, disc_b, tax_pct)

    if total_a <= total_b:
        return "A"
    else:
        return "B"