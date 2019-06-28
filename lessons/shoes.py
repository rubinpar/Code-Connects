# 24 June 2019

class Shoe: 
  """
  Shoes have:
    - Price
    - Color
    - Size
    - Pattern
    - Brand
  """
  def __init__(self, price, color, size, pattern, brand):
    self.price = price
    self.color = color
    self.size = size
    self.pattern = pattern
    self.brand = brand

  def calculate_sale_price(self, percentage):
    # $108 on 10% sale then it costs $108 - (0.1 * $108) = $108 - $10.80 = $97.20
    return self.price - (self.price * percentage/100)

marcus_shoes = Shoe(87, "Black", 10.5, "plain", "Nike")
rubins_discount = 20
print("The shoes originally cost {}".format(marcus_shoes.price))
print("The shoes now cost {}".format(marcus_shoes. (rubins_discount)))


shoe_price = 87
shoe_color = "black"
