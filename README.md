# Sitech Starships
A study. *Sitech Starships* is a REST API application to support a peer-to-peer starship listing and sales platform based on starships in the Starships API (https://swapi.co/documentation#starships). The application is built for consumption by an external frontend.
## Installation
~~The application is containerised for quick and easy testing.~~ You will ~~also~~ find a `requirements.txt` file for deployment in your favourite Python virtual environment using pip ~~if you prefer~~.

The file `db.sqlite3` includes a selection of ready-to-use database entries for quick local testing. The superuser is "jabba" and their password is "jabbathehutt".

## API Documentation
### URL
**Base URL**

`https://localhost:8000/` or your preferred local URL and port of course.

**Specific Records**

Syntax
`<base_url>/<endpoint>/<id>`
should be used to retrieve existing records where <id> is the specific ID of the record required.

**List Filters**

Query parameters for list endpoints should be encoded in the URL after the endpoint:
`<base_url>/<endpoint>?<attribute>=<value>&<attribute>=<value>`

For example
`https://localhost:8000/listings?created_after=2023-12-01T:00:00:00Z&price_below=50000`

### Authorisation
There is no authorisation required.

---

### Endpoints
**Starships** `/starships`

A type of starship which might be listed for sale on this site.

**Listings** `/listings`

A starship listed for sale by a user.

*Listing Attributes*
- `id` : Listing entry unique ID.
- `created` : Entry created at time and date as ISO date/time string (YYYY-MM-ddThh:mm:ssZ).
- `updated` : Entry last updated at time and date as ISO date/time string (YYYY-MM-ddThh:mm:ss.000Z)
- `status` : Listing status as string ("active" or "inactive").
- `seller_id`\* : Seller ID of the user who is posting the Starship for sale (integer).
- `starship_id`\* : Starship ID of the starship which is for sale (integer).
- `sale_price`\* : The asking price for the Starship in credits (integer).
- `sold`: An indicator of whether the Starship has been sold (boolean).

*\* These attributes are required when posting a new listing.*

*Optional List Filters*
- `sold` : "True" or "False" (default).
- `status` : "active" or "inactive" (default).
- `added_since` : Only listings created since (as ISO time string).
- `added_before` : Only listings created before (as ISO time string).
- `price_below` : Only listings below asking price (integer in credits).
- `price_above` : Only listings above asking price (integer in credits).
- `seller_id` : Only listings sold by seller with this id (integer).
- `seller_ids[]` : Only listings sold by these comma-separated sellers (comma-separated integers).
- `starship_id` : Only listings advertising starship with this id (integer).
- `starship_ids[]` : Only listings advertising these comma-separated starship ids (comma-separated integers).
- `starship_class` : Only listings advertising starships of this class (string).
- `sort` : Sort results by this field (string). Use hyphen prefix to invert order (E.g. "sale_price" or "-sale_price").

*GET list Example*

URL: `/listings?seller_ids[]=1,3&sort=sale_price`

A list of starship listings currently for sale from sellers with IDs 1 or 2 sorted by sale_price (lowest first).

URL: `/listings?sold=True&starship_class=Corvette&sort=-created`

A list of historically sold starship listings where the starship was of class "Corvette", sorted by created date (most recent first).

*GET specific listing detail Example*

URL: `/listings/3`

Get the detail for listing with ID 3.

*PUT to change existing listing detail Example*

URL: `listings/3`

Body:
```json
{
    "status": "inactive"  
}
```
Deactivate an active listing with ID 3.

URL: `listings/3`

Body:
```json
{
    "status": "active",  
    "sale_price": 42995
}
```

Reactivate listing with ID 3 and change sale price to 42,995 credits.

*POST new listing Example*

URL: `/listings`

Body:
```json
{
  "seller_id": 4,
  "starship": "Sentinel-class landing craft",
  "sale_price": 25800
}
```

Post a new listing for a Sentinel-class landing craft being sold by user with ID 4 for 25,800 credits.

URL: `/listings`

Body:

```json
{
  "seller_id": 7563,
  "starship_id": 22,
  "sale_price": 100900
}
```

Post a new listing for a starship with ID 22 being sold by user with ID 7563 for 100,900 credits.

**Sales** `/sales`

The final recorded sale of a specific starship listed for sale on this site.

