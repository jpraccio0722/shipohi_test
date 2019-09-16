# shipohi_test
Shipohi code test

To run project: docker-compose up --build in the project root directory.

## Endpoints

#### http://localhost:8080/api/v1/warehouse/

POST creates a new warehouse
```json 
{
	"address": {
		"address1": "346 Broadway",
		"city": "New York",
		"state_province": "NY",
		"post_code": "10013",
		"country_code": "US"
	}	
}
```

#### http://localhost:8080/api/v1/order/
POST creates a new order
```json
{
	"shipping_address": {
		"address1": "450 W 34th Street",
		"city": "New York",
		"state_province": "NY",
		"post_code": "10001",
		"country_code": "US"
	},
	"line_items": [
		{
			"sku": "1110011aaaa",
			"quantity": 1,
			"name": "stuff",
			"price": 1.99
		}
	],
	"customer": {
		"first_name": "Jesse",
		"last_name": "Raccio",
		"phone": "203-779-9459",
		"email": "jpraccio@gmail.com"
	},
	"status": "order_created"
}
```
