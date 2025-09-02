def currency(value: float) -> str:
    try:
        return f"${float(value):,.2f}"
    except Exception:
        return str(value)


def register_template_helpers(app):
    app.jinja_env.filters["currency"] = currency
