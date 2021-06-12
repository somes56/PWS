from dataclasses import dataclass


@dataclass
class DefaultInvoiceItemUpsertDto:
    InvoiceID: str = ""
    ItemID: str = ""
    ItemQuantity: int = 0
    ItemUnitAmount: float = 0.00
    ItemAmount: float = 0.00
