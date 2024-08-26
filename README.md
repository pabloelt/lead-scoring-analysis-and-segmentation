# Lead Scoring Analysis and Segmentation

![featured](https://github.com/pabloelt/lead-scoring-analysis-and-segmentation//blob/main/00_Imagenes/featured.jpg?raw=true)

##### Table of Contents 
* [Introduction](#introduction)
* [Objectives](#objectives)
* [Project results](#project-results)
* [Project structure](#project-structure)
* [Instructions](#instructions)

<div align="justify">
 
## Introduction

The client for this project is a cosmetics ecommerce company based in Russia. They have experienced flat growth over the past few months and have hired us to analyze their transactional data and implement Conversion Rate Optimization (CRO) actions to reverse this situation.

 * [See a technical explanation of the project here](https://pabloelt.github.io/project/project3/)

## Objectives

The main objective is to analyze the transactional data to identify potential CRO actions that can increase visits, conversions, and average ticket size, thereby boosting the overall revenue of the ecommerce company. To achieve this goal, we will create advanced analytical assets such as:

* **RFM Segmentation:** Analyzing customer data based on Recency, Frequency, and Monetary value to identify key customer segments and tailor marketing strategies accordingly.
* **Recommendation System:** Developing a recommendation system to personalize the shopping experience, encouraging higher conversions and increasing the average ticket size.

These tools will help us implement effective CRO actions and drive substantial revenue growth.

## Project results

The main results obtained from this Discovery Project are summarized below:

### After analyzing the data, the baseline of the company has been found

* In each session, on average:
  * 2.2 products are viewed.
  * 1.3 products are added to the cart.
  * 0.9 products are removed from the cart.
  * 0.3 products are purchased.
* Cross-selling: median of 5 products per purchase.
* Recurrence: 10% of customers repeat purchases after the first month.
* Conversion rates:
  * 60% from views to cart additions.
  * 22% from cart additions to purchases.
  * 13% from views to purchases.
* Average monthly revenue: 125.000€

### Actionable initiatives

A plan of 10 specific initiatives, organized into five major business levers, has been derived from the exploratory data analysis to break the stagnant trend in the company over the last few months and achieve an overall increase in ecommerce revenues:

#### Actions to increase the number of views:

1. Review paid campaigns (generation and retargeting) to focus investment during the time slots between 9 am and 1 pm, and between 6 pm and 8 pm.
2. Concentrate investment for the Christmas and post-Christmas period during the Black Friday week.
3. Increase investment to reach the maximum CPA based on the identified LTV.

#### Actions to increase conversion rates:

4. Preconfigure the homepage with the products identified in the "most viewed" and "most sold" analyses.
5. Work on products with a high cart abandonment rate.
6. Work on products that are frequently viewed but infrequently purchased.

#### Actions to increase cross-selling:

 7. The median purchase is 5 products at the moment. To increase this ratio, implement real-time recommendations using the new recommendation system.

#### Actions to increase purchase frequency:

8. The 90% of the customers only make a single purchase. Create a periodic newsletter using the new recommendation system to increase visit frequency.
9. Run promotional campaigns targeting the top segments identified in the RFM segmentation.

#### Actions to improve customer loyalty:

10. Create a loyalty program based on the new RFM segmentation.

## Project structure

* 📁 Datos: Project datasets.
  * 📁 Imagenes: Contains project images.
* 📁 Notebooks:
  * <mark>01_Diseño del proyecto.ipynb</mark>: Notebook compiling the initial design of the project.
  * <mark>02_Creacion del Datamart Analitico.ipynb</mark>: Notebook creating analytic data mart (loading and unifying data, applying data quality processes, and so on).
  * <mark>03_Analisis e Insights.ipynb</mark>: Notebook used for the execution of the exploratory data analysis, which collects the business insights and the recommended actionable initiatives.
* 📈 <mark>Business_Case.xlsx</mark>: Business Case excel file.
