# Currency Exchange Rate Async Web Service

## Overview

Asynchronous web microservice for fetching currency exchange rates to selected target currencies. Supports querying for a specific date and implements on-disk caching to minimize API requests.

## Features

- **Async HTTP server** with `aiohttp`
- **Async HTTP client** requests for external APIs
- **On-disk cache** via `aiofiles`
- Support for querying by **currency** and **date** (with current date as default)
- **Error handling**: 404 for unknown currency, 422 for invalid date

## Endpoints

### Get Exchange Rates

#### `GET /rates`

**Query Parameters:**
- `base` *(str, required)*: ISO code of the source currency (e.g. `usd`)
- `date` *(str, optional)*: Date in ISO-8601 (`YYYY-MM-DD`). Defaults to today.

**Response:**
- Exchanged rates to a predefined static set of target currencies.

**Example**:

```
GET /rates?base=usd&date=2024-07-26
```

## API & Data Sources

- [Currency List](https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json)
- [Exchange Rates (latest)](https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{currency}.json)
- [Exchange Rates (by date)](https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@{date}/v1/currencies/{currency}.json)

## Cache Mechanism

- **Location:** Predefined folder on disk
- **Key:** `{base_currency}_{date}.json`
- Requests first check cache; if missing, fetch from API and populate cache.

## Example Usage

```http
GET /rates?base=eur
```
```http
GET /rates?base=usd&date=2024-09-28
```

### Responses

```json
{
  "base": "usd",
  "date": "2024-09-28",
  "rates": {
    "eur": 0.91,
    "rub": 93.1,
    "cny": 7.25
  }
}
```

## Error Handling

- `404 Not Found`: Unknown currency code
- `422 Unprocessable Entity`: Invalid date format

## Tech Stack

- [aiohttp](https://docs.aiohttp.org/) for web server and HTTP client
- [aiofiles](https://pypi.org/project/aiofiles/) for asynchronous filesystem caching

## Project Structure

```
├── data/
  ├── data.json (cache file)
  ├── vals.py (current stocks)
├── server.py
├── client.py
├── get_currency.py
├── common.py
├── config.py
└── README.md
```

### Quick Start

1. **Install dependencies:**
   ```bash
   pip install aiohttp aiofiles
   ```

2. **Run server:**
   ```bash
   python server.py
   ```

3. **Query exchange rates:**
   ```
   curl "http://localhost:8080/currency/{currency}/{date}"
   ```
   ```
   curl "http://localhost:8080/currency/{currency}"
   ```
