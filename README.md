**Objective**
The goal of this project is to streamline and optimize the process of data extraction, transformation, and analysis for a growing e-commerce platform. The project involves setting up an efficient data pipeline that can handle large volumes of transactional and user data, ensuring that data is clean, well-organized, and ready for analysis

**Tools**
- Cloud Storage: Data will be stored and managed in Google Cloud Storage, which will act as a centralized repository for raw data before being processed.
- BigQuery: Data will be loaded into BigQuery for further analysis and querying.
- DBT: The transformation layer will be handled by DBT, ensuring that all necessary data transformations (such as cleaning, aggregating, and joining) are performed efficiently and accurately.
- Airflow: Airflow will be used to orchestrate the pipeline, automating the extraction, transformation, and loading processes.
- Looker Studio: Visualization and reporting will be done in Looker Studio, where dashboards will be created to provide insights into various aspects of the business.

**Data Pipeline Workflow**

**Data Extraction**
Raw data is extracted from Cloud Storage, which contains CSV or other file formats for various tables like product, transactions, and users. This ensures that the data is securely stored and easily accessible for processing.

**Data Transformation** 
The data extraction process follows an ELT (Extract, Load, Transform) approach. The data is first loaded into the data warehouse (BigQuery) and then transformed using DBT. This approach allows us to take advantage of BigQuery's scalability and DBT's transformation capabilities, ensuring the data is optimized for analysis.

**Conversion Funnel**
The conversion funnel model is already aligned with the overall goal of tracking user behavior, from viewing products to completing purchases. This part of the project ensures that we can analyze the steps users take within the platform and identify any potential bottlenecks or areas for improvement in the sales process.
