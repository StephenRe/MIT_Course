/*
2005
Motor vehicle and parts dealers	12	888307
Furniture and home furnishings stores	12	109120

all
Motor vehicle and parts dealers	350	24,809,799	
Furniture and home furnishings stores	350	2,699,781	
*/

SELECT
	NAICS_code,
    Business_type,
	month_year,
    month_start,
    sales,
    lag(sales) over(partition by NAICS_code order by month_start) as lag_sales,
    (sales - lag(sales) over(partition by NAICS_code order by month_start)) / lag(sales) over(partition by NAICS_code order by month_start) as pct_change
FROM module_8_project.mrts_data
where NAICS_code in (441)
order by NAICS_code, month_start
;

/*
45111	Sporting goods stores
45112	Hobby, toy, and game stores
451211	Book stores
*/

SELECT
	NAICS_code,
    Business_type,
    month(month_start) as monthnum,
    left(month_year, length(month_year)-5) as month,
    avg(cpi_adjd)
FROM module_8_project.mrts_data
where NAICS_code in (45111,45112,451211)
group by 
	NAICS_code,
    Business_type,
    month(month_start),
     left(month_year, length(month_year)-5)
order by monthnum, NAICS_code
;

/*
trends of retail and food services categories
limits on years and months and industries.
*/


use module_8_project;

select
	*,
    (sales - lag(sales) over(partition by NAICS_code order by year)) / lag(sales) over(partition by NAICS_code order by year) * 100 as pct_change
from (
	select
		m.naics_code,
		m.business_type,
		m.year,
		sum(m.sales) as sales
	from mrts_data m
	where naics_code in (1)
		and year between 1992 and 2006
	group by 
		m.naics_code,
		m.business_type,
		m.year
) a
;


/*
mens and womens clothing stores
44811 | Men's clothing stores
44812 | Women's clothing stores
*/

use module_8_project;

select
	*,
    (sales - lag(sales) over(partition by NAICS_code order by year)) / lag(sales) over(partition by NAICS_code order by year) * 100 as pct_change
from (
	select
		m.naics_code,
		m.business_type,
		m.year,
		sum(m.sales) as sales
	from mrts_data m
	where naics_code in (44811, 44812)
		and year between 1992 and 2006
	group by 
		m.naics_code,
		m.business_type,
		m.year
) a
;

select
	m.year,
    sum(sales) as sales,
	sum(case when NAICS_code = 44811 then sales end) as mens_sales,
    sum(case when NAICS_code = 44812 then sales end) as womens_sales,
    round(sum(case when NAICS_code = 44811 then sales end)/sum(sales) * 100,2) as mens_pct,
    round(sum(case when NAICS_code = 44812 then sales end)/sum(sales) * 100,2)as womens_pct,
    100.0 as total_pct
from mrts_data m
where naics_code in (44811, 44812)
group by m.year
;

select
	Business_type,
    m.year,
    sum(m.sales)/a.sales as gender_pct
from mrts_data m
join (	select
			m.year,
			sum(sales) as sales
		from mrts_data m
		where naics_code in (44811, 44812)
		group by m.year
	) a on a.year = m.year
where naics_code in (44811, 44812)
group by Business_type, m.year
;

-- rolling 3 previous months
select 
	Business_type,
    month_start,
    month_year,
    sales,
    cpi_adjd,
    sum(sales) over(partition by Business_type order by month_start rows between 2 PRECEDING and CURRENT ROW) as rolling_sum_sales,
    sum(cpi_adjd) over(partition by Business_type order by month_start rows between 2 PRECEDING and CURRENT ROW) as rolling_sum_cpi,
    avg(sales) over(partition by Business_type order by month_start rows between 2 PRECEDING and CURRENT ROW) as rolling_avg_sales,
    avg(cpi_adjd) over(partition by Business_type order by month_start rows between 2 PRECEDING and CURRENT ROW) as rolling_avg_cpi
from mrts_data
where naics_code in (44811, 44812)
;


select 
	Business_type,
    month_start,
    month_year,
    sales,
    cpi_adjd,
    sum(sales) over(partition by Business_type order by month_start rows between 3 PRECEDING and CURRENT ROW) as rolling_sum_sales,
    sum(cpi_adjd) over(partition by Business_type order by month_start rows between 3 PRECEDING and CURRENT ROW) as rolling_sum_cpi,
    avg(sales) over(partition by Business_type order by month_start rows between 3 PRECEDING and CURRENT ROW) as rolling_avg_sales,
    avg(cpi_adjd) over(partition by Business_type order by month_start rows between 3 PRECEDING and CURRENT ROW) as rolling_avg_cpi
from mrts_data
where naics_code in (44811, 44812)
;






