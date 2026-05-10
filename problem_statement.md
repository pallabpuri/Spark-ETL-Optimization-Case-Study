# Business Problem

A large ETL pipeline processing customer transaction data was taking over 2 hours to complete.

Problems observed:
- Excessive shuffle operations
- Data skew during joins
- Small file problem
- Inefficient partitioning
- High executor memory pressure
- Slow aggregations

Business impact:
- Increased cloud cost
- SLA breaches
- Delayed analytics reporting
- Pipeline instability
