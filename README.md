# Lead Scoring Analysis and Segmentation

![featured](https://github.com/pabloelt/lead-scoring-analysis-and-segmentation//blob/main/00_Imagenes/featured.jpg?raw=true)

##### Table of Contents 
* [Introduction](#introduction)
* [Objectives](#objectives)
* [Project results](#project-results)
 * [Recommended actions from EDA](#recommended-actions-from-eda)
* [Project structure](#project-structure)
* [Instructions](#instructions)

<div align="justify">
 
## Introduction

The client for this project is an online teaching company that offers a high-value online course designed to train professionals in the data science sector. The company advertises this course on various websites and search engines. When people visit the website—promoted effectively by the marketing department—they may browse the course, fill out a form, or watch related videos. If they provide their email address or phone number through a form, they are classified as a lead. Additionally, the company also acquires leads through referrals from past clients.

Once these leads are acquired, the sales team begins reaching out via calls, emails, and other forms of communication. However, while some leads convert into customers, most do not, leading to inefficiencies that negatively impact the company’s profitability.

 * [See a technical explanation of the project here](https://pabloelt.github.io/project/project5/)

## Objectives

The main objective is to analyse the historical leads information of the company to propose potential actions that will increase the overall turnover and reverse the low conversion rate at which the company is operating. To achieve this goal, we will create advanced analytical assets such as:

* **Lead segmentation model:** This tool will help to identify the key customer groups interested in the product, enabling the sales team to tailor marketing efforts effectively for each identified segment.
***Predictive lead scoring model:** It will assist the sales team in identifying potential customers who are most likely to convert into final clients, as well as leads that are not economically viable to pursue.

## Project results

### Recommended actions from EDA

Several insights have been uncovered through the exploratory data analysis. The main actionable initiatives are summarized below.

**Actions to improve leads' management:**

1. Enhance the quality of survey or form questions to gather more user inputs and reduce the occurrence of NaN or default (‘Select’) values.
2. Collect timestamps for website visits to enable seasonality analysis and implement cookies to track and identify users as they navigate different pages on the website.
3. Develop a new **lead segmentation algorithm** that categorizes the company's diverse lead profiles, enabling the identification of the best-fitting group for each new lead. This will allow for more personalized commercial actions.

**Actions to improve lead-to-customer conversion rate:**

1. Implement a **predictive lead scoring algorithm** that identifies individuals most likely to convert into paying customers. This will reduce the sales team's workload allowing them to focus more time on engaging with the most promising leads.

**Actions to improve commercial and marketing channels performance:**

1. Enhance the content strategy across the website, lead magnet, and emails to attract more traffic and increase user engagement. Focus on creating tailored content specifically for working professionals interested in the data science sector.
2. Develop a referral program to motivate existing customers to recommend the course to their friends, family, and colleagues.
3. Allocate more resources to acquiring leads through ‘Reference’ channel, as they demonstrate the highest conversion rate.
4. Boost investments in SMS campaigns, given their strong performance.

### Lead segmentation model

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
