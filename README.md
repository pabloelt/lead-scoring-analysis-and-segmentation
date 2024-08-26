# Lead Scoring Analysis and Segmentation

![featured](https://github.com/pabloelt/lead-scoring-analysis-and-segmentation//blob/main/00_Imagenes/featured.jpg?raw=true)

##### Table of Contents 
* [Introduction](#introduction)
* [Objectives](#objectives)
* [Project results](#project-results)
   * [Recommended actions from EDA](#recommended-actions-from-eda)
   * [Lead segmentation model](#lead-segmentation-model)
   * [Predictive lead scoring model](#predictive-lead-scoring-model)
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
* **Predictive lead scoring model:** It will assist the sales team in identifying potential customers who are most likely to convert into final clients, as well as leads that are not economically viable to pursue.

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

Four distinct potential customer profiles were identified through the implementation of the lead segmentation model. These profiles correspond to very low, low, medium, and super high-quality leads. The key actionable initiatives for each profile are summarized below.

1. The company's most valuable leads are working professionals who arrive through the lead form submission.
2. While SMS campaigns are generally effective, they should be targeted more precisely:
  * Focus on working professionals from API sources who spend above-average time on the website.
  * Avoid sending SMS to leads from Landing Page Submissions who spend minimal time on the site, as they represent the lowest quality leads and divert resources from more promising campaigns.
3. The live chat feature primarily attracts low-quality leads. The company should consider reallocating resources from this service and, for leads from API sources, prioritize email marketing and SMS campaigns instead.

### Predictive lead scoring model

A powerful predictive lead scoring model was developed using a straightforward logistic regression algorithm. After implementing this predictive model, the company has been able to:

1. Increase its conversion rate from 41.70% to 45.77%.
2. Reduce by 9.31% the workload to be managed by the sales department.
3. Reduce by 28.81% the loss in investments.
4. Increase its sales profit by 4.75%.

|   | As is  | To be  | Improvements  |
|--:|--:|--:|--:|
| Conversion rate  | 41.70%  | 45.77%  | Increased by 4.07%  |
| Workload  | 2084  | 1890  | Reduced by 9.31%  |
| Lost investment  | 6075  | 4325  | Reduced by 28.81%  |
| Sales profit  | 33021.31  | 34591.35  | Increased by 4.75%  |

## Project structure

* 📁 Datos: Project datasets.
  * 📁 Imagenes: Contains project images.
* 📁 Notebooks:
  * <mark>01_Diseño del proyecto.ipynb</mark>: Notebook compiling the initial design of the project.
  * <mark>02_Creacion del Datamart Analitico.ipynb</mark>: Notebook creating analytic data mart (loading and unifying data, applying data quality processes, and so on).
  * <mark>03_Analisis e Insights.ipynb</mark>: Notebook used for the execution of the exploratory data analysis, which collects the business insights and the recommended actionable initiatives.
* 📈 <mark>Business_Case.xlsx</mark>: Business Case excel file.

* 📁 00_Imagenes: Contains project images.
* 📁 01_Documentos: Contains basic project files:
  * <mark>leadscoring.yml</mark>: Project environment file.
  * <mark>FaseDesarrollo_Transformaciones.xlsx</mark>: Support file for designing feature transformation processes.
  * <mark>FaseProduccion_Procesos.xlsx</mark>: Support file for designing final production script.
* 📁 02_Datos
  * 📁 01_Originales
    * <mark>Leads.csv</mark>: Original dataset.
  * 📁 02_Validacion
    * <mark>validacion.csv</mark>: Sample extracted from the original dataset at the beginning of the project, which is used to check the correct performance of the model once it is put into production.
  * 📁 03_Trabajo
    * This folder contains the datasets resulting from each of the stages of the project (data quality, exploratory data analysis, variable transformation, ...).
* 📁 03_Notebooks
    * 📁 02_Development
      * <mark>01_Set Up.ipynb</mark>: Notebook used for the initial set up of the project.
      * <mark>02_Calidad de Datos.ipynb</mark>: Notebook detailing and executing all data quality processes.
      * <mark>03_EDA.ipynb</mark>: Notebook used for the execution of the exploratory data analysis.
      * <mark>04_Transformacion de datos.ipynb</mark>: Notebook that details and executes the data transformation processes necessary to prepare the variables for the models.
      * <mark>05_Modelizacion para No Supervisado.ipynb</mark>: Notebook for modeling the unsupervised Kmeans algorithm used to perform lead segmentation.
      * 06_Feature Selection.ipynb: Notebook used to make a selection of the final variables to be entered into the models.
07_Supervised Classification Modelling.ipynb: Notebook for modelling the predictive lead scoring model. Model selection, hyperparameterisation, selection of the optimal discrimination threshold and evaluation of results.
08_Production Code Preparation.ipynb: Notebook used to compile all the quality, transformation and variable selection processes, as well as the final model and execution and retraining processes, with the aim of creating the final retraining and execution pipes that condense all the aforementioned processes.
09_Retraining script.ipynb: Notebook to retrain the model with new data when necessary.
10_Execution script.ipynb: Notebook to execute the final model and obtain the results.
📁 04_Models
pipe_execution.pickle: pipe that condenses the final trained model as well as all necessary prior data transformations.
pipe_training.pickle: pipe that condenses the entire training process. It can be used to retrain the model with new data when necessary.
optimal_disc_threshold.pickle: Contains the value of the optimal discrimination threshold of the model that maximises the company's roi. It is used by pipe_training.pickle and is updated when re-training the model with pipe_training.pickle.
📁 05_Results
Project Results.ipynb: Notebook summarising the insights and KPIs improvements achieved from the exploratory data analysis as well as from the execution of the scoring and lead segmentation machine learning models.
Execution script.py: Python script to execute the model and obtain the results.
Retraining script.py: Python script to retrain the model with new data when necessary.
final features.pickle: Names of the final features pre-selected for input to the model.
