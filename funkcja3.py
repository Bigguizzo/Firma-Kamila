def getValue_percentage():
        percentage_of_bonus = 0
        monthly_sales_value_seller = getMonthly_sales_value_seller()
        if(monthly_sales_value_seller < 10000):
            percentage_of_bonus = 0.10
        if(monthly_sales_value_seller > 10000 and monthly_sales_value_seller < 14999.99):
            percentage_of_bonus = 0.12
        if(monthly_sales_value_seller > 10000 and monthly_sales_value_seller < 17999.99):
            percentage_of_bonus = 0.14
        if(monthly_sales_value_seller > 10000 and monthly_sales_value_seller < 21999.99):
            percentage_of_bonus = 0.16
        if(monthly_sales_value_seller > 22000):
            percentage_of_bonus = 0.18
        return percentage_of_bonus