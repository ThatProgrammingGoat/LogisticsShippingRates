# Shipping Cost Calculator

## Input packcage weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
Shipping_cost= weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")
