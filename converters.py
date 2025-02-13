
# Length (m)
def feet_to_meters(feet):
    """Converts feet to meters."""
    return feet * 0.3048

# Weight  (kg)
def pounds_to_kg(pounds):
    """Converts pounds (lbs) to kilograms (kg)."""
    return pounds * 0.453592

# Temperature  (°C)
def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

# Currency (INR)
def usd_to_inr(usd):
    """Converts US Dollars (USD) to Indian Rupees (INR)."""
    exchange_rate_usd_to_inr = 74.5  
    return usd * exchange_rate_usd_to_inr

def eur_to_inr(eur):
    """Converts Euros (EUR) to Indian Rupees (INR)."""
    exchange_rate_eur_to_inr = 88.2  
    return eur * exchange_rate_eur_to_inr

def jpy_to_inr(jpy):
    """Converts Japanese Yen (JPY) to Indian Rupees (INR)."""
    exchange_rate_jpy_to_inr = 0.68  
    return jpy * exchange_rate_jpy_to_inr
