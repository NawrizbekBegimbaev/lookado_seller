# Data Model: Returns Test Automation

**Feature**: 001-returns-tests
**Date**: 2025-12-20

## Overview

This document defines the data entities and their relationships for Returns test automation. Note: This is a UI test automation project - these entities represent what is displayed in the UI, not database schema.

## Entities

### Return

Represents a return request displayed in the admin panel.

| Field | Type | Description | UI Location |
|-------|------|-------------|-------------|
| id | string | Return ID in RMA format (e.g., RMA39) | List: ID column, Detail: Title |
| numeric_id | int | Numeric portion of ID (e.g., 39) | URL path parameter |
| type | string | Return type (e.g., "Возврат без товара") | List: Тип возврата column |
| status | string | Current status | List/Detail: Status badge |
| date | datetime | Return request date | List: Дата column, Detail: below title |
| customer_name | string | Customer name | List/Detail: Покупатель |
| customer_id | string | Customer ID | List/Detail: below name |
| store_name | string | Store name | List: Магазин column, Detail: section |
| store_id | string | Store identifier | Detail: below store name |
| quantity | int | Total quantity of items | List: Кол-во column |
| amount | decimal | Total amount in sum | List: Сумма column, Detail: Summary |

### Return Status (Enum)

Possible status values with Russian labels:

| Status | Russian Label | Tab Index |
|--------|---------------|-----------|
| ALL | Все | 0 |
| PENDING | На рассмотрении | 1 |
| SELLER_APPROVED | Одобрено продавцом | 2 |
| SELLER_REJECTED | Отклонено продавцом | 3 |
| MARKETPLACE_HELP | Помощь маркетплейса | 4 |
| MARKETPLACE_APPROVED | Одобрено маркетплейсом | 5 |
| MARKETPLACE_REJECTED | Отклонено маркетплейсом | 6 |
| WAREHOUSE_RECEIVED | Получено складом | 7 |
| WAREHOUSE_REJECTED | Отклонено складом | 8 |
| RETURNED | Возвращено | 9 |
| CANCELLED | Отменено | 10 |

### Return Item

Product being returned, displayed in detail page products table.

| Field | Type | Description |
|-------|------|-------------|
| name | string | Product name |
| sku | string | Product SKU (format: SKU-XXXX) |
| barcode | string | Product barcode |
| price | decimal | Unit price |
| quantity | int | Quantity being returned |
| amount | decimal | Line total (price × quantity) |

### Return Info

Additional information about the return request.

| Field | Type | Description |
|-------|------|-------------|
| reason | string | Return reason (e.g., "Mahsulotda nuqson bor") |
| customer_comment | string | Customer's comment |
| purchase_date | datetime | Original purchase date |
| request_date | datetime | Return request date |

### Return Summary

Financial summary for the return.

| Field | Type | Description |
|-------|------|-------------|
| amount | decimal | Subtotal amount |
| commission | decimal | Commission amount |
| total_to_return | decimal | Final refund amount |

### Return History Entry

Status change history log entry.

| Field | Type | Description |
|-------|------|-------------|
| timestamp | datetime | When change occurred |
| actor | string | Who made the change |
| old_status | string | Previous status |
| new_status | string | New status |
| comment | string | Optional comment/reason |

### Return Image

Image attached to return for verification.

| Field | Type | Description |
|-------|------|-------------|
| thumbnail_url | string | Thumbnail image URL |
| full_url | string | Full-size image URL |
| index | int | Position in gallery |

## Relationships

```
Return (1) ──────< Return Item (many)
    │
    ├──────< Return History Entry (many)
    │
    ├──────< Return Image (many)
    │
    └────── Return Info (1)
            └────── Return Summary (1)
```

## State Transitions

```
                    ┌─────────────────────┐
                    │   На рассмотрении   │
                    │     (PENDING)       │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              ▼                ▼                ▼
    ┌─────────────────┐ ┌─────────────┐ ┌─────────────┐
    │Одобрено продавц.│ │Отклонено    │ │  Помощь     │
    │(SELLER_APPROVED)│ │продавцом    │ │маркетплейса │
    └────────┬────────┘ └─────────────┘ └──────┬──────┘
             │                                  │
             ▼                                  ▼
    ┌─────────────────┐              ┌─────────────────┐
    │Получено складом │              │Одобрено/Отклон. │
    │(WAREHOUSE_RECV) │              │ маркетплейсом   │
    └────────┬────────┘              └─────────────────┘
             │
             ▼
    ┌─────────────────┐
    │   Возвращено    │
    │   (RETURNED)    │
    └─────────────────┘
```

## Validation Rules

### Refund Amount
- Minimum: > 0 (cannot be zero or negative)
- Maximum: <= order total (cannot exceed original amount)

### Reject Reason
- Required: Cannot reject without providing reason
- Type: Non-empty string

### Status Transitions
- Only specific transitions allowed (see state diagram)
- Already refunded returns cannot be refunded again
