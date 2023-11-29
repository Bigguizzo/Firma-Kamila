monthly_sales_value_seller, value_payment, percentage_of_bonus = 0
    
    monthly_sales_value_seller = getMonthly_sales_value_seller()
    value_payment = getValue_payment()
    percentage_of_bonus = getValue_percentage()
    
    seller_remuneration = 0
    seller_remuneration = monthly_sales_value_seller * percentage_of_bonus - value_payment